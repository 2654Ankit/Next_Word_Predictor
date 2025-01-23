from dataclasses import dataclass
from pathlib import Path

@dataclass(frozen=True)
class DataIngestionConfig:
    root_dir:Path
    source_URL:str
    local_data_file:Path
    unzip_dir:Path

@dataclass(frozen=True)
class DataTransformationConfig:
    data_file_path:str
    data_file_name:str
    transformed_data_x:str
    transformed_data_y : str

@dataclass(frozen=True)
class ModelTrainerConfig:
    transformed_data_dir : str
    model_dir: str
    model_name: str

@dataclass
class PredictionConfig:
    model_path: str


@dataclass(frozen=True)
class EvaluationConfig:
    path_of_model: Path
    all_params: dict
    # mlfl