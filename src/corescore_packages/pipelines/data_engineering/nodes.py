"""
This is a boilerplate pipeline 'data_engineering'
generated using Kedro 0.18.1
"""
import pandas as pd

def preprocess_evreg(EVRegistrationMN: pd.DataFrame) -> pd.DataFrame:
   """Preprocesses data for Minnesota EV Registration
    Args:
      EV Registration Data for Minnesota
    Returns:
      Preprocessed data for EV Registration
   """
   return EVRegistrationMN

def preprocess_utilityDER(MNUtilityDER: pd.DataFrame) -> pd.DataFrame:
   """Preprocesses data for Minnesota Utility DERs
    Args:
     Utility DER Data for Minnesota
    Returns: 
     Preprocessed data for Minnesota Utility DERs
   """
   return MNUtilityDER
def preprocess_eap(x: pd.DataFrame) -> pd.DataFrame:
   return x
def preprocess_gasstations(x: pd.DataFrame) -> pd.DataFrame:
   return x


def preprocess_outages(x: pd.DataFrame) -> pd.DataFrame:
   return x

def preprocess_wind(Wind: pd.DataFrame) -> pd.DataFrame:
   """Preprocesses data for Wind Power.
    
    Args: 
       Wind Power: Raw data.
    Returns: 
       Preprocessed data with vars:
       t_state -	string -	State where turbine is located.
       t_county -	string -	County where turbine is located.
       p_name - string - Name of the wind power project that the turbine is a part of. Project names are typically provided by the developer; some names are identified via other internet resources, and others are created by the authors to differentiate them from previous projects. Values are that were unknown were assigned a name based on the county where the turbine is located.
       p_year - number (integer) - Year that the turbine became operational and began providing power. Note this may differ from the year that construction began.
       p_tnum - number (integer) - Number of turbines in the wind power project.
       p_cap - number (float) - Cumulative capacity of all turbines in the wind power project in megawatts (MW).
       t_cap - number (integer) - Turbine rated capacity - stated output power at rated wind speed from manufacturer, ACP, and/or internet resources in kilowatts (kW).
       Retrofit - number (integer) - Indicator of whether the turbine has been partially retrofit after initial construction (e.g., rotor and/or nacelle replacement). 0 indicates no known retrofit. 1 indicates yes known retrofit.
       xlong - number (float) - Longitude of the turbine point, in decimal degrees.
       ylat	- number (float) - Latitude of the turbine point, in decimal degrees.
    """
   state_filter = Wind["t_state"] == "MN"
   Wind = Wind.loc[state_filter]
   Wind = Wind[["t_state", "t_county", "p_name", "p_year", "p_tnum", "p_cap", "t_cap", "retrofit", "t_conf_atr", "t_conf_loc", "xlong", "ylat"]]
   return Wind

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

def create_model_input_table(
    Demographics: pd.DataFrame, Wind: pd.DataFrame, ev_reg: pd.DataFrame, utility: pd.DataFrame, liea: pd.DataFrame, outage: pd.DataFrame
) -> pd.DataFrame:
    """Combines all data to create a model input table.

    Args:
        shuttles: Preprocessed data for shuttles.
        companies: Preprocessed data for companies.
        reviews: Raw data for reviews.
    Returns:
        model input table.

    """
    

    return Demographics