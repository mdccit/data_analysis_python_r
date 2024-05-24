import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression

def main():
    # Example data from the image
    data = np.array([4.33, 2.98, 3.54, 1.35, 1.21, 2.62, 1.57, 1.49, 2.31, 1.51, 1.23, 1.05, 7.63, 
                     1.49, 1.38, 2.32, 1.04, 1.49, 1.04, 1.00, 6.97, 2.22, 2.35, 1.30, 1.29, 1.34])

    # Creating a pandas DataFrame
    df = pd.DataFrame(data, columns=['Value'])
    df['Index'] = range(len(df))

    # Prepare data for model
    X = df['Index'].values.reshape(-1, 1)
    y = df['Value'].values

    # Initialize and fit the model
    model = LinearRegression()
    model.fit(X, y)

    # Predict future values (next 5 indices)
    future_indices = np.array(range(len(df), len(df) + 5)).reshape(-1, 1)
    predictions = model.predict(future_indices)

    # Plotting the results
    plt.figure(figsize=(10, 6))
    plt.plot(df['Index'], df['Value'], label='Observed Values')
    plt.plot(future_indices, predictions, label='Predicted Values', linestyle='--')
    plt.xlabel('Index')
    plt.ylabel('Value')
    plt.title('Observed and Predicted Values')
    plt.legend()
    plt.show()

    # Display predictions
    print("Predicted values for the next 5 indices:", predictions)

if __name__ == "__main__":
    main()