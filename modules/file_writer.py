import threading

lock = threading.Lock()

def write_string(string, file_name):
    with lock:
        f = open(file_name,'a')
        f.write(string)
        f.close()
