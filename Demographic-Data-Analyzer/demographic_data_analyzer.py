import pandas as pd


def calculate_demographic_data(print_data=True):
    # Read data from file
    df = pd.read_csv('adult.data.csv')

    # How many of each race are represented in this dataset? This should be a Pandas series with race names as the index labels.
    race_count = pd.Series(df['race'].value_counts())

    # What is the average age of men?
    average_age_men = round(df['age'].loc[df['sex'] == 'Male'].mean(),1)

    # What is the percentage of people who have a Bachelor's degree?
    percentage_bachelors = round(df['education'].loc[
        df['education'] == 'Bachelors'].count() / df['education'].count().sum()*100,1)
    # What percentage of people with advanced education (`Bachelors`, `Masters`, or `Doctorate`) make more than 50K?
    # What percentage of people without advanced education make more than 50K?

    # with and without `Bachelors`, `Masters`, or `Doctorate`
    maskhi = df['education'].isin(['Bachelors', 'Doctorate', 'Masters'])
    masklo = ~df['education'].isin(['Bachelors', 'Doctorate', 'Masters'])
    higher_education = df['salary'][maskhi].count()
    lower_education = df['salary'][masklo].count()

    # percentage with salary >50K
    higher_education_rich = round(df['salary'][maskhi].loc[
        df['salary'] == '>50K'].count() / df['salary'][maskhi].count().sum()*100,1) 
    lower_education_rich = round(df['salary'][masklo].loc[
        df['salary'] == '>50K'].count() / df['salary'][masklo].count().sum()*100,1)

    # What is the minimum number of hours a person works per week (hours-per-week feature)?
    min_work_hours = df['hours-per-week'].min()

    # What percentage of the people who work the minimum number of hours per week have a salary of >50K?
    maskminhour = df['hours-per-week'] == df['hours-per-week'].min()
    num_min_workers = df['hours-per-week'][maskminhour].count() 

    rich_percentage = df['salary'][maskminhour].loc[
        df['salary'] == '>50K'].count() / df['salary'][maskminhour].count()*100

    # What country has the highest percentage of people that earn >50K?
    maskrichhi = df.loc[df['salary'] == '>50K'].groupby(['native-country']).count()['age']
    maskgroupall = df.groupby(['native-country']).count()['age']
    earn_rich_percent_country = maskrichhi / maskgroupall
    highest_earning_country = earn_rich_percent_country.idxmax()
    highest_earning_country_percentage = round(earn_rich_percent_country.max()*100,1)

    # Identify the most popular occupation for those who earn >50K in India.
    top_IN_occupation = df.loc[(df['salary'] == '>50K') & 
    (df['native-country'] == 'India')].groupby(['occupation']).count().idxmax()[0]
    # DO NOT MODIFY BELOW THIS LINE

    if print_data:
        print("Number of each race:\n", race_count) 
        print("Average age of men:", average_age_men)
        print(f"Percentage with Bachelors degrees: {percentage_bachelors}%")
        print(f"Percentage with higher education that earn >50K: {higher_education_rich}%")
        print(f"Percentage without higher education that earn >50K: {lower_education_rich}%")
        print(f"Min work time: {min_work_hours} hours/week")
        print(f"Percentage of rich among those who work fewest hours: {rich_percentage}%")
        print("Country with highest percentage of rich:", highest_earning_country)
        print(f"Highest percentage of rich people in country: {highest_earning_country_percentage}%")
        print("Top occupations in India:", top_IN_occupation)

    return {
        'race_count': race_count,
        'average_age_men': average_age_men,
        'percentage_bachelors': percentage_bachelors,
        'higher_education_rich': higher_education_rich,
        'lower_education_rich': lower_education_rich,
        'min_work_hours': min_work_hours,
        'rich_percentage': rich_percentage,
        'highest_earning_country': highest_earning_country,
        'highest_earning_country_percentage':
        highest_earning_country_percentage,
        'top_IN_occupation': top_IN_occupation
    }
