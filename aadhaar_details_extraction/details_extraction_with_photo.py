import torch
from PIL import Image
import pathlib
import cv2
# from paddleocr import PaddleOCR
import easyocr
import base64



import numpy as np

# ocr = PaddleOCR(use_angle_cls=True, lang='en')

reader = easyocr.Reader(['en']) # this needs to run only once to load the model into memory
# result = reader.readtext('chinese.jpg')

list_of_details = ["aadhaar number", "address", "dob", "emblem", "father", "gender", "goi symbol", "issue date", "logo", "name", "photo", "uiai icon", "uiai symbol", "vid", "yob"]



def get_cropped_image(image, bounding_box):
    """
        fetches the cropped part of image where a particular
        document is predicted to be according to the bounding
        box coordinates
    """

    # bounding_box = bounding_box


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


text_extracted = {
    "dob" : "DOB not extracted",
    "gender" : "Gender not extracted",
    "aadhaar number" : "Aadhaar number not found",
    "name" : "Name not found"
}



temp = pathlib.PosixPath
pathlib.PosixPath = pathlib.WindowsPath


model = torch.hub.load('yolov5', 'custom', path = r'aadhar_extraction_model_with_photo_runs\\train\\exp\weights\best.pt', force_reload = True, source='local')


try:
    img = cv2.imread("pradeep_rotated_aadhaar.jpg")
    img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

    copy_img = img.copy()

    results = model(img)  # inference

    results.show()

    # print(results)
    results = results.xyxy[0].cpu()
    print(results)

    final_function(copy_img, results, text_extracted, list_of_details)

except Exception as e:

    print(e)
    print("Error occurred")


print(text_extracted)
# print("everything works well")