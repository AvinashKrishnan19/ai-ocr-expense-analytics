import cv2
import os


input_folder ="inputocrimage"
output_folder="outputocrimage"

def image_cleaning(input_folder,output_folder):
    valid_extension=(".jpg",".jpng",".png")
    convert_count=0
    for filename in os.listdir(input_folder):
        if filename.lower().endswith(valid_extension):
            input_path = os.path.join(input_folder,filename)
            output_path = os.path.join(output_folder,filename)
            try:
                colour_image = cv2.imread(input_path)
                #converting black and white
                grey_image = cv2.cvtColor(colour_image,cv2.COLOR_BGR2GRAY)
                #removing noise from the image
                blur_image =cv2.GaussianBlur(grey_image,(5,5),0)
                #otsu's binarizations
                ret, binary_image = cv2.threshold(blur_image, 0, 255, cv2.THRESH_BINARY | cv2.THRESH_OTSU)
                cv2.imwrite(output_path,binary_image)
                convert_count += 1
                print(f"Image converted{convert_count}{filename}")
            except Exception as e:
                print(f"failed to convert {filename}{e}")

if __name__ == "__main__":
    image_cleaning(input_folder,output_folder)

                      









