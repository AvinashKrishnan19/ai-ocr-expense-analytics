import pytesseract
import os

#1. path setting to the tesseract
pytesseract.pytesseract.tesseract_cmd=r"G:\tessaract\tesseract.exe"

INPUT_FOLDER = "outputocrimage"
OUTPUT_FOLDER = "extracted_text.txt"

def perform(INPUT_FOLDER,OUTPUT_FOLDER):
    all_extracted_text= ""
    for filename in os.listdir(INPUT_FOLDER):
        if filename.endswith((".jpg", ".jpeg", ".png")):
            image_path = os.path.join(INPUT_FOLDER,filename)
            try:
                text =pytesseract.image_to_string(image_path)
                print("-"*20)
                print(text.strip)
                print("-"*20)
                all_extracted_text += f"\n--Text from {filename}--\n{text}\n"
            except Exception as e:
                print(f"error in {filename}{error}")


        with open(OUTPUT_FOLDER, 'w', encoding='utf-8') as f:
            f.write(all_extracted_text)



        print("completed ocr")

if __name__ == "__main__":
    perform(INPUT_FOLDER,OUTPUT_FOLDER)


