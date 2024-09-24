from dataclasses import dataclass

@dataclass
class DataIngestionArtifact:
    data_file_path: str




@dataclass
class DataValidationArtifact:
    validation_status: bool




@dataclass
class ModelTrainerArtifact:
    trained_model_file_path: str

