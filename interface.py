from crypt import methods
from flask import Flask,jsonify,render_template,request
from Diabetes.utils import DiabetesPrediction
import config


app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predicted_diabetes',methods=['GET','POST'])
def get_predicted_diabetes():
    user_data = request.form
    Pregnancies = eval(user_data['Pregnancies'])
    Glucose = eval(user_data['Glucose'])
    BloodPressure = eval(user_data['BloodPressure'])
    SkinThickness = eval(user_data['SkinThickness'])
    Insulin = eval(user_data['Insulin'])
    BMI = eval(user_data['BMI'])
    DiabetesPedigreeFunction = eval(user_data['DiabetesPedigreeFunction'])
    Age = eval(user_data['Age'])

    diabetes_obj = DiabetesPrediction(Pregnancies,Glucose,BloodPressure,SkinThickness,Insulin,BMI,DiabetesPedigreeFunction,Age)
    predicted = diabetes_obj.get_prediction()
    return jsonify({"Result":f"Predicted diabetes is : {predicted}"})

if __name__ == "__main__":
    app.run(port=config.POER_NUMBER)