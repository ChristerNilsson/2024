import tensorflow as tf
import tf2onnx
import onnx

# GER BARA SKRÄP!

# Load your TensorFlow/Keras model
model = tf.keras.models.load_model("abcdefgh.h5")

# Convert the model to ONNX format
onnx_model, _ = tf2onnx.convert.from_keras(model)

# Save the ONNX model
onnx.save_model(onnx_model, "abcdefgh.onnx")