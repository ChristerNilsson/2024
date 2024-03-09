import numpy as np
import pandas as pd
import tensorflow as tf
from tensorflow.keras import layers, models
import time

start = time.time_ns()

BASE = 36

# Load EMNIST-byclass dataset from CSV files
train_data = pd.read_csv('emnist-byclass-train.csv', header=None)
#test_data = pd.read_csv('emnist-byclass-test.csv', header=None)
test_data = pd.read_csv('Te2e4.csv', header=None)

# Extract features and labels
x_train = train_data.iloc[:, 1:].values.astype('float32') / 255.0  # Normalize pixel values
y_train = train_data.iloc[:, 0].values  # Convert labels to start from 0

x_test = test_data.iloc[:, 1:].values.astype('float32') / 255.0  # Normalize pixel values
y_test = test_data.iloc[:, 0].values  # Convert labels to start from 0

# Preprocess the data to extract letters 'a' to 'h' (classes 10 to 17 in EMNIST ByClass. )

valid_classes = list(range(BASE,BASE+8))

x_train = x_train[np.isin(y_train, valid_classes)]
y_train = y_train[np.isin(y_train, valid_classes)] - BASE  # Convert labels to start from 0
x_test = x_test[np.isin(y_test, valid_classes)]
y_test = y_test[np.isin(y_test, valid_classes)] - BASE  # Convert labels to start from 0

# Reshape features to 28x28 images
x_train = x_train.reshape(-1, 28, 28, 1)
x_test = x_test.reshape(-1, 28, 28, 1)

# Define the model architecture
model = models.Sequential([
    layers.Conv2D(32, (3, 3), activation='relu', input_shape=(28, 28, 1)),
    layers.MaxPooling2D((2, 2)),
    layers.Conv2D(64, (3, 3), activation='relu'),
    layers.MaxPooling2D((2, 2)),
    layers.Conv2D(64, (3, 3), activation='relu'),
    layers.Flatten(),
    layers.Dense(64, activation='relu'),
    layers.Dense(8, activation='softmax')  # 8 output classes (a to h)
])

# Compile the model
model.compile(optimizer='adam', loss='sparse_categorical_crossentropy', metrics=['accuracy'])

# Train the model
model.fit(x_train, y_train, epochs=5, batch_size=64, validation_data=(x_test, y_test))

# Evaluate the model
test_loss, test_acc = model.evaluate(x_test, y_test)
print(f'Test accuracy: {test_acc}')

# Save the model
model.save('abcdefgh.h5')
model.save('abcdefgh.keras')

print((time.time_ns() - start)/10**6)
