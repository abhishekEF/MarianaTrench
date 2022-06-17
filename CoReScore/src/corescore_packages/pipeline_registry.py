"""Project pipelines."""
from typing import Dict

from kedro.pipeline import Pipeline, pipeline
from corescore_packages.pipelines import data_engineering as de, data_science as ds

def register_pipelines() -> Dict[str, Pipeline]:
    """Register the project's pipeline.
    Returns:
    A mapping from a pipeline name to a ``Pipeline`` object.
    """
    data_engineering_pipeline = de.create_pipeline()
    data_science_pipeline = ds.create_pipeline()

    return {
        "__default__": data_engineering_pipeline + data_science_pipeline,
        "de": data_engineering_pipeline,
        "ds": data_science_pipeline,
    }