import time

def worker(x,y):
    print('About to work')
    time.sleep(20)
    print('Done')
    return x + y

def do_work(x,y,fut):
    fut.set_result(worker(x,y))