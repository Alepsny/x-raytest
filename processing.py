from PIL import Image, ImageEnhance
import cv2

source = 'x-ray.tiff'
final_file = 'final.jpg'

img = cv2.imread(source, cv2.IMREAD_GRAYSCALE)
cv2.imwrite(final_file, img)

im = Image.open(final_file)
enhancer = ImageEnhance.Brightness(im)
factor = 4
im_output = enhancer.enhance(factor)

enhancer = ImageEnhance.Sharpness(im_output)
factor = 2
im_s_1 = enhancer.enhance(factor)
im_s_1.save(final_file)

img = cv2.imread(final_file)
gas_im = cv2.GaussianBlur(img, (33, 33), 0)
cv2.imwrite(final_file, gas_im)



