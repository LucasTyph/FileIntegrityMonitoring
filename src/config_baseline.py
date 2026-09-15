from pathlib import Path
import json

data_dir_path = Path.cwd() / Path("data")
data_json_path = data_dir_path / Path("data.json")
data_config_path = data_dir_path / Path("config.json")

def create_baseline(data: dict[str, str]):
    data_dir_path.mkdir(parents=True, exist_ok=True)
    with open(data_json_path, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=2, sort_keys=True, default=str)

def get_baseline() -> dict[str, str]:
    with open(data_json_path, "r", encoding="utf-8") as f:
        return json.load(f)


def save_config(directory: str):
    config = {
        "directory": directory
    }
    with open(data_config_path, "w") as f:
        json.dump(config, f, indent=4)

def load_config():
    if not data_config_path.exists():
        return None

    with open(data_config_path, "r") as f:
        config = json.load(f)

    return config.get("directory")