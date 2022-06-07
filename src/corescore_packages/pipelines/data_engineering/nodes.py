"""
This is a boilerplate pipeline 'data_engineering'
generated using Kedro 0.18.1
"""
import pandas as pd

def preprocess_demographics(Demographics: pd.DataFrame) -> pd.DataFrame:

    """Preprocesses data for Demographics.
    
    Args: 
       Demographics: Raw data.
    Returns: 
       Preprocessed data, with margin of error removed and keeps only demographics of citizens permanently in Census tract (ignores those who moved away, etc)
    """
    Demographics = Demographics.loc[:, ~Demographics.columns.str.endswith('M')]
    Demographics = Demographics[Demographics.columns[~Demographics.columns.str.endswith('M')]]
    Demographics = Demographics.loc[:, ~Demographics.columns.str.startswith('S0701_C02')]
    Demographics = Demographics[Demographics.columns[~Demographics.columns.str.startswith('S0701_C02')]]
    Demographics = Demographics.loc[:, ~Demographics.columns.str.startswith('S0701_C03')]
    Demographics = Demographics[Demographics.columns[~Demographics.columns.str.startswith('S0701_C03')]]
    Demographics = Demographics.loc[:, ~Demographics.columns.str.startswith('S0701_C04')]
    Demographics = Demographics[Demographics.columns[~Demographics.columns.str.startswith('S0701_C04')]]
    Demographics = Demographics.loc[:, ~Demographics.columns.str.startswith('S0701_C05')]
    Demographics = Demographics[Demographics.columns[~Demographics.columns.str.startswith('S0701_C05')]]
    new_header = Demographics.iloc[0] #grab the first row for the header
    Demographics = Demographics[1:] #take the data less the header row
    Demographics.columns = new_header #set the header row as the df header

    return Demographics