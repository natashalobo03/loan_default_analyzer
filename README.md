Loan Default Analyzer

Overview
The Loan Default Analyzer is a machine learning-based web application that predicts whether a person will repay a loan with interest or default. The project utilizes a Flask web framework to serve the model and provide a user-friendly interface.

Features
- Accepts user input for key financial parameters.
- Predicts loan repayment status using a trained machine learning model.
- Provides a clean and styled user interface.
- Deployed online for easy access.

Technologies Used
- Frontend: HTML, CSS
- Backend: Flask (Python)
- Machine Learning: Scikit-Learn
- Deployment: Render

Installation & Setup

1. Clone the Repository
```bash
git clone https://github.com/natashalobo03/loan_default_analyzer.git
cd loan_default_analyzer
```

2. Create a Virtual Environment
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

3. Install Dependencies
```bash
pip install -r requirements.txt
```

4. Run the Flask Application
```bash
python app.py
```
The application will be available at `http://127.0.0.1:5000/`.

Deployment
The project is deployed using Render. Follow these steps to deploy:
1. Push your code to GitHub.
2. Create a new service on Render (Web Service) and connect your GitHub repository.
3. Specify the build command: `pip install -r requirements.txt`
4. Specify the start command: `python app.py`
5. Deploy and access the live web application.

Usage
1. Open the application in a web browser.
2. Enter details like age, loan amount, income, months employed, and interest rate.
3. Click on 'Predict' to get the result.
4. The model will classify whether the person will repay the loan or default.

Screenshots
![image](https://github.com/user-attachments/assets/002c653c-6f35-41fb-acb2-d2098751cf9d)
![image](https://github.com/user-attachments/assets/89f72bb8-7c70-4d94-afc7-1a5b3504d3ce)



Video Demo
https://drive.google.com/file/d/11dRpa75wE17fY0lU9h667yzELHY9-Ja1/view?usp=sharing

Contributors
Natasha Lobo - Developer

