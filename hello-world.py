import tensorflow as tf
import os

# Install Tensorflow Commands (Python 3 Needed) (cpu support only):
# pip install --upgrade tensorflow 

# Uninstalling commands.
# pip uninstall tensorflow
# pip uninstall tensorflow-gpu
# Note: tensorflow-gpu did not work when trying to import

# Disables Warning:
# Your CPU supports instructions
#   that this TensorFlow binary was
#   not compiled to use: AVX AVX2
# Stack Overflow on issue:
# https://stackoverflow.com/questions/47068709/your-cpu-supports-instructions-that-this-tensorflow-binary-was-not-compiled-to-u
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '2'

hello = tf.constant("Hello, TensorFlow")
sess = tf.Session()

# '.decode()' used to convert byte string to string.
# if '.decode()' is not added, then output is: b'Hello, TensorFlow'
print(sess.run(hello).decode())
