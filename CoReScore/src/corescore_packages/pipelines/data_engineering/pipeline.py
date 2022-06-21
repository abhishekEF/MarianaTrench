"""
This is a boilerplate pipeline 'data_engineering'
generated using Kedro 0.18.1
"""

from kedro.pipeline import Pipeline, node, pipeline

from .nodes import preprocess_demographics, preprocess_wind, create_model_input_table
def create_pipeline(**kwargs) -> Pipeline: 
    return pipeline(
        [
           
            node(
                func = preprocess_demographics,
                inputs = "MinnesotaDemographics",
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
                func=create_model_input_table,
                inputs=["cleaned_demographics", "cleaned_wind-power"],
                outputs="model_input_table",
                name="Aggregate-Data",
),
    
        ]
    )