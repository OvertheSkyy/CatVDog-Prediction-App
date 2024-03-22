from flask import Blueprint, render_template
import base64
import numpy as np
import io
from PIL import Image, UnidentifiedImageError
import keras
from keras.models import Sequential
from keras.models import load_model
from keras.preprocessing.image import ImageDataGenerator
from keras.preprocessing.image import img_to_array
from flask import request
from flask import jsonify

views = Blueprint('views', __name__)

def get_model():
    global model
    model = load_model('working_sequential_model.h5')
    print(" * Model loaded!")
    
def preprocess_image(image, target_size):
    if image.mode != "RGB":
        image = image.convert("RGB")
    image = image.resize(target_size)
    image = img_to_array(image)
    image = np.expand_dims(image, axis=0)
    
    return image

print(" * Loading Keras model...")
get_model()

@views.route('/', methods=['GET'])
def index():
    # This block is executed for GET requests
    return render_template('index.html')

@views.route('/predict', methods=['POST'])
def predict():
    try:
        message = request.get_json(force=True)
        print("Received message:", message)  # Add this line for debugging
        encoded = message.get('image')
        print("Received encoded image data:", encoded)  # Add this line for debugging

        if encoded:
            try:
                decoded = base64.b64decode(encoded)
                print("Decoding successful")
            except Exception as decode_error:
                print("Error decoding base64 data:", decode_error)
                # Handle the decoding error, e.g., return an error response
            else:
                print("No image data provided in the request")
                # Handle the case when no image data is provided

            try:
                image = Image.open(io.BytesIO(decoded))
                processed_image = preprocess_image(image, target_size=(224, 224))
                prediction = model.predict(processed_image).tolist()

                response = {
                    'prediction': {
                        'dog': prediction[0][0],
                        'cat': prediction[0][1]
                    }
                }
                return jsonify(response)
            except UnidentifiedImageError:
                error_response = {'error': 'Unidentified image format'}
                return jsonify(error_response), 400  # HTTP 400 Bad Request
        else:
            error_response = {'error': 'Image not provided in the request'}
            return jsonify(error_response), 400  # HTTP 400 Bad Request
    except Exception as e:
        # Handle other exceptions
        error_response = {'error': 'Internal server error'}
        return jsonify(error_response), 500  # HTTP 500 Internal Server Error
