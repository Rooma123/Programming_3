  #basic multiprocessing
import multiprocessing
import time

def squ_num(numbers):
    for n in numbers:
        print( n*n )
        time.sleep(3)

def cub_num(numbers):
    for n in numbers:
        print( n*n*n )
        time.sleep(3)

if __name__ == "__main__":
    arr=[1,2,3]


t=time.time()
p1=multiprocessing.process(target=squ_num,args=(arr,))
p2=multiprocessing.process(target=cub_num,args=(arr,))

p1.start()
p2.start()

p1.join()
p2.join()

print("done")

##################################################################################################################################
#shared data space problem
import multiprocessing

result=[]

def square(numder):
    global result
    for num in numder:
        result.append(num*num)
        print(result)

if __name__ == "__main__":
    list=[1,2,3]

p1=multiprocessing.Process(target=square,args=(list,))
p1.start()
p1.join()

print(result)

##################################################################################################################
#shared data space solution
import multiprocessing 

def square_list(mylist, result, square_sum): 
	for idx, num in enumerate(mylist): 
		result[idx] = num * num 
	square_sum.value = sum(result) 
     
    # print(result)
    # print(square_sum.value)
if __name__ == "__main__":  
	mylist = [1,2,3,4] 
      
	result = multiprocessing.Array('i', 4) 
	square_sum = multiprocessing.Value('i') 

	p1 = multiprocessing.Process(target=square_list, args=(mylist, result, square_sum)) 
     
    # print(result)
    # print(square_sum.value)

	p1.start() 
	p1.join() 
     
#####################################################################################################################3
#communications between processes
import multiprocessing 

def square_list(mylist, q): 
	for num in mylist: 
		q.put(num * num) 

def print_queue(q): 
	print("Queue elements:") 
	while not q.empty(): 
		print(q.get()) 
	print("Queue is now empty!") 

if __name__ == "__main__": 
	mylist = [1,2,3,4] 
	q = multiprocessing.Queue() 

	p1 = multiprocessing.Process(target=square_list, args=(mylist, q)) 
	p2 = multiprocessing.Process(target=print_queue, args=(q,)) 
 
	p1.start() 
	p1.join() 

	p2.start() 
	p2.join() 

#communications between processes pipe example
import multiprocessing 

def sender(conn, msgs): 
	for msg in msgs: 
		conn.send(msg) 
		print(msg) 
	conn.close() 

def receiver(conn): 
	while 1: 
		msg = conn.recv() 
		print(msg) 

if __name__ == "__main__": 
	msgs = ["hello", "hey", "hru?", "END"] 
	parent_conn, child_conn = multiprocessing.Pipe() 

	p1 = multiprocessing.Process(target=sender, args=(parent_conn,msgs)) 
	p2 = multiprocessing.Process(target=receiver, args=(child_conn,)) 

	p1.start() 
	p2.start() 

	p1.join() 
	p2.join() 
