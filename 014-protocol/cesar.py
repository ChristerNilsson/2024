import tensorflow as tf
from tensorflow.keras.models import load_model
import pandas as pd
import numpy as np

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
	#y_p = [1 + tf.argmax(p[1:9]).numpy() for p in pred] # nollor och nior tas bort. I dessa fall gäller näst bästa siffran
	y_p = [tf.argmax(p).numpy() for p in pred]

	ok = 0
	for i in range(len(pred)):
		p0 = label[y_p[i]]
		p1 = label[y[i]]
		if p0 == p1: ok += 1
		else: print(i, p0, p1, [round(item,3) for item in pred[i]])
	print('Accuracy',ok/len(pred),"\n")

#predictor('data/e2e4/digits-transposed.csv','h5/shaygu.h5') # acc = 1.0000

# predictor('data/e2e4/digits-transposed.csv','h5/digits.h5') # acc = 1.0000
#predictor('MNIST/emnist-mnist-test.csv','h5/digits.h5') # 0.9484
#predictor('MNIST/emnist-mnist-train.csv','h5/digits.h5') # acc = 0.9490

#predictor('shaygu_test.csv','h5/shaygu.h5') # saknas label i test.csv
#predictor('shaygu_train.csv','h5/shaygu.h5') # acc = 0.9948
#predictor('MNIST/emnist-mnist-train.csv',  'h5/shaygu.h5') # acc = 0.9946
#predictor('MNIST/emnist-mnist-test.csv',  'h5/shaygu.h5') # acc = 0.9949

