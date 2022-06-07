"""
This is a boilerplate pipeline 'data_engineering'
generated using Kedro 0.18.1
"""

from kedro.pipeline import Pipeline, node, pipeline

from .nodes import preprocess_demographics

def create_pipeline(**kwargs) -> Pipeline: 
    return pipeline(
        [
            node(
                func = preprocess_demographics,
                inputs = "Demographics",
                outputs = "preprocessed_demographics",
                name = "preprocess_demographics_node",
            ),
    
        ]
    )