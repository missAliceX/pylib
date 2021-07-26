import os
from os import path

def append_grpc_import(fpath):
    with open(fpath, "r") as f:
        buf = f.readlines()

    with open(fpath, "w") as f:
        for line in buf:
            if line == "import grpc\n":
                line = line + "from grpc import experimental\n"
            f.write(line)
    print(f"Updated {fpath}.")

for root, dirs, files in os.walk('pylib/proto'):
    for file in files:
        if file.endswith('.py'):
            append_grpc_import(path.join(root, file))

