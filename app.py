from flask import Flask
import pandas as pd
import joblib


app = Flask(__name__)

model = joblib.load("best_formation_model.pkl")

formations = {
    "4-3-3": {"GK": 1, "DEF": 4, "MID": 3, "FWD": 3},
    "4-4-2": {"GK": 1, "DEF": 4, "MID": 4, "FWD": 2},
    "3-5-2": {"GK": 1, "DEF": 3, "MID": 5, "FWD": 2}
}

feature_cols = [
    "Crossing",
    "Finishing",
    "HeadingAccuracy",
    "ShortPassing",
    "Volleys",
    "Dribbling",
    "Curve",
    "FKAccuracy",
    "LongPassing",
    "BallControl",
    "SprintSpeed",
    "Stamina"
]

@app.route("/")
def home():
    return "Football Manager AI is running. Go to /predict"

@app.route("/predict")
def predict():

    temp_df = df.copy()

    temp_df["Predicted_Rating"] = model.predict(
        temp_df[feature_cols]
    )

    formation_scores = {}

    for formation, positions in formations.items():

        team = []

        for pos, count in positions.items():

            selected = (
                temp_df[temp_df["Position"] == pos]
                .sort_values(
                    by="Predicted_Rating",
                    ascending=False
                )
                .head(count)
            )

            team.append(selected)

        final_team = pd.concat(team)

        formation_scores[formation] = (
            final_team["Predicted_Rating"].mean()
        )

    best_formation = max(
        formation_scores,
        key=formation_scores.get
    )

    return {
        "best_formation": best_formation,
        "score": round(
            formation_scores[best_formation],
            2
        )
    }

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)