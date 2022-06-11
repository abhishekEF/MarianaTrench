"""
This is a boilerplate pipeline 'data_science'
generated using Kedro 0.18.1
"""


from kedro.pipeline import Pipeline, node, pipeline

from .nodes import evaluate_model, split_data, train_model, calculate_corescore


def create_pipeline(**kwargs) -> Pipeline:
    return pipeline(
        [
            node(
                func=split_data,
                inputs=["model_input_table", "params:model_options"],
                outputs=["X_train", "X_test", "y_train", "y_test"],
                name="split_data_node",
            ),
            node(
                func=train_model,
                inputs=["X_train", "y_train"],
                outputs="regressor",
                name="train_model_node",
            ),
            node(
                func=evaluate_model,
                inputs=["regressor", "X_test", "y_test"],
                outputs="Weight Matrix",
                name="Learn-Weights-From-Regression-Analysis",
            ),
            node(
                func=calculate_corescore,
                inputs=["Weight Matrix", "model_input_table", "closest_gas-stations"],
                outputs="Ranked CoReScore by Gas Station",
                name="Calculate-and-Rank-CoReScore-by-Gas-Station",
            ),
        ]
    )