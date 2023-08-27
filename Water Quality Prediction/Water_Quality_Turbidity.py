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

data['Turbidity_Lagged'] = data['Turbidity'].shift(1)  # Lag by one day

# from sklearn.model_selection import train_test_split
X = data['Turbidity_Lagged'].values[1:].reshape(-1, 1)
y = data['Turbidity'].values[1:]

# Load the saved model
from tensorflow.keras.models import load_model

saved_model = load_model('Turbidity_prediction_model.h5')

def predict_turbidity_for_date(user_date, Turbidity_previous_day):
    # Convert the user input date to a pandas datetime object
    user_date = pd.to_datetime(user_date)

    # Get the lagged Turbidity value for the previous day
    lagged_Turbidity = data[data['Date'] == user_date - pd.Timedelta(days=16)]['Turbidity_Lagged'].values[0]

    # Predict Turbidity for the user-specified date
    predicted_Turbidity = saved_model.predict([[lagged_Turbidity]])

    return predicted_Turbidity[0][0]

# Prompt the user to enter a date
User_Date = input("Enter a date in 'YYYY-MM-DD' format: ")

# Check if the user input is valid (you may want to add more validation)
if len(User_Date) == 10 and User_Date[4] == '-' and User_Date[7] == '-':
    print(f'User entered date: {User_Date}')
else:
    print('Invalid date format. Please use "YYYY-MM-DD" format.')
A
#User_Date= '' #Input the Date You Wanted to Predict (This is the User input date from the App)

previous_random_number = None
while True:
    random_number = random.randint(1, 7)
    if random_number != previous_random_number:
        break
user_input_date = '2020-02-01'  # Replace with the user's input date (Forcasting for Next Two Weeks)
user_input_date_parts = user_input_date.split('-')
user_input_date_parts[2] = str(random_number).zfill(2)  # Ensure it's a two-digit day
modified_user_input_date = '-'.join(user_input_date_parts)

previous_day_Turbidity = 10  # Replace with the actual previous day's humidity

predicted_Turbidity = predict_turbidity_for_date(modified_user_input_date, previous_day_Turbidity)
print(f"Predicted Turbidity for {User_Date}: {predicted_Turbidity:.3f}")
