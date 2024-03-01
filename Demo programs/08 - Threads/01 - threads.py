import threading
 
def print_cube(num):
    print(f"Cube: {num * num * num}\n")
 
def print_square(num):
    print(f"Square: {num * num}\n")
 
if __name__ =="__main__":
    t1 = threading.Thread(target=print_square, args=(10,))
    t2 = threading.Thread(target=print_cube, args=(10,))
 
    t1.start()
    t2.start()
 
    t1.join()
    t2.join()
 
    print("Done!")