# project

| Field | Details |
|------|---------|
| Title of ML Project | Football Manager AI |
| Name | Bishad |
| Organization | Entri Elevate |
| Date | 25/06/2026 |

## 1. Overview of Problem Statement
Football formation selection is a crucial part of team strategy because it directly affects a team's balance, attacking strength, and defensive stability. However, choosing the most suitable formation is difficult due to the complex relationship between player skills, positions, and tactical decisions. Therefore, developing an effective machine learning model to predict the best formation can help coaches and analysts make more informed decisions and improve team performance.
## 2. objective 
This project is a simple Flask web app that predicts the best football formation based on preprocessed player data and a trained machine learning model.

## 3. Data Description

**Source:**
CSV file containing football player statistics and performance attributes.

**Features:**

* Overall – Overall player rating
* SprintSpeed – Player speed
* Finishing – Goal-scoring ability
* ShortPassing – Passing accuracy
* Dribbling – Ball dribbling skill
* Stamina – Endurance level
* Strength – Physical strength
* BallControl – Ball control ability
* Position – Playing position

**Target Variable:**
**Formation** – The recommended football formation (e.g., 4-3-3, 4-4-2, 3-5-2) predicted by the machine learning model.

## 4. Data Preprocessing & Cleaning

* Missing values were handled using mean imputation.
* Outliers were detected and removed using the IQR method.
* Categorical data were converted into numerical form using Label Encoding.
* Skewed numerical features were transformed using logarithmic transformation.
* Unnecessary columns were removed and the dataset was cleaned before model training.

## 5.oratory Data Analysis (EDA)

* A heatmap was used to analyze correlations between numerical features.
* Strong relationships were identified among player performance attributes.
* It helped in feature selection and improving model performance.

## 6. Feature Engineering

* Categorical features such as player positions were encoded using Label Encoding.
* Relevant player performance attributes were selected as input features.
* New features were created where necessary to improve model performance and prediction accuracy.

## 7. Feature Scaling

* Numerical features were scaled to ensure a uniform range and improve model performance.
*
* MinMaxScaler and RobustScaler were also evaluated for effective feature scaling and handling outliers.

## 8. Model Building

* The dataset was split into training and testing sets.
* Multiple machine learning algorithms such as Decision Tree, Random Forest, SVM, and Logistic Regression were applied.
* The models were trained using the training dataset to predict the best football formation.

## 9. Model Evaluation

* Model performance was evaluated using Accuracy, Precision, Recall, and F1-Score.
* Results from multiple models were compared.
* Random Forest achieved the best performance and was selected as the final model.
## 10. Hyperparameter Tuning

* GridSearchCV was used to optimize the Random Forest model.
* Parameters such as n_estimators, max_depth, min_samples_split, and min_samples_leaf were tuned.
* The best parameter combination was selected to improve prediction accuracy.

## 12. Model Deployment

* The trained Random Forest model was saved using Joblib.
* A Flask web application was developed to provide a user-friendly interface.
* Users can input player and opponent details to receive formation predictions.
* The deployed model was tested using real-world football match scenarios.

## 13. Conclusion

* A machine learning model was developed to predict the best football formation based on player performance attributes.
* Random Forest achieved the best performance among the tested models.
* The model can assist coaches and managers in team selection and tactical decision-making.
* Future improvements include using larger datasets, real-time match statistics, and advanced machine learning techniques.

## 14. References

* FIFA Player Dataset (CSV File)

## Project Files
- app.py: Flask application exposing the prediction endpoint
- preprocessed_data.csv: Preprocessed player dataset used by the model
- best_formation_model.pkl: Trained model file
- requirements.txt: Python dependencies
- Dockerfile: Container setup for running the app
- datapreprocessing.ipynb: Notebook used for data preprocessing

## Requirements
Make sure Python 3.8+ is installed.

Install dependencies:
```bash
pip install -r requirements.txt
```

## Run Locally
Start the Flask app:
```bash
python app.py
```

Then open:
- http://localhost:5000/ for a welcome message
- http://localhost:5000/predict for the formation prediction result

## Run with Docker
Build the image:
```bash
docker build -t football-manager-ai .
```

Run the container:
```bash
docker run -p 5000:5000 football-manager-ai
```

## Notes
The app expects the model file and dataset to be present in the project directory.
