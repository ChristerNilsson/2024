import tensorflow as tf
from tensorflow.keras.models import load_model
import pandas as pd

def predictor(filename,modelname,label="0123456789"):
	data = pd.read_csv(filename, header=None)
	x = data.iloc[:, 1:].values / 255
	y = data.iloc[:, 0].values
	x = x.reshape(-1, 28, 28, 1)
	model = load_model(modelname)
	print(model.summary())
	pred = model.predict(x)
	y_p = [tf.argmax(p).numpy() for p in pred]

	ok = 0
	for i in range(1000): #len(pred)):
		p0 = label[y_p[i]]
		p1 = label[y[i]]
		if p0 == p1: ok += 1
		else: print(i, p0, p1, [round(item,3) for item in pred[i]])
	print('Accuracy',ok/len(pred),"\n")

# predictor('MNIST/emnist-mnist-test.csv','MNIST/j05t.h5') # Saknar troligen json
#predictor('data/e2e4/letters.csv','letters.h5','abcdefgh')
#predictor('data/e2e4/digits.csv','digits.h5')
predictor('MNIST/emnist-mnist-train.csv','digits.h5')
