# 1 ####

# Skapar h5-modeller för letters och digits

# Hanterar både digits och letters (abcdefgh).
# Letters har klasserna 0-7
# Digits har klasserna 0-9
# abcdefgh.csv ska bara innehålla dessa åtta bokstäver.
# 0123456789.csv ska bara innehålla dessa tio siffror.

#KATEGORI = 'MNIST/emnist-byclass-train-abcdefgh'
#KATEGORI = 'MNIST/emnist-byclass-train-0123456789' # 45 min
KATEGORI = 'MNIST/emnist-mnist-train'

EPOCHS = 20

CLASSES = 8 if KATEGORI.endswith('abcdefgh') else 10

import os
import random
import numpy as np
import tensorflow as tf
from tensorflow.python.keras import backend as K
import pandas as pd
from sklearn.model_selection import train_test_split
from tensorflow.python.keras.utils.np_utils import to_categorical
from tensorflow.keras.layers import Input, Dense, Conv2D, Activation, Add, ReLU, MaxPool2D, Flatten, Dropout, BatchNormalization
from tensorflow.keras.models import Model

from tensorflow.keras.preprocessing.image import ImageDataGenerator
from tensorflow.keras.callbacks import ReduceLROnPlateau, ModelCheckpoint
from tensorflow.keras.optimizers.legacy import Adam
from tensorflow.keras.optimizers import RMSprop

# Seed value
# Apparently you may use different seed values at each stage
seed_value = 32

# 1. Set the `PYTHONHASHSEED` environment variable at a fixed value
os.environ['PYTHONHASHSEED'] = str(seed_value)

# 2. Set the `python` built-in pseudo-random generator at a fixed value
random.seed(seed_value)

# 3. Set the `numpy` pseudo-random generator at a fixed value
np.random.seed(seed_value)

# 4. Set the `tensorflow` pseudo-random generator at a fixed value
tf.random.set_seed(seed_value)

# 5. Configure a new global `tensorflow` session
session_conf = tf.compat.v1.ConfigProto(intra_op_parallelism_threads=1, inter_op_parallelism_threads=1)
sess = tf.compat.v1.Session(graph=tf.compat.v1.get_default_graph(), config=session_conf)
K.set_session(sess)

# 2 ###

# 3 ###

# Import Data
train = pd.read_csv(KATEGORI + ".csv", header=None)
# test = pd.read_csv(KATEGORI + ".csv", header=None)
# print("Train size:{}\nTest size:{}".format(train.shape, test.shape))

x_train = train.iloc[:, 1:].values
y_train = train.iloc[:, 0].values
# test = test.iloc[:, 1:].values.astype('float32')

# Transform Train and Test into images\labels.
# x_train = train.drop(['label'], axis=1).values.astype('float32') # all pixel values
# y_train = train['label'].values.astype('int32') # only labels i.e targets digits

### x_test = test # .values.astype('float32')
x_train = x_train.reshape(x_train.shape[0], 28, 28) / 255.0
### x_test = x_test.reshape(x_test.shape[0], 28, 28) / 255.0

x_train, x_val, y_train, y_val = train_test_split(x_train, y_train, test_size=0.02, random_state=32)

print(x_train.shape)
print(x_val.shape)
print(y_train.shape)
### print(x_test.shape)

# 5 ###

x_train = x_train.reshape(x_train.shape[0], 28, 28,1)
x_val = x_val.reshape(x_val.shape[0], 28, 28,1)
### x_test = x_test.reshape(x_test.shape[0], 28, 28,1)
### print("Train size:{}\nvalidation size:{}\nTest size:{}".format(x_train.shape,x_val.shape, x_test.shape))

mean_px = x_train.mean().astype(np.float32)
std_px = x_train.std().astype(np.float32)

# 6 ###

input = Input(shape=[28, 28, 1])
x = Conv2D(64, (5, 5), strides=1, padding='same')(input)
x = Activation('relu')(x)
x = Conv2D(64, (5, 5), strides=1, padding='same')(x)
x = Activation('relu')(x)
x = MaxPool2D(pool_size=2, strides=2, padding='same')(x)
x = Dropout(0.35)(x)

x = Conv2D(128, (3, 3), strides=1, padding='same')(x)
x = Activation('relu')(x)
x = Conv2D(128, (3, 3), strides=1, padding='same')(x)
x = Activation('relu')(x)
x = Conv2D(64, (3, 3), strides=1, padding='same')(x)
x = Activation('relu')(x)

x = MaxPool2D(pool_size=2, strides=2, padding='same')(x)
x = Dropout(0.35)(x)
x = Flatten()(x)
x = Dense(256)(x)
x = Activation('relu')(x)
x = Dense(128)(x)
x = Activation('relu')(x)
x = BatchNormalization()(x)
x = Dense(CLASSES)(x)
x = Activation('softmax')(x)

model = Model(inputs=input, outputs=x)
print(model.summary())

# 7 ###

# optimizer = RMSprop(lr=0.001, rho=0.95, epsilon=1e-08, decay=0.0)
Learning_rate = 0.001
decay = 5 * Learning_rate / EPOCHS
# optimizer = Adam(lr=Learning_rate, decay= 3 * Learning_rate / EPOCHS)
optimizer = RMSprop(learning_rate=Learning_rate, rho=0.9, epsilon=1e-08)
print('compile')
model.compile(optimizer=optimizer, loss='sparse_categorical_crossentropy', metrics=['accuracy'])

#               loss='sparse_categorical_crossentropy',

# Set a learning rate annealer
learning_rate_reduction = ReduceLROnPlateau(monitor='lr', patience=4, verbose=0, factor=0.5, min_lr=0.00001) # val_acc

# Data augmentation
aug_num = 16
print('ImageDataGenerator')
datagen = ImageDataGenerator(
        featurewise_center=False,  # set input mean to 0 over the dataset
        samplewise_center=False,  # set each sample mean to 0
        featurewise_std_normalization=False,  # divide inputs by std of the dataset
        samplewise_std_normalization=False,  # divide each input by its std
        zca_whitening=False,  # apply ZCA whitening
        rotation_range=aug_num,  # randomly rotate images in the range (degrees, 0 to 180)
        zoom_range=aug_num / 100, # Randomly zoom image
        width_shift_range=aug_num / 100,  # randomly shift images horizontally (fraction of total width)
        height_shift_range=aug_num / 100,  # randomly shift images vertically (fraction of total height)
        horizontal_flip=False,  # randomly flip images horizontally
        vertical_flip=False)  # randomly flip images vertically

datagen.fit(x_train)

batch_size = 64
# batch_size = 256

# Max value lr_min = 0.000125
checkpoint = ModelCheckpoint(KATEGORI + str(EPOCHS) + ".h5", monitor='val_acc', verbose=1, save_best_only=False, mode='max')
print('fit')
history = model.fit_generator(datagen.flow(x_train,y_train, batch_size=batch_size), epochs=EPOCHS, validation_data=(x_val,y_val), verbose=1, steps_per_epoch=x_train.shape[0] // batch_size, callbacks=[checkpoint, learning_rate_reduction])

# verbose = 0, steps_per_epoch=x_train.shape[0] // batch_size,callbacks=[checkpoint,learning_rate_reduction])

model.save(KATEGORI + '-shaygu_' + str(EPOCHS) + '.h5')
