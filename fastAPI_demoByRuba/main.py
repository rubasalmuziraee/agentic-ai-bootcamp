# Data Handling
import pickle
import numpy as np
from pydantic import BaseModel

# Server
from fastapi import FastAPI

app = FastAPI()

# Initialize files
clf = pickle.load(open('models/iris_model.pickle', 'rb')) # model object
features = pickle.load(open('models/iris_features.pickle', 'rb')) # feature names

class IrisData(BaseModel):
    sepal_length: float
    sepal_width: float
    petal_length: float
    petal_width: float

@app.get('/')
def index():
    return {"message": "Welcome to Iris Classification Application..."}

@app.post("/predict")
def predict(data: IrisData):

    # Extract data in correct order
    data_dict = data.dict()

    to_predict = np.array([data_dict[feature] for feature in features]).reshape(1, -1)
    
    # Create and return prediction
    prediction = clf.predict(to_predict).tolist()
    
    return {"prediction": int(prediction[0])}
