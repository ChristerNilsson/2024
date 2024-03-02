import tensorflow as tf
from tensorflow.keras.models import load_model
# from tensorflow.keras.datasets import mnist
# from tensorflow.keras.utils import to_categorical
import time

import cv2
import numpy as np

# Load the biased image of the chessboard
image = cv2.imread('data/5254.jpg')
corners = [int(corner) for corner in "136 241 3321 247 3322 2165 134 2163".split(" ")]

#image = cv2.imread('data/e2e4.jpg')
#corners = [int(corner) for corner in "138 241 3323 248 3321 2169 132 2162".split(" ")]

temp = []
for i in range(0,8,2):
    temp.append((corners[i],corners[i+1]))
corners = temp

# Function to transform the image based on the corners
def transform_image(image, corners):
    # Define the target size for the chessboard (e.g., 400x400)
    target_size = (33*28, 20*28)

    # Define the target corners for the transformation
    target_corners = np.float32([[0, 0], [target_size[0], 0], [target_size[0], target_size[1]], [0, target_size[1]]])

    # Calculate the perspective transformation matrix
    transform_matrix = cv2.getPerspectiveTransform(np.float32(corners), target_corners)

    # Apply the perspective transformation to the image
    transformed_image = cv2.warpPerspective(image, transform_matrix, target_size)

    return transformed_image


# Function to extract square images and convert to grayscale
def extract_square_images(image):
    # Define the dimensions of each square (e.g., 50x50)
    square_size = 28

    square_images = []

    for row in range(20):
        for col in range(33):
            # Calculate the coordinates of the top-left corner of the current square
            x1 = col * square_size
            y1 = row * square_size

            # Extract the region of interest (ROI)
            square_roi = image[y1:y1 + square_size, x1:x1 + square_size]

            # Resize the ROI to 28x28
            resized_roi = cv2.resize(square_roi, (28, 28))

            # Convert the resized ROI to grayscale
            grayscale_roi = cv2.cvtColor(resized_roi, cv2.COLOR_BGR2GRAY)

            for i in range(28):
                for j in range(28):
                    grayscale_roi[i][j] = 255 - grayscale_roi[i][j]
                    if grayscale_roi[i][j] < 50: grayscale_roi[i][j] = 0
                    if i in [0,1,26,27] or j in [0,1,26,27]: grayscale_roi[i][j] = 0
                    # if i in [0,27] or j in [0,27]: grayscale_roi[i][j] = 0

            square_images.append(grayscale_roi)

    return square_images


# Apply perspective transformation
transformed_image = transform_image(image, corners)

# Extract square images and convert to grayscale
square_images = extract_square_images(transformed_image)

# Display the first square image
cv2.imshow('Square Image', square_images[5*33+8])
cv2.waitKey(0)
cv2.destroyAllWindows()

##################################################

# pip install pyzbar
# pip install opencv-python-headless

# import cv2
# from pyzbar.pyzbar import decode
#
# def find_qr_codes(image_path):
#     # Load the image
#     image = cv2.imread(image_path)
#
#     # Convert the image to grayscale
#     gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
#
#     # Find QR codes in the image
#     qr_codes = decode(gray)
#
#     # Extract QR code positions
#     positions = [(code.rect.left, code.rect.top, code.rect.width, code.rect.height) for code in qr_codes]
#
#     return positions
#
# # Path to the image containing QR codes
# image_path = "path/to/your/image.jpg"
#
# # Find QR codes in the image
# qr_code_positions = find_qr_codes(image_path)
#
# # Print positions
# for i, position in enumerate(qr_code_positions):
#     print(f"QR Code {i+1} Position: {position}")


antal = 0

# Load MNIST dataset
# (_, _), (x_test, y_test) = mnist.load_data()

x_test = np.ndarray(660*28*28)
x_test = x_test.reshape(660,28,28)

for i in range(660):
    # x_test[i] = square_images[i].astype('float32') / 255
    x_test[i] = square_images[i] / 255

# Preprocess the data
# x_test = x_test.reshape(-1, 28, 28, 1).astype('float32') / 255

#x_test = square_images.reshape(-1, 28, 28, 1).astype('float32') / 255
# x_test = square_images / 255

