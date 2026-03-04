import os
import stat

def prem(fpath):
    filestat = os.stat(fpath)
    prems = stat.filemode(filestat.st_mode)
    return prems

if __name__ == "__main__":
    path = input("Dosya yolunu girin: ")
    if os.path.exists(yol):
        print("İzinler:", prem(path))
    else:
        print("Dosya bulunamadı")
