from flask import Flask, render_template, request, jsonify
import torch
from PIL import Image
import pathlib
import threading
import numpy as np
import cv2
import easyocr
import base64


list_of_details = ["aadhaar number", "address", "dob", "emblem", "father", "gender", "goi symbol", "issue date", "logo", "name", "photo", "uiai icon", "uiai symbol", "vid", "yob"]
reader = easyocr.Reader(['en']) # this needs to run only once to load the model into memory

text_extracted = {
    "type" : "None",
    "address" : "Address not extracted",
    "dob" : "DOB not extracted",
    "gender" : "Gender not extracted",
    "aadhaar number" : "Aadhaar number not found",
    "name" : "Name not found"
}

temp = pathlib.PosixPath
pathlib.PosixPath = pathlib.WindowsPath

app = Flask(__name__)
lock = threading.Lock()


def get_cropped_image(image, bounding_box):
    """
        fetches the cropped part of image where a particular
        document is predicted to be according to the bounding
        box coordinates
    """

    x1 = np.int32(bounding_box[0])
    y1 = np.int32(bounding_box[1])
    x2 = np.int32(bounding_box[2])
    y2 = np.int32(bounding_box[3])

    cropped_image = image[y1:y2, x1:x2]
    cropped_image = cv2.cvtColor(cropped_image, cv2.COLOR_BGR2RGB)

    if isinstance(cropped_image, torch.Tensor) and cropped_image.is_cuda:
        cropped_image = cropped_image.cpu()

    return cropped_image


def final_function(image, pandas_res, text_extracted, list_of_details):

    for bbox in pandas_res:
        

        cropped_image = get_cropped_image(image, bbox)
        

        cv2.imwrite("filename.jpg", cropped_image)

        print(int(bbox[-1]))

        # results = ocr.ocr(cropped_image, cls=True)
        # # print(results)

        # for line in results:
        #     text = line
        #     print(text)

        results = reader.readtext(cropped_image)
        # print(results)

        predicted_outcome = int(bbox[-1])

        if predicted_outcome == 10:
                    # Convert the image to base64 encoding
                    _, img_encoded = cv2.imencode('.jpg', cropped_image)
                    base64_encoded_image = base64.b64encode(img_encoded).decode('utf-8')

                    # Save base64 encoded image to a text file
                    with open("base64_encoded_image.txt", "w") as file:
                        file.write(base64_encoded_image)

        if results:
            if results[0][1] and predicted_outcome in [0,1,2,5,9]:
                # print(list_of_details[predicted_outcome])
                text_extracted[list_of_details[predicted_outcome]] = results[0][1]

    return text_extracted


model = torch.hub.load('yolov5', 'custom', path = r'aadhar_extraction_model_with_photo_runs\\train\\exp\weights\best.pt', force_reload = True, source='local')

def process_image(image_file):
    img = np.array(Image.open(image_file))

    # Acquire the lock if needed
    with lock:
        results = model(img)
        print(results)

        results= results.xyxy[0].cpu()
        res = final_function(img, results,text_extracted, list_of_details)
        return res

@app.route("/", methods=['GET','POST'])
def home():

    

    return render_template('upload_file.html')


@app.route("/details", methods=["POST"])
def details_to_be_displayed():

    if request.method == 'POST':

        image_file = request.files['file']

        # img = Image.open(image_file)

        # Start a new thread to process the image
        print("------------")
        result = process_image(image_file)
        

        if result['address'] == "Address not extracted":
            result['type'] = "Front"
        else:
            result['type'] = 'Back'

    return jsonify(result)











if __name__ == '__main__':

    app.run(debug=True)