# y_test = to_categorical(y_test, 10)

# Load pre-trained model
#lettersModel = load_model('letters.h5')  # Load your trained model here
digitsModel = load_model('digits.h5')  # Load your trained model here

# Evaluate the model
# loss, accuracy = model.evaluate(x_test, y_test, verbose=0)
# print(f'Test accuracy: {accuracy}')

# Make predictions
#predLetters = lettersModel.predict(x_test)
predDigits = digitsModel.predict(x_test)

# Example of predicting the first image
index = 0  # Change this index to predict other images

# White Black
facit = """4244 7776
3164 6877
5253 7866
2142 5878
7163 4746
6143 2726
8283 3827
7274 6645
6473 4524
4352 2847
3233 2436
8384 4766
7475 6647
8485 5756
8576 6776
5354 4645
2224 4554
4254 3644
6344 2754
4456 7733
5161 4857
5668 1868
1131 5481
4123 7888
2333 5777
3337 8154
5274 5465
7452 6583
6151 6865
3141 6575
3748 7768
4875 6824
4142 2421
5241 2154
4252 5481
5142 8136
5258 8877
7557 7786
7364"""

# facit = """d2d4 g7g6
# c1f4 f8g7
# e2e3 g8f6
# b1d2 e878
# g1f3 d7d6
# f1d3 b7b6
# h2h3 c8b7
# g2g4 f6d5
# f4g3 d5b4
# d3e2 b8d7
# c2c3 b4c6
# h3h4 d7f6
# g4g5 f6d7
# h4h5 e7e6
# h5g6 f7g6
# e3e4 d6d5
# b2b4 d5e4
# d2e4 c6d4
# f3d4 b7e4
# d4e6 g7c3
# e1f1 d8e7
# e6f8 18f8
# a1c1 e4h1
# d1b3 g8h8
# b3c3 e8g8
# c3c7 h1e4
# e2g4 e4f5
# g4e2 f583
# f1e1 f8f5
# c1d1 f5g5
# c7d8 g7f8
# d8g5 f8b4
# d1d2 b4b1
# e2d1 b1e4
# d2e2 e4h1
# e1d2 h1c6
# e2e8 h8g7
# g5e7 g7h6
# g3f4"""


facit = facit.replace("\n"," ").split(" ")
start = time.time_ns()
for i in range(len(facit)):
    row = i // 2
    row = row % 20
    coloffset = 2 * (i//40)
    col = i % 2 + coloffset
    index = row * 33 + [1,6,12,17,23,28][col]
    # print(i,index)

    # z = tf.argmax(predLetters[index]).numpy()

    # p0 = "abcdefgh"[tf.argmax(predLetters[index]).numpy()-1]
    p0 = "12345678"[tf.argmax(predDigits[index]).numpy()-1]
    p1 = "12345678"[tf.argmax(predDigits[index+1]).numpy()-1]
    # p2 = "abcdefgh"[tf.argmax(predLetters[index+2]).numpy()-1]
    p2 = "12345678"[tf.argmax(predDigits[index+2]).numpy()-1]
    p3 = "12345678"[tf.argmax(predDigits[index+3]).numpy()-1]
    är = f"{p0}{p1}{p2}{p3}"

    # if är[1] != facit[i][1]: print(i,är,facit[i])
    # if är[3] != facit[i][3]: print(i,är,facit[i])

    for d in range(4):
        # if max(predictions[index + d]) < 0.75:
        #     print(i,p,facit[i],'shaky!', " ".join([str(round(p,3)) for p in predictions[index+d]]))

        if är[d] != facit[i][d]:
            # pred = predLetters if d % 2 == 0 else predDigits
            pred = predDigits
            print(i,är,facit[i],'fel!', " ".join([str(round(p,3)) for p in pred[index+d]]))

    # print(index,predicted_label)
    # true_label = tf.argmax(y_test[index]).numpy()
    # print(f'Predicted label: {predicted_label}, True label: {true_label}')
    # if predicted_label != true_label:
    #     antal += 1 # print('problem',index)
# print(antal)
# print((time.time_ns() - start)/10**6)