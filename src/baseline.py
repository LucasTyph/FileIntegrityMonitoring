from pathlib import Path
import json

data_dir_path = Path.cwd() / Path("data")
data_json_path = data_dir_path / Path("data.json")

def create_baseline(data: dict[str, str]):
    data_dir_path.mkdir(parents=True, exist_ok=True)
    with open(data_json_path, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=2, sort_keys=True, default=str)

def get_baseline() -> dict[str, str]:
    with open(data_json_path, "r", encoding="utf-8") as f:
        return json.load(f)