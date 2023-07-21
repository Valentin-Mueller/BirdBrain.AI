import os
import shutil

import numpy as np
from PIL import Image

from fastapi import FastAPI, File, UploadFile
from fastapi.middleware.cors import CORSMiddleware

import tensorflow as tf

from app.constants import bird_mapping  # pylint: disable=E0401
from app.wikipedia_api import get_bird_information  # pylint: disable=E0401

app = FastAPI()

origins = ['*']

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=['*'],
    allow_headers=['*'],
)

model = tf.keras.models.load_model(os.path.join(os.path.dirname(__file__), './models/bird_brain_model.h5'))

# @app.get('/', response_model=None)
# async def root() -> dict[str, str]:
#     """Basic API root endpoint.

#     Returns:
#         dict[str, str]: JSON with dummy message.
#     """
#     return {'message': 'Hello World'}


@app.get('/test-api/', response_model=None)
async def test_api() -> dict[str, str]:
    """Test API endpoint to test connectivity.

    Returns:
        dict[str, str]: JSON with message confirming connection.
    """
    return {'message': 'API was called and model loaded successfully.'}


@app.post('/classify-bird', response_model=None)
async def classifiy_bird(image: UploadFile = File()) -> dict[str, str | float]:
    """API endpoint to predict the species of a bird shown in an image.

    The image will be resized to 224 x 224.

    Args:
        image (UploadFile, optional): Image showing the bird. Defaults to File().

    Returns:
        dict[str, str | float]: JSON containing species and confidence.
    """
    with open('temp_image.jpg', 'wb') as buffer:
        shutil.copyfileobj(image.file, buffer)

    img = Image.open('temp_image.jpg')

    img = img.resize((224, 224))

    img_np = np.array(img)

    predictions = model.predict(np.expand_dims(img_np, axis=0))

    os.remove('temp_image.jpg')

    predictions = predictions.flatten()

    predicted_class_index = np.argmax(predictions)

    bird_name = bird_mapping[predicted_class_index]

    confidence = predictions[predicted_class_index]

    return {'bird_name': bird_name, 'confidence': float(confidence)}


# @app.post('/{bird_name}/summary/')
# async def bird_summary(bird_name):
#     bird_wiki_summary = bird_summary_wikipedia(bird_name)
#     bird_wiki_summary = str(bird_wiki_summary)
#     return {'message': bird_wiki_summary}

# @app.post('/{bird_name}/page/')
# async def bird_page(bird_name):
#     bird_wiki_page = bird_wikipedia_page(bird_name)
#     bird_wiki_page = str(bird_wiki_page)
#     return {'message': bird_wiki_page}


@app.post('/bird-information', response_model=None)
async def bird_information(bird_name: str, detailed: bool = False) -> dict[str, str]:
    """API endpoint to retrieve information about a species of bird.

    Args:
        bird_name (str): Name of the bird to look up information for.
        detailed (bool, optional): Whether to return the full page or just the summary. Defaults to False.

    Returns:
        dict[str, str]: JSON containing the information.
    """
    bird_info = get_bird_information(bird_name=bird_name, detailed=detailed)

    return {'bird_information': bird_info}
