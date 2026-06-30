from flask import Flask, jsonify, request,render_template,redirect,url_for,session
from flask_jwt_extended import JWTManager, jwt_required, create_access_token, get_jwt_identity
import pymongo,config
import datetime,pandas as pd
from src.utils import MedicalInsurance
medical_insurance_obj = MedicalInsurance()

app = Flask(__name__)

app.config["JWT_SECRET_KEY"] = 'secret'
app.config["SECRET_KEY"] = "flask-session-secret"
jwt = JWTManager(app)

mongo_client = pymongo.MongoClient(config.MONGO_URL)
db = mongo_client[config.db_name]
user_collection = db[config.user_collection_name]


@app.route("/")
def home():
    return redirect(url_for("login_page"))

@app.route("/register_page")
def register_page():
    return render_template("register.html")

@app.route("/login_page")
def login_page():
    return render_template("login.html")

@app.route("/forget_password_page")
def forget_password_page():
    return render_template("forget_password.html")

@app.route("/prediction_page")
def prediction_page():
    token = request.args.get("token", "")
    return render_template("prediction.html", token=token)

@app.route("/register", methods = ["POST"])
def register():
    user_data = request.form
    user_name = user_data['user_name']
    password = user_data['password']
    email_id = user_data['email_id']
    contact_number = user_data['contact_number']
    dob = user_data['dob']

    response = user_collection.find_one({"email_id": email_id})
    if not response:
        user_collection.insert_one({
            "user_name": user_name,
            "password": password,
            "email_id": email_id,
            "contact_number": contact_number,
            "dob": dob
            })
        return jsonify({"status": "success", "message":"User Registered Successfully"})
    else:
        return jsonify({"status": "exists", "message": "User Already Exists"})


@app.route("/login",methods = ['POST'])
def login():
    user_data = request.form
    user_name = user_data['user_name']
    password = user_data['password']
    response = user_collection.find_one({"user_name": user_name, "password": password})
    if response:
        access_token = create_access_token(
            identity=user_name,            
            expires_delta=datetime.timedelta(minutes=10))
        return jsonify({"status": "success","message": "Login Successful", 
                        "access_token":access_token})
    else:
        return jsonify({"status": "failure", "message": "Invalid Credentials"})
    

@app.route("/forget_password", methods=["POST"])
def forget_password():
    user_data = request.form
    user_name= user_data['user_name']
    dob = user_data['dob']
    new_password = user_data['new_password']
    response = user_collection.find_one({'user_name':user_name,"dob":dob})
    if response:
        user_collection.update_one({'user_name':user_name,"dob":dob},{"$set":{"password":new_password}})
        return jsonify({"status": "success", "message":"Password Updated Successfully"})
    else:
        return jsonify({"Status":"Failure","Message":"Invalid User Credentials"})


@app.route("/gender_options")
def gender_options():
    """
    this Method is used for showing options in dropdown
    """
    col_data = medical_insurance_obj.load_column_data()
    gender_values = list(col_data['gender'].keys())
    return jsonify(gender_values)


@app.route("/smoker_options")
def smoker_options():
    """
    this Method is used for showing options in dropdown
    """
    col_data = medical_insurance_obj.load_column_data()
    smoker_values = list(col_data['smoker'].keys())
    return jsonify(smoker_values)


@app.route("/region_options")
def region_options():
    """
    this Method is used for showing options in dropdown
    """
    col_data = pd.read_csv(config.INPUT_DATA_PATH)
    region_values = [feature.replace("region_", "") for feature in col_data['colName'] if "region_" in feature]
    return jsonify(region_values)


@app.route("/predict_charges", methods=["POST"])
def predict_charges():
    user_input_data = request.form
   
    prediction = medical_insurance_obj.predict_charges(user_input_data)
    return jsonify({"Predicted Charges": prediction})


if __name__ == "__main__":
    app.run(host=config.FLASK_HOST, port=config.FLASK_PORT, debug=True)