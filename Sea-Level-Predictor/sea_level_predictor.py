import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import linregress

def draw_plot():
    # Read data from file
    df = pd.read_csv('epa-sea-level.csv')

    # Create scatter plot
    fig, axes = plt.subplots()
    x = df['Year']
    y = df['CSIRO Adjusted Sea Level']
    axes.scatter(x, y, label= 'Sea Level')


    # Create first line of best fit
    slope, intercept, r, p, se = linregress(x, y)
    # fit_x1 = df['Year'].copy()
    # fit_x1 = fit_x1.append(pd.Series([2050]))
    fit_x1 = pd.Series([i for i in range(1880, 2051)]) 
    fit_y1 = slope * fit_x1 + intercept
    axes.plot(fit_x1, fit_y1, label= 'Best Fit',color= 'b')

    # Create second line of best fit
    slope_2, intercept_2, r_2, p_2, se_2 = linregress(
    df['Year'].loc[df['Year'] >= 2000], 
    df['CSIRO Adjusted Sea Level'].loc[df['Year'] >= 2000])
    # fit_x2 = df['Year'][df['Year'] >= 2000].copy()
    # fit_x2 = fit_x2.append(pd.Series([2050]))
    fit_x2 = pd.Series([i for i in range(2000, 2051)])
    fit_y2 = slope_2 * fit_x2 + intercept_2
    axes.plot(fit_x2, fit_y2, label= 'New best fit', color='r')

    # Add labels and title
    plt.ylabel('Sea Level (inches)') 
    plt.xlabel('Year')
    plt.title('Rise in Sea Level')
    plt.legend()

    
    # Save plot and return data for testing (DO NOT MODIFY)
    plt.savefig('sea_level_plot.png')
    return plt.gca()