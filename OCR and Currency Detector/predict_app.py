import base64
import numpy as np
#import tensorflow as tf
import tensorflow.compat.v1 as tf
import io
from PIL import Image
from tensorflow import keras
from tensorflow.python.keras import backend as K
from tensorflow.python.keras.backend import set_session
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import MaxPooling2D,Conv2D,Flatten,Dense, Dropout 
from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing.image import ImageDataGenerator
from tensorflow.keras.preprocessing.image import img_to_array
from flask import request
from flask import jsonify
from flask import Flask
from gevent.pywsgi import WSGIServer
import flask

tf.disable_v2_behavior()
#tf.compat.v1.enable_eager_execution()
# K.clear_session()
app = Flask(__name__)

def get_model():
    global model
    model = load_model('models/model7.h5')
    model._make_predict_function()
    print(" * Model loaded!")
    
def preprocess_image(image, target_size):
    if image.mode != "RGB":
        image = image.convert("RGB")
    image = image.resize(target_size)
    image = img_to_array(image)
    image = np.expand_dims(image, axis=0)
    
    return image

print(" * Loading Keras model...")
#init_g = tf.compat.v1.global_variables_initializer()
#get_model()
# global sess
# sess = tf.compat.v1.Session()
global graph
# set_session(sess)
graph = tf.get_default_graph()
# graph = tf.Graph()
# with graph.as_default():
get_model()
#tf.compat.v1.global_variables_initializer
#tf.initialize_all_variables().run()
#tf.global_variables_initializer().run()
#tf.compat.v1.global_variables_initializer().run()

@app.route("/predict", methods=["GET","POST"])
def predict():
    message = request.get_json(force=True)
    encoded = message['image']
    decoded = base64.b64decode(encoded)
    image = Image.open(io.BytesIO(decoded))
    preprocessed_image = preprocess_image(image, target_size=(256, 256))
    
    #tf.reset_default_graph()
    #with tf.get_default_graph().as_default():
    with graph.as_default():
        init_g = tf.global_variables_initializer()
        init_l = tf.local_variables_initializer()
        with tf.Session() as sess:
            sess.run(init_g)
            sess.run(init_l)
            prediction = model.predict(preprocessed_image).tolist()
            print(prediction)
            
    response = {
    'prediction': {
        'hundred' : prediction[0][0],
        'fivehundred' : 1- prediction[0][0]
        }
    }
    return jsonify(response)
    
#     params = flask.request.json
#     if(params == None):
#         params = flask.request.args
#     if(params!= None):
#         with graph.as_default():
#             #tf.compat.v1.keras.backend.set_session(sess)
#             set_session(sess)
#             prediction = model.predict(preprocessed_image).tolist()

#         response = {
#             'prediction': {
#                 'hundred' : prediction[0][0],
#                 'fivehundred' : prediction[0][1]
#             }
#         }
#     return jsonify(response)

#if __name__ == "__main__":
#    app.run(debug=True)
app.run(host='0.0.0.0')





# @app.route("/predict", methods=["GET","POST"])
# def predict():
#     message = request.get_json(force=True)
#     encoded = message['image']
#     decoded = base64.b64decode(encoded)
#     image = Image.open(io.BytesIO(decoded))
#     preprocessed_image = preprocess_image(image, target_size=(256, 256))
    
#     tf.compat.v1.reset_default_graph()
#     with tf.Graph().as_default():
#         init_g = tf.compat.v1.global_variables_initializer()
#         init_l = tf.compat.v1.local_variables_initializer()
#         with tf.compat.v1.Session() as sess:
#             sess.run(init_g)
#             sess.run(init_l)
#             prediction = model.predict(preprocessed_image).tolist()
            
#     response = {
#     'prediction': {
#         'hundred' : prediction[0],
#         'fivehundred' : prediction[1]
#         }
#     }
#     return jsonify(response)