from pathlib import Path
import hashlib

path = Path("E:/tests")
path_glob = path.glob('**/*')
chunk_size = 65536

def hash_all() -> dict[str, str]:
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