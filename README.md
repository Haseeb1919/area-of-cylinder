# Cylinder Surface Area Prediction Project

This project aims to predict the surface area of a cylinder based on its radius and height using machine learning models. Follow the steps below to set up and complete the project.

### Project Overview
[GitHub Repository](https://github.com/Haseeb1919/area-of-cylinder)


## Step 1: Generate and Split the Dataset

- Create a dataset with synthetic data points representing cylinders with various radii and heights.
- Split the dataset into a training set and a testing set with an 80/20 ratio.

**Libraries Used**: `pandas`, `numpy`, `sklearn`

**Files**: `DataGenerator.ipynb`


## Step 2: Choose Machine Learning Models

- Select four machine learning models for this project: Random Forest Regressor and K-Nearest Neighbors Regressor from `sklearn`.
- Perform Hyperparameter Tuning to find the best parameters for the models.
- These models are suitable for regression tasks and will be used to predict the surface area of cylinders based on input features.
- **Data Scaling**: Different types of scaling techniques were tried to normalize the data and assess their impact on model performance. The chosen scaling technique for this project is Standard Scaling.


**Libraries Used**: `sklearn`, `pandas`

**Files**: `KNN.ipynb`
**Files**: `RandomForest.ipynb`



## Step 3: Train and Evaluate the Models

- Train the selected machine learning models using the training dataset.
- Adjust model parameters to optimize their fit to the data.
- Evaluate model performance using metrics such as Mean Absolute Error (MAE), Mean Squared Error (MSE), and R-squared (R2) scores.

**Libraries Used**: `sklearn`

**Files**: `KNN.ipynb`
**Files**: `RandomForest.ipynb`


## Step 4: Create an Inference Script

- Develop an inference script that allows users to interact with the trained models.
- Users can input the radius and height of a cylinder, and the script will load the trained model to predict the cylinder's surface area based on the provided input.

**Libraries Used**: `sklearn`, `joblib` (for model serialization)

**Files**: `inference_KNN.py`
**Files**: `inference_RF.py`

## How to Install Required Libraries

To install the required libraries for this project, you can create a `requirements.txt` file with the following content:


To install required libraries, run the following command in your terminal:
        
        pip install -r requirements.txt



```plaintext
# requirements.txt

#Python version
python==3.11.3

# Libraries for data manipulation and analysis
pandas==1.3.3
numpy==1.19.5

# Machine learning libraries
scikit-learn==0.24.2

# Model serialization
joblib==1.1.0

