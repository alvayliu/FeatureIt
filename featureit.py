import pandas as pd
import numpy as np

def aggregate_numerical_features(df, attr):
    """
    This function aggregates the numerical features in a Pandas DataFrame.
    """
    
    # Check which features are being aggregated
    print("The following numerical features will be treated", 
          list(df.select_dtypes('number').columns))

    
    agg_df = df.select_dtypes('number').copy()
    agg_df[attr] = df[attr]
    agg_df = agg_df.groupby(attr).agg(['mean', 'max', 'min', 'median', 'count', 'sum']).reset_index()
    
    column_names = [] 
    for a,b in list(agg_df):
        if a == attr:
            column_names.append(a)
        else:
            column_names.append(a + "_" + b)
    agg_df.columns = column_names
    
    return agg_df



def aggregate_categorical_features(df, attr):
    """
    This function aggregates the categorical features in a Pandas DataFrame
    and returns a count for each category.
    """
    
    # Check which features are being aggregated
    print("The following categorical features will be one-hot-encoded\n", 
          df.select_dtypes('object').apply(pd.Series.nunique, axis = 0))
    print("You are creating", 
          np.sum(list(df.select_dtypes('object').apply(pd.Series.nunique, axis = 0))),
          "new features in total.")
    
    
    agg_df = df.select_dtypes('object').copy()
    agg_df[attr] = df[attr]
    agg_df = pd.get_dummies(agg_df)
    agg_df = agg_df.groupby(attr).agg(['sum']).reset_index()
    
    column_names = [] 
    for a,b in list(agg_df):
        if a == attr:
            column_names.append(a)
        else:
            column_names.append(a + "_" + b)
    agg_df.columns = column_names
    
    return agg_df


def transform_date(df, column_name, drop=False):
    df['year'] = pd.to_datetime(df[column_name]).dt.year
    df['month'] = pd.to_datetime(df[column_name]).dt.month
    df['day'] = pd.to_datetime(df[column_name]).dt.day
    if drop:
        df.drop(columns=[column_name], inplace=True)
    
def transform_time(df, column_name, drop=False):
    df['hour'] = pd.to_datetime(df[column_name]).dt.hour
    df['minute'] = pd.to_datetime(df[column_name]).dt.minute
    df['second'] = pd.to_datetime(df[column_name]).dt.second
    if drop:
        df.drop(columns=[column_name], inplace=True)