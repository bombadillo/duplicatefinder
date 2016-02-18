import glob

def retrieve(path):
    if '.txt' in path:
        return [path]
    else:
        return glob.glob(path + '*.txt')
