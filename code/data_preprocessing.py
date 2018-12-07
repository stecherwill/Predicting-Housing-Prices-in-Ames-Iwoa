import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


def get_missing_values(data, suppress=False):
    '''
    -- parameters --
    data : pandas dataframe
    '''
    df = pd.DataFrame([], columns=['features','num_missing_values'])
    df['features'] = data.columns[data.isna().any()].tolist()
    df['num_missing_values'] = [data[col].isna().sum() \
                                for col in data.columns \
                                if data[col].isna().sum() > 0]
    if not suppress:
        print('Number of features without missing values: {}'.format(len(df['features'])))
    return df


def impute_missing_values(df, method):
    df_numeric = df._get_numeric_data()
    df_null = get_missing_values(df, suppress=True)

    np.random.seed(42)

    for feature in df_null['features']:
        if feature in df_numeric:
            if method == 'mean':
                df[feature].fillna(df[feature].mean(), inplace=True)
            elif method == 'median':
                df[feature].fillna(df[feature].median(), inplace=True)
            elif method == 'random':
                num_bag = df[feature].dropna()
                df[feature] = df[feature].apply(lambda x: np.random.choice(num_bag) if np.isnan(x) else x)

def create_ordinal_data(df_train , df_test):
    df_object = df_train.select_dtypes(include = ['object'])
    df_object_test = df_test.select_dtypes(include = ['object'])
    for col in df_object.columns:
        avg_prices = {}
        category_dict={}
        for i , x in enumerate(df_object[col].unique()):
            avg_prices[i] = x ,df_train['saleprice'][df_object[col]==x].mean()
        sorted_dict = pd.DataFrame(avg_prices).T.sort_values(by = 1)

        for i,x in enumerate(sorted_dict[0]):
            category_dict[x]=i

        df_train[col] = df_object[col].map(category_dict)
        df_test[col] = df_object_test[col].map(category_dict)


def subplot_hist(df, columns):

    n_columns = len(columns)
    ncols = 3
    
    nrows = int(np.ceil(n_columns/ncols))    # Makes sure you have enough rows
    
    fig, ax = plt.subplots(nrows = nrows, 
                           ncols = ncols, 
                           figsize = (ncols * 5, nrows * 5),   # You'll want to specify your figsize
                           sharey = False, 
                           sharex = False)
    
    ax = ax.ravel()                                 # Ravel turns a matrix into a vector, which is easier to iterate
    
    for i, column in enumerate(columns): 
        ax[i].hist(df[column], bins = 25)  
        ax[i].set_title('Distribution of {}'.format(column), fontsize = 15)
        ax[i].set_ylabel("Frequency", fontsize = 15)
        
    # delete extra axes
    if n_columns%ncols != 0:
        for i in range(0, n_columns%ncols-1):
            fig.delaxes(ax.flatten()[n_columns-i])
