from pdf2image import convert_from_path
from PIL import Image
import numpy as np

from paddleocr import PaddleOCR

# Convert PDF to images

# print(len(pages))

# def find_line_number(result, name):

    # Process OCR result
    # for idx in range(len(result)):
    #     res = result[idx]
    #     print(res)
    #     print("-----------------")
    #     for line in res:
    #         # print([line[1][0]])
    #         textual_data = textual_data+ line[1][0].lower() + " "
        
    #     print(res)


    # print(textual_data)

    # return textual_data.find(name) >= 0


def find_name(name, path_to_resume):
    pages = convert_from_path(path_to_resume, 500, poppler_path='E:/cholamandalam-practice/poppler-23.11.0/Library/bin')

    result = ocr.ocr(np.array(pages[0]), cls=True)  # Convert PIL image to NumPy array

    print(len(result[0]))
    print("------------------------\n\n\n" )

    textual_data = ""

    for idx in range(len(result)):
        res = result[idx]
        # print(res)
        # print("-----------------")
        for line in res:
            print([line[1][0]])
            print("-----------------")

            textual_data = line[1][0].lower()


        
        # print(res)


    print(textual_data)

    return textual_data.find(name) >= 0

    


            


# OCR on the first page
ocr = PaddleOCR(use_angle_cls=True, lang='en')  # need to run only once to download and load model into memory



name = input()

print(find_name(name.lower(), 'Harsh_Kumar_Jain_Resume.pdf'))