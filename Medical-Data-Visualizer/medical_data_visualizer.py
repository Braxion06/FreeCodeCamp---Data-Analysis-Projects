import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np

# Import data
df = pd.read_csv('medical_examination.csv')

# Add 'overweight' column
df['overweight'] = None

# Normalize data by making 0 always good and 1 always bad. If the value of 'cholesterol' or 'gluc' is 1, make the value 0. If the value is more than 1, make the value 1.


# Draw Categorical Plot
def draw_cat_plot():
    # Create DataFrame for cat plot using `pd.melt` using just the values from 'cholesterol', 'gluc', 'smoke', 'alco', 'active', and 'overweight'.
    df_cat = pd.read_csv('medical_examination.csv')
    # Group and reformat the data to split it by 'cardio'. Show the counts of each feature. You will have to rename one of the columns for the catplot to work correctly.
    # Transform centimeters into meters
    df_cat['bmi'] = df_cat['weight'] / ((df_cat['height'] / 100) ** 2 )
    df_cat.loc[df_cat['bmi'] > 25, 'overweight'] = 1
    df_cat.loc[df_cat['bmi'] <= 25, 'overweight'] = 0
    df_cat.loc[df_cat['cholesterol'] == 1, 'cholesterol'] = 0
    df_cat.loc[df_cat['gluc'] == 1, 'gluc'] = 0
    df_cat.loc[df_cat['cholesterol'] > 1, 'cholesterol'] = 1
    df_cat.loc[df_cat['gluc'] > 1, 'gluc'] = 1
    columns = ['cholesterol', 'gluc', 'smoke', 'alco', 'active', 'overweight']
    melted_df_cat = df_cat.melt(id_vars='cardio', value_vars=columns)
    agg_melted_df_cat = melted_df_cat.groupby(
    ['cardio', 'variable']).value_counts().reset_index().rename(columns={0:'total'})



    # Draw the catplot with 'sns.catplot()'
    # Make the catplot
    graph = sns.catplot(data=agg_melted_df_cat, x= 'variable', y='total', col= 'cardio', hue= 'value',  kind= 'bar')


    # Get the figure for the output
    fig = graph.fig


    # Do not modify the next two lines
    fig.savefig('catplot.png')
    return fig


# Draw Heat Map
def draw_heat_map():
    # Clean the data
    df_heat = pd.read_csv('medical_examination.csv')
    df_heat['bmi'] = df_heat['weight'] / ((df_heat['height'] / 100) ** 2 )
    df_heat.loc[df_heat['bmi'] > 25, 'overweight'] = 1
    df_heat.loc[df_heat['bmi'] <= 25, 'overweight'] = 0
    df_heat.loc[df_heat['cholesterol'] == 1, 'cholesterol'] = 0
    df_heat.loc[df_heat['gluc'] == 1, 'gluc'] = 0
    df_heat.loc[df_heat['cholesterol'] > 1, 'cholesterol'] = 1
    df_heat.loc[df_heat['gluc'] > 1, 'gluc'] = 1
    df_heat = df_heat.drop(columns=['bmi'])
    filtered_df_heat = df_heat.loc[
                    (df_heat['ap_lo'] <= df_heat['ap_hi'])  &
                    (df_heat['height'] >= df_heat['height'].quantile(0.025)) &
                    (df_heat['height'] <= df_heat['height'].quantile(0.975)) & 
                    (df_heat['weight'] >= df_heat['weight'].quantile(0.025)) & 
                    (df_heat['weight'] <= df_heat['weight'].quantile(0.975))]
    

    # Calculate the correlation matrix
    corr = filtered_df_heat.corr()

    # Generate a mask for the upper triangle
    mask = np.triu(np.ones_like(filtered_df_heat.corr(), dtype=bool))


    # Set up the matplotlib figure
    fig, ax = plt.subplots()

    # Draw the heatmap with 'sns.heatmap()'
    sns.heatmap(corr, annot=True, mask= mask, fmt= '.1f')


    # Do not modify the next two lines
    fig.savefig('heatmap.png')
    return fig
