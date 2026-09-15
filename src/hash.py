from pathlib import Path
import hashlib

chunk_size = 65536

def hash_all(path_str: str) -> dict[str, str]:
    path = Path(path_str)
    path_glob = path.glob('**/*')
    data = {}
    files = [x for x in path_glob if x.is_file()]
    for entry in files:
        hash_obj = hashlib.new("sha256")
        with open(entry, "rb") as f:
            while True:
                chunk = f.read(chunk_size)
                if not chunk:
                    break
                hash_obj.update(chunk)
            data[str(entry)] = hash_obj.hexdigest()
    return data