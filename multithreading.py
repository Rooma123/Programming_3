#wwith out threading
import time

def calc_square(numbers):
    for n in numbers:
        print(n*n )
        time.sleep(0.2) 

def calc_cube(numbers):
    for n in numbers:
        print(n*n*n )
        time.sleep(0.2) 

arr = [2,3,8,9]

t = time.time()

calc_square(arr)
calc_cube(arr)

print("done in : ",time.time()-t)

############################################################################################################
#with threading 

import time
import threading
def calc_square(numbers):
    for n in numbers:
        print(n*n )
        time.sleep(0.2) 

def calc_cube(numbers):
    for n in numbers:
        print(n*n*n )
        time.sleep(0.2) 

arr = [2,3,8,9]

t = time.time()
t1= threading.Thread(target=calc_square, args=(arr,))
t2= threading.Thread(target=calc_cube, args=(arr,))

t1.start()
t2.start()

t1.join()
t2.join()

print("done in : ",time.time()-t)

################################################################################################################
#A thread pool
import concurrent.futures

def worker():
	print("Worker thread running")

pool = concurrent.futures.ThreadPoolExecutor(max_workers=2)

pool.submit(worker) 
pool.submit(worker)

pool.shutdown(wait=True)

print("done")

##Another Example

import time
import concurrent.futures

def calc_square(numbers):
    print("calculate square numbers \n")
    for n in numbers:
        print('square:',n*n , '\n')
        time.sleep(1)
 

def calc_cube(numbers):
    print("calculate cube of numbers \n")
    for n in numbers:
        print('cube:',n*n*n , '\n')
        time.sleep(1)


arr = [2,3,8]

pool = concurrent.futures.ThreadPoolExecutor(max_workers=2)

pool.submit(calc_square , arr) 
pool.submit(calc_cube , arr)

pool.shutdown(wait=True)

print("done")

########################################################################################################
#Race Condition (Problem)

import threading 

# global variable x 
x = 0

def increment(): 
	global x 
	x += 1

def thread_task(): 
	for _ in range(100000): 
		increment() 

def main_task(): 
	global x 
	x = 0

	t1 = threading.Thread(target=thread_task) 
	t2 = threading.Thread(target=thread_task) 
 
	t1.start() 
	t2.start() 

	t1.join() 
	t2.join() 

if __name__ == "__main__": 
	for i in range(10): 
		main_task() 
          
#######################################################################################################
#Race Condition (solution)

import threading 

# global variable x 
x = 0

def increment(): 
	global x 
	x += 1

def thread_task(lock): 
	for _ in range(100000): 
		lock.acquire()
		increment() 
		lock.release()

def main_task(): 
	global x 
	x = 0

	lock = threading.Lock() 

	t1 = threading.Thread(target=thread_task, args=(lock,)) 
	t2 = threading.Thread(target=thread_task, args=(lock,)) 

	t1.start() 
	t2.start() 

	t1.join() 
	t2.join() 

if __name__ == "__main__": 
	for i in range(10): 
		main_task() 
		
#################################################################################
#This example demostrates the use of events to coordinate threads: one thread signals an event while other threads wait for it.
from threading import Thread, Event
from time import sleep

def task(event, id) :
    print(f'\nThread {id} started. Waiting for the signal....')
    event.wait() #Tell thread to wait until thread is set
    print(f'\nReceived signal. The thread {id} was completed.')

def main() :
    event = Event() #reate a new Event object:

    t1 = Thread(target=task, args=(event,1))
    t2 = Thread(target=task, args=(event,2))

    t1.start()
    t2.start()

    print('Blocking the main thread for 3 seconds...')
    sleep(3) 
    event.set() #Set the event



if __name__ == '__main__':
    main()
    