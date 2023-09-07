
import joblib

def predict():
    try:
        # Loading the model
        best_model = joblib.load('rf_model.joblib')

        # Input for radius and height
        radius_input = float(input("Enter the radius: "))
        height_input = float(input("Enter the height: "))
        
        # Prepare data  
        X_new = [[radius_input, height_input]]

        # Predict
        y_pred = best_model.predict(X_new)

        return y_pred[0]
    except Exception as e:
        return f"An error occurred: {str(e)}"

predicted_value = predict()

if isinstance(predicted_value, (float, int)):
    print(f'Predicted Surface Area: {predicted_value:.2f}')
else:
    print(predicted_value)
