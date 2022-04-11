
# importing the necessary dependencies
from flask import Flask, render_template, request,jsonify
from flask_cors import CORS,cross_origin
import pickle

app = Flask(__name__) # initializing a flask app

@app.route('/',methods=['GET'])  # route to display the home page
@cross_origin()
def homePage():
    return render_template("index.html")

@app.route('/predict',methods=['POST','GET']) # route to show the predictions in a web UI
@cross_origin()
def index():
    if request.method == 'POST':
        try:
            #  reading the inputs given by the user
            HighBP=float(request.form['HighBP'])
            HighChol = float(request.form['HighChol'])
            CholCheck = float(request.form['CholCheck'])
            BMI = float(request.form['BMI'])
            Smoker = float(request.form['Smoker'])
            Stroke = float(request.form['Stroke'])
            HeartDiseaseorAttack = float(request.form['HeartDiseaseorAttack'])
            PhysActivity = float(request.form['PhysActivity'])
            Fruits = float(request.form['Fruits'])
            Veggies = float(request.form['Veggies'])
            HvyAlcoholConsump = float(request.form['HvyAlcoholConsump'])
            AnyHealthcare = float(request.form['AnyHealthcare'])
            NoDocbcCost = float(request.form['NoDocbcCost'])
            GenHlth = float(request.form['GenHlth'])
            
            filename = 'finalized_model.pickle'
            loaded_model = pickle.load(open(filename, 'rb')) # loading the model file from the storage
            # predictions using the loaded model file
            prediction=loaded_model.predict([[HighBP,HighChol,CholCheck,BMI,Smoker,Stroke,HeartDiseaseorAttack,PhysActivity,Fruits,Veggies,HvyAlcoholConsump,AnyHealthcare,NoDocbcCost,GenHlth]])
            print('prediction is', prediction)
            # showing the prediction results in a UI
            return render_template('results.html',prediction=round(10*prediction[0]))
        except Exception as e:
            print('The Exception message is: ',e)
            return 'something is wrong'
    # return render_template('results.html')
    else:
        return render_template('index.html')



if __name__ == "__main__":
    #app.run(host='127.0.0.1', port=8001, debug=True)
	app.run(debug=True) # running the app