import numpy as np
import pandas as pd
import tensorflow as tf
from tensorflow.keras import layers, models

# Load EMNIST dataset from CSV files
train_data = pd.read_csv('emnist-letters-train.csv', header=None)
test_data = pd.read_csv('emnist-letters-test.csv', header=None)

# Extract features and labels
x_train = train_data.iloc[:, 1:].values.astype('float32') / 255.0  # Normalize pixel values
y_train = train_data.iloc[:, 0].values - 1  # Convert labels to start from 0

x_test = test_data.iloc[:, 1:].values.astype('float32') / 255.0  # Normalize pixel values
y_test = test_data.iloc[:, 0].values - 1  # Convert labels to start from 0

# Preprocess the data to extract letters 'a' to 'h' (classes 10 to 17 in EMNIST) ???

#valid_classes = list(range(10, 18))
valid_classes = list(range(0,8))

x_train = x_train[np.isin(y_train, valid_classes)]
y_train = y_train[np.isin(y_train, valid_classes)] # - 10  # Convert labels to start from 0
x_test = x_test[np.isin(y_test, valid_classes)]
y_test = y_test[np.isin(y_test, valid_classes)] # - 10  # Convert labels to start from 0

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
model.save('letters.h5')
