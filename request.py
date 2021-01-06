import os
import requests

image_path = os.getcwd() + '/sample_image.jpeg'

resp = requests.post("http://localhost:5000/predict",
                     files={"file": open('sample_image.jpeg','rb')})
