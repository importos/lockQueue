from multiprocessing import Process
from lockQueue import lockQueue
import time
import random



def process(queue):
    ## Read from the queue
    while True:
        cid,msg = queue.get_for_proccess()         # Read from the queue and do nothing
##        print 'start wait ',msg
        time.sleep(msg[1]*1.0/10)
##        print 'return',msg
        queue.put_proccessed(cid,(msg[0],'in '+str(msg[1])))
        
def generator(queue):
    index=0
    while True:
        queue.put((index,random.randint(1, 10)))
        time.sleep(0.01)
        index+=1
if __name__=='__main__':
    queue = lockQueue()
    processes=[]
    pp=Process(target=generator, args=(queue,))
    pp.daemon = True
    pp.start()
    processes.append(pp)
    for i in xrange(10):
        pp=Process(target=process, args=(queue,))
        pp.daemon = True
        pp.start()
        processes.append(pp)

    last=-1
    while True:
        msg=queue.get()
        if msg[0]==last+1:
            pass
            print "ok",msg
        else:
            print "Failed",msg
        last=msg[0]
