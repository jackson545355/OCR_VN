from imutils import paths
from pdf2image import convert_from_path
from tqdm import tqdm
import tempfile
import os
import cv2
inputDirt = 'input_image/'

CROP_DIR = 'input_image/'
def preprocess(fname):
    imageName = list(paths.list_images(fname))

    outputDir = 'input_image/'
    # Store Pdf with convert_from_path function
    with tempfile.TemporaryDirectory() as path:
        print(path)
        images = convert_from_path(fname, output_folder=path)
        for i in tqdm(range(len(images))):
            # Save pages as images in the pdf
            images[i].save(outputDir + "/page_%03d.jpg" % i, 'JPEG')


if __name__ == "__main__":
    inputDir = 'inputpdf/'
    fname = inputDir + "DÂN LÀNG HỒ.pdf"
    preprocess(fname)
    for filename in os.listdir(inputDirt):
        f = os.path.join(inputDirt, filename)
        img = cv2.imread(f)

        # Shape of the image
        # [rows, columns]
        try:
            # resize image
            dim = (1590, 1220)
            resized = cv2.resize(img, dim, interpolation=cv2.INTER_AREA)
            row = img.shape[0]
            col = img.shape[1]
            img = img[int(row * 0.1):, ]
            cv2.imwrite(CROP_DIR + '/' + filename, img)
        except:
            continue
