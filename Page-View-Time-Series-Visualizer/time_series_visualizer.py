import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
from pandas.plotting import register_matplotlib_converters
register_matplotlib_converters()

# Import data (Make sure to parse dates. Consider setting index column to 'date'.)
df = pd.read_csv('fcc-forum-pageviews.csv', index_col='date', parse_dates=['date'])

# Clean data
df = df.loc[(df['value'] > df['value'].quantile(0.025)) &
                    (df['value'] < df['value'].quantile(0.975)) ]


def draw_line_plot():
    # Draw line plot
    fig, ax = plt.subplots(figsize=(15,5))
    x = df.index
    y = df['value']
    ax.plot(x, y,'r')
    ax.set_xlabel('Date')
    ax.set_ylabel('Page Views')
    ax.set_title('Daily freeCodeCamp Forum Page Views 5/2016-12/2019')

    # Save image and return fig (don't change this part)
    fig.savefig('line_plot.png')
    return fig

def draw_bar_plot():
    # Copy and modify data for monthly bar plot
    df_bar = df.copy()
    df_bar['year'] = df_bar.index.year 
    df_bar['month'] = df_bar.index.month_name()
    
    # Draw bar plot
    fig, ax_2 = plt.subplots(figsize= (10,8))
    working_df = df_bar.groupby(['year', 'month'])['value'].mean()
    working_df = working_df.unstack(level='month')
    working_df = working_df[['January', 'February', 'March', 'April', 'May', 'June', 
                            'July', 'August', 'September', 'October', 'November', 'December']]
    working_df.plot.bar(ax=ax_2)
    ax_2.set_xlabel('Years')
    ax_2.set_ylabel('Average Page Views')
    ax_2.legend(title='Months')

    # Save image and return fig (don't change this part)
    fig.savefig('bar_plot.png')
    return fig

def draw_box_plot():
    # Prepare data for box plots (this part is done!)
    df_box = df.copy()
    df_box.reset_index(inplace=True)
    df_box['year'] = [d.year for d in df_box.date]
    df_box['month'] = [d.strftime('%b') for d in df_box.date]

    # Draw box plots (using Seaborn)
    fig, ax_3 = plt.subplots(1,2, figsize= (20,10))
    sns.boxplot(ax=ax_3[0], data=df_box, x='year', y='value')
    ax_3[0].set_xlabel('Year')
    ax_3[0].set_ylabel('Page Views')
    ax_3[0].set_title('Year-wise Box Plot (Trend)')
    sns.boxplot(ax=ax_3[1], data=df_box, x='month', y='value', 
                        order=['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec'])
    ax_3[1].set_xlabel('Month')
    ax_3[1].set_ylabel('Page Views')
    ax_3[1].set_title('Month-wise Box Plot (Seasonality)')

    # Save image and return fig (don't change this part)
    fig.savefig('box_plot.png')
    return fig
