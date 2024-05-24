import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression

def main():
    # Read data from the text file
    file_path = 'data/raw/numbers.txt'
    try:
        with open(file_path, 'r') as file:
            data = np.array([float(line.strip()) for line in file])
    except FileNotFoundError:
        print(f"File not found: {file_path}")
        return
    except ValueError:
        print("Error reading the data from the file. Ensure the file contains only numeric values.")
        return

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
