
# Cylinder Surface Area Prediction Project

This project aims to predict the surface area of a cylinder based on its radius and height using machine learning models. Follow the steps below to set up and complete the project.

## Step 1: Generate and Split the Dataset

- Create a dataset with synthetic data points representing cylinders with various radii and heights.
- Split the dataset into a training set and a testing set with an 80/20 ratio.

## Step 2: Choose Machine Learning Models

1. Select four machine learning models for this project: Random Forest Regressor and K-Nearest Neighbors Regressor from `sklearn`.
2. I have done some Hyperparameter Tuning to find the best parameters for the models.
3. These models are suitable for regression tasks and will be used to predict the surface area of cylinders based on input features.

## Step 3: Train and Evaluate the Models

1. Train the selected machine learning models using the training dataset.
2. Adjust model parameters to optimize their fit to the data.
3. Evaluate model performance using metrics such as Mean Absolute Error (MAE), Mean Squared Error (MSE), and R-squared (R2) scores.

## Step 4: Create an Inference Script

- Develop an inference script that allows users to interact with the trained models.
- Users can input the radius and height of a cylinder, and the script will load the trained model to predict the cylinder's surface area based on the provided input.
- The inference script for both the Random Forest Regressor and K-Nearest Neighbors Regressor models are saved in the `inference` folder.


