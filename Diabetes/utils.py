import json
import pickle
import config
import numpy as np

class DiabetesPrediction():
    def __init__(self,Pregnancies,Glucose,BloodPressure,SkinThickness,Insulin,BMI,DiabetesPedigreeFunction,Age):
        self.pregnancies = Pregnancies
        self.glucose     = Glucose
        self.bloodpressure = BloodPressure
        self.skinthickness = SkinThickness
        self.insulin       = Insulin
        self.bmi           = BMI
        self.diabetespedigreefunction = DiabetesPedigreeFunction
        self.age = Age

    def get_model_data(self):
        with open(config.MODEL_FILE_PATH,'rb') as file:
            self.model = pickle.load(file)
        with open(config.JSON_FILE_PATH,'r') as file:
            self.json_data = json.load(file)

    def get_prediction(self):
        self.get_model_data()
        test_array = np.zeros(len(self.json_data['columns']))
        test_array[0] = self.pregnancies
        test_array[1] = self.glucose
        test_array[2] = self.bloodpressure
        test_array[3] = self.skinthickness
        test_array[4] = self.insulin
        test_array[5] = self.bmi
        test_array[6] = self.diabetespedigreefunction
        test_array[7] = self.age
        print("Test Array is : ",test_array)
        Predicted_diabetes = self.model.predict([test_array])
        return Predicted_diabetes