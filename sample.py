import time
def run(params=None):
    string = "Sample python script run!"
    for i in range(10):
        string = string + " iteration"
        time.sleep(6)

    return string
