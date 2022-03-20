import os
try:
    os.mkdir("elma")
except FileExistsError:
    print("bu dosya zaten var")
    