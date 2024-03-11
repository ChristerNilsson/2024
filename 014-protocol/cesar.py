import tensorflow as tf
from tensorflow.keras.models import load_model
import pandas as pd

from keras.models import model_from_json

def predictor(filename,modelname,label="0123456789"):
	data = pd.read_csv(filename, header=None)

	x = data.iloc[:, 1:].values
	y = data.iloc[:, 0].values
	x = x.reshape(-1, 28, 28, 1)
	x = x/255.0

	if modelname.endswith('.h5'):
		model = load_model(modelname)
		print(model.summary())
	elif modelname.endswith('.json'):
		with open(modelname, 'r') as f:
			loaded_model_json = f.read()
			model = model_from_json(loaded_model_json)
			model.load_weights(modelname.replace('.json','.h5'))

	pred = model.predict(x)
	y_p = [tf.argmax(p).numpy() for p in pred]

	ok = 0
	for i in range(len(pred)):
		p0 = label[y_p[i]]
		p1 = label[y[i]]
		if p0 == p1: ok += 1
		else: print(i, p0, p1, [round(item,3) for item in pred[i]])
	print('Accuracy',ok/len(pred),"\n")

LETTERS1 = 'MNIST/emnist-byclass-train-abcdefgh-shaygu.h5'
DIGITS1  = 'MNIST/emnist-byclass-train-0123456789-shaygu.h5'

LETTERS5 = 'MNIST/emnist-byclass-train-abcdefgh-shaygu_5.h5'
DIGITS5  = 'MNIST/emnist-byclass-train-0123456789-shaygu_5.h5'

LETTERS10 = 'MNIST/emnist-byclass-train-abcdefgh-shaygu_10.h5'

LETTERS20 = 'MNIST/emnist-byclass-train-abcdefgh-shaygu_20.h5'
DIGITS20 = 'MNIST/emnist-mnist-train-shaygu_20.h5'

# EPOCHS == 1
#predictor('data/e2e4/letters.csv',LETTERS1,'abcdefgh') # 0.9610
#predictor('data/e2e4/digits.csv', DIGITS1) # acc = 0.9935
#predictor('data/5254/digits.csv',DIGITS1) # acc = 0.9958
#predictor('MNIST/emnist-byclass-test-0123456789.csv',DIGITS1) # acc = 0.9885
#predictor('MNIST/emnist-byclass-test-abcdefgh.csv',LETTERS1) # acc = 0.9773

# EPOCHS == 5
#predictor('data/e2e4/letters.csv',LETTERS5,'abcdefgh') # 1.0000
#predictor('data/e2e4/digits.csv',DIGITS5) # acc = 1.0000
#predictor('data/5254/digits.csv',DIGITS5) # acc = 0.9917
#predictor('MNIST/emnist-byclass-test-0123456789.csv',DIGITS5) # acc = 0.9921
#predictor('MNIST/emnist-byclass-test-abcdefgh.csv',LETTERS5) # acc = 0.9846

# EPOCHS == 10
#predictor('data/e2e4/letters.csv',LETTERS10,'abcdefgh') # 1.0000
#predictor('MNIST/emnist-byclass-test-abcdefgh.csv',LETTERS10) # 0.9905
#predictor('MNIST/emnist-byclass-test-0123456789.csv',DIGITS10) #
#predictor('data/e2e4/digits.csv',DIGITS10) #
#predictor('data/5254/digits.csv',DIGITS10) #

# EPOCHS == 20
predictor('data/e2e4/letters.csv',LETTERS20,'abcdefgh') # 0.9870
#predictor('MNIST/emnist-byclass-test-abcdefgh.csv',LETTERS20,"abcdefgh") # 0.9911
#predictor('MNIST/emnist-byclass-test-0123456789.csv',DIGITS20) # 0.9967
#predictor('data/e2e4/digits.csv',DIGITS20) # 1.0000
#predictor('data/5254/digits.csv',DIGITS20) # 0.9979
