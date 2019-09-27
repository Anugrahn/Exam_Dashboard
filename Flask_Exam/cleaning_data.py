import pandas as pd 
# import numpy as np 
# import seaborn as sns
def data_mobil():
    df = pd.read_csv('clean.csv')
    return df

def data_ranking():
    df = pd.read_csv('clean.csv')
    list_europe = df[(df['origin']== 'europe')].sort_values(by='horsepower', ascending=False)['name'].head(3).values
    list_usa = df[(df['origin']== 'usa')].sort_values(by='horsepower', ascending=False)['name'].head(3).values
    list_japan = df[(df['origin']== 'japan')].sort_values(by='horsepower', ascending=False)['name'].head(3).values
    data_ranking = pd.DataFrame({
    'usa' : list_usa,
    'japan' : list_japan,
    'europe' : list_europe
    }, index =['Rank 1', 'Rank 2', 'Rank 3'])  
    return data_ranking

def data_ranking2():
    df = pd.read_csv('clean.csv')
    usa = df[(df['origin']== 'usa')].sort_values(by='mpg', ascending=False)['name'].head(3).values
    japan = df[(df['origin']== 'japan')].sort_values(by='mpg', ascending=False)['name'].head(3).values
    europe = df[(df['origin']== 'europe')].sort_values(by='mpg', ascending=False)['name'].head(3).values

    data_ranking2 = pd.DataFrame({
        'usa' : usa,
        'japan' : japan,
        'europe' : europe
    }, index =['Rank 1', 'Rank 2', 'Rank 3'])  
    return data_ranking2  

