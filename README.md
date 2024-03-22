# CatVDog-Prediction-App

This repository implements a deep learning model for distinguishing between cat and dog images. The model is built using Keras' Sequential API. It served as a learning project to explore the fundamentals of building and deploying such models as Flask web applications. I developed this project during my internship at DOST-ASTI.

## Features

- Building a Keras Sequential model for image classification
- Training the model on a dataset of cat and dog images (https://www.kaggle.com/competitions/dogs-vs-cats/data)
- Evaluating model performance
- Deploying the trained model as a Flask application

## How to Use

### Install Locally

- Clone [this repository](https://github.com/Deep-Computer-Vision/image-data-asset-management-tool-deep-computer-vision-team). ([Not sure how?](https://docs.github.com/en/repositories/creating-and-managing-repositories/cloning-a-repository))

- Install [Python](https://www.python.org/downloads/) and [pip](https://pip.pypa.io/en/latest/installation/#installation).

- Run the following command to ensure that Python and pip are installed correctly: ([Not on Path?](https://realpython.com/add-python-to-path/))

  - On Windows
    ```
    python --version && pip --version
    ```
  - On Linux/Unix or MacOS
    ```
    python3 --version && pip --version
    ```
    Versions of installed Python and pip should be displayed.

- On the root directory of the project, run the following command to install necessary [Python packages](https://github.com/CMPE-40062-Azure-Python/CEA-ROOM-INFORMATION-SYSTEM/blob/main/requirements.txt) using pip.

  ```
  pip install -r requirements.txt
  ```
- On the root directory of the project, run the following command to start the project.

  ```
  flask run
  ```

- Enter the following to the address bar of a browser.

  ```
  localhost:5000
  ```
  [&#9650; Back to the Top](#catvdog-prediction-app)
