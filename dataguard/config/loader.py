from importlib.resources import files
import yaml

def load_config():
    config_path = files("dataguard.config").joinpath("rules.yaml")
    with config_path.open("r") as f:
        return yaml.safe_load(f)