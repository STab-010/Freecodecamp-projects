import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import linregress

def draw_plot():
    # Read data from file
    df = pd.read_csv('C:/DISEÑO/Analisis de datos/Data/epa-sea-level.csv')
    

    # Create scatter plot

    plt.scatter(df['Year'], df['CSIRO Adjusted Sea Level'])

    # Create first line of best fit
    x = df['Year']
    y = df['CSIRO Adjusted Sea Level']

    # Create second line of best fit
    x_future = pd.Series(range(1880, 2051))
    y_future = linregress(x,y).intercept + linregress(x,y).slope * x_future
    plt.plot(x_future, y_future, color = 'red')

    # Add labels and title
    plt.xlabel('Year')
    plt.ylabel('Sea Level (inches)')
    plt.title('Rise in Sea Level')

    # Save plot and return data for testing (DO NOT MODIFY)
    plt.savefig('sea_level_plot.png')
    return plt.gca()

draw_plot()