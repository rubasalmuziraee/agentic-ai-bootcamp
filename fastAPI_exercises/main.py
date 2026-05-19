""""
Please complete the rest of this file.
Hints:
1. Load in required files (what files do we need in a ML application?)
2. Define data model or schema of what the API should be receiving (what is the data model used for? Model?)
3. Define the API endpoint (what should the API endpoint path be called?)
4. Define the API endpoint logic (what should logic contain?)
"""

# Data Handling
import pickle
import numpy as np
from pydantic import BaseModel

# Server
from fastapi import FastAPI

app = FastAPI()

# Initialize files
clf = pickle.load(open("models/model.pickle", "rb"))
features = pickle.load(open("models/features.pickle", "rb"))

class Data(BaseModel):
    
    MedInc: float
    HouseAge: float
    AveRooms: float
    AveBedrms: float
    Population: float
    AveOccup: float
    Latitude: float
    Longitude: float
                
@app.post("/predict")
def predict(data: Data):

    "<define prediction logic here>"
    
    input_data = np.array([[getattr(data, f) for f in features]])

    prediction = clf.predict(input_data)

    return {"prediction": prediction.tolist()}