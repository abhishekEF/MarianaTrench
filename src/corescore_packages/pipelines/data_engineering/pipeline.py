"""
This is a boilerplate pipeline 'data_engineering'
generated using Kedro 0.18.1
"""

from kedro.pipeline import Pipeline, node, pipeline

from .nodes import preprocess_demographics, preprocess_wind, create_model_input_table, preprocess_evreg, preprocess_utilityDER, preprocess_eap, preprocess_outages, preprocess_gasstations

def create_pipeline(**kwargs) -> Pipeline: 
    return pipeline(
        [
            node(
                func = preprocess_evreg,
                inputs = "Electric-Vehicle-Registration",
                outputs = "cleaned_Electric-Vehicle-Registration",
                name = "preprocess_Electric-Vehicle-Registration",
            ),
            node(
                func = preprocess_eap,
                inputs = "Low-Income-Energy-Assistance",
                outputs = "cleaned_Low-Income-Energy-Assistance",
                name = "preprocess_Low-Income-Energy-Assistance",
            ),
            node(
                func = preprocess_outages,
                inputs = "Outage-History",
                outputs = "cleaned_Outage-History",
                name = "preprocess_Outage-History",
            ),
            node(
                func = preprocess_utilityDER,
                inputs = "Renewable-Energies",
                outputs = "cleaned_renewable-energies",
                name = "preprocess_renewable-energies",
            ),
            node(
                func = preprocess_demographics,
                inputs = "Demographics",
                outputs = "cleaned_demographics",
                name = "preprocess_demographics",
            ),
            node(
                func = preprocess_wind,
                inputs = "Wind-Power",
                outputs = "cleaned_wind-power",
                name = "preprocess_wind-power",
            ),
            node(
                func = preprocess_gasstations,
                inputs = "Gas-Stations",
                outputs = "closest_gas-stations",
                name = "preprocess_stations",
            ),
            node(
                func=create_model_input_table,
                inputs=["cleaned_demographics", "cleaned_wind-power", "cleaned_Electric-Vehicle-Registration", "cleaned_renewable-energies","cleaned_Low-Income-Energy-Assistance", "cleaned_Outage-History"],
                outputs="model_input_table",
                name="Aggregate-Data",
),
    
        ]
    )