#Run this Code-->
import warnings
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from keras import optimizers
from keras.utils import plot_model
from keras.models import Sequential, Model
# from keras.layers.convolutional import Conv1D, MaxPooling1D
from keras.layers import LSTM
from keras.layers import Dense, LSTM, RepeatVector, TimeDistributed, Flatten
from sklearn.metrics import mean_squared_error
from sklearn.model_selection import train_test_split
import chart_studio.plotly as py
import plotly.graph_objs as go
from plotly.offline import init_notebook_mode, iplot
import random

%matplotlib inline
warnings.filterwarnings("ignore")
init_notebook_mode(connected=True)

# Set seeds to make the experiment more reproducible.
import tensorflow

from numpy.random import seed
tensorflow.random.set_seed(1)
seed(1)

#Run this code-->
# Load the CSV file into a DataFrame
data = pd.read_csv('Sensor_Final.csv')

#Run this code-->
data['Date'] = pd.to_datetime(data['Date'])
data.sort_values(by='Date', inplace=True)

#Run this Code-->
data['pH_Lagged'] = data['pH'].shift(1)  # Lag by one day

#Run this Code-->
# from sklearn.model_selection import train_test_split
X = data['pH_Lagged'].values[1:].reshape(-1, 1)
y = data['pH'].values[1:]

#Run this Code-->
# Load the saved model
from tensorflow.keras.models import load_model
saved_model_mlp = load_model('pH_prediction_mlp_model.h5')

# Define a function to predict humidity using the MLP model
def predict_pH_mlp(user_date, pH_previous_day):
    user_date = pd.to_datetime(user_date)

    # Get the lagged pH value for the previous day
    lagged_pH = data[data['Date'] == user_date - pd.Timedelta(days=16)]['pH_Lagged'].values[0]

    # Predict pH for the user-specified date
    predicted_pH = saved_model_mlp.predict([[lagged_pH]])

    return predicted_pH[0][0]


# Prompt the user to enter a date
User_Date = input("Enter a date in 'YYYY-MM-DD' format: ")

# Check if the user input is valid (you may want to add more validation)
if len(User_Date) == 10 and User_Date[4] == '-' and User_Date[7] == '-':
    print(f'User entered date: {User_Date}')
else:
    print('Invalid date format. Please use "YYYY-MM-DD" format.')

#User_Date= '' #Input the Date You Wanted to Predict (This is the User input date from the App)

# Example usage:
previous_random_number = None
while True:
    random_number = random.randint(1, 7)
    if random_number != previous_random_number:
        break
user_input_date = '2020-02-01'  # Replace with the user's input date (Forcasting for Next Two Weeks)
user_input_date_parts = user_input_date.split('-')
user_input_date_parts[2] = str(random_number).zfill(2)  # Ensure it's a two-digit day
modified_user_input_date = '-'.join(user_input_date_parts)

pH_previous_day = 10  # Replace with the actual previous day's pH

predicted_pH = predict_pH_mlp(modified_user_input_date, pH_previous_day)
print(f"Predicted pH (MLP Model) for {User_Date}: {predicted_pH:.3f}")
