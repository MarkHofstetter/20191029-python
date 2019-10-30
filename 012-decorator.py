import time

def timing(func_ref):
    def wrapper():        
        t_start = time.time()
        func_ref()
        t_end = time.time()       
        print(t_end - t_start)                
    return wrapper

def info(func_ref):
    def wrapper():
        print("vorher")
        func_ref()
        print("nachher")    
    return wrapper

@timing
@info
def long_function():
    print("start sleeping")
    time.sleep(1)
    print("end sleeping")
    

long_function()    