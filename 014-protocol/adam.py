import cv2
import numpy as np

# raw.jpg => 28x28 (stor bild)

SIZE = 28

DIR = "e2e4/"

cornerFile = 'data/' + DIR + 'corners.txt'
infile = 'data/' + DIR + 'raw.jpg'
outfile = 'data/' + DIR + f'{SIZE}x{SIZE}.jpg'

with open(cornerFile) as f: corners = [int(item) for item in f.readline().split(" ")]
corners = [(corners[i], corners[i + 1]) for i in range(0, 8, 2)]

image = cv2.imread(infile)
w,h = (33 * SIZE, 20 * SIZE)
target_corners = np.float32([[0, 0], [w, 0], [w, h], [0, h]])
transform_matrix = cv2.getPerspectiveTransform(np.float32(corners), target_corners)
transformed_image = cv2.warpPerspective(image, transform_matrix, (w,h))
gray_image = cv2.cvtColor(transformed_image, cv2.COLOR_BGR2GRAY)
gray8 = gray_image.astype('uint8')
cv2.imwrite(outfile, gray8)
