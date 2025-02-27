from flask import Flask, request, render_template
import numpy as np
import pickle

app = Flask(__name__)

# Load model and scaler correctly
with open("model.pkl", "rb") as f:
    data = pickle.load(f)
    model = data["model"]  # Load the trained model
    scaler = data["scaler"]  # Load the scaler

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/predict", methods=["POST"])
def predict():
    # Get input values from form
    age = float(request.form["age"])
    loan_amount = float(request.form["loan_amount"])
    income = float(request.form["income"])
    months_employed = float(request.form["months_employed"])
    interest_rate = float(request.form["interest_rate"])

    # Preprocess input
    input_data = np.array([[age, loan_amount, income, months_employed, interest_rate]])
    input_data_scaled = scaler.transform(input_data)  # Scale the input

    # Make prediction
    prediction = model.predict(input_data_scaled)[0]

    # Create prediction message
    message = "The person will not repay the loan." if prediction == 0 else "The person will repay the loan with interest."

    return render_template("result.html", message=message)

if __name__ == "__main__":
    app.run(debug=True)
