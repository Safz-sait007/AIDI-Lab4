# AIDI-Lab4-Fish Weight Prediction Model


# Project Overview

This project is a Machine Learning (ML) web application that predicts the weight of a fish based on its physical measurements. The model is trained using the Fish Market dataset and is deployed using Flask and Heroku.

# Dataset

•	Source: Kaggle - Fish Market Dataset

•	Features:

  o	Species (Categorical)

  o	Length1 (Vertical length)

  o	Length2 (Diagonal length)

  o	Length3 (Cross length)

  o	Height

  o	Width

•	Target Variable: Weight (grams)


# Machine Learning Model

•	Problem Type: Regression (Predicting fish weight)

•	Algorithm Used: Random Forest Regressor

•	Preprocessing Steps:

  o	One-hot encoding for categorical variables (Species)

  o	Standardization of numerical features (Length, Height, Width)

  o	Train-test split (80% training, 20% testing)

•	Evaluation Metrics:

  o	Mean Squared Error (MSE)

  o	R² Score


