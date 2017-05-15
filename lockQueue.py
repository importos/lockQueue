from multiprocessing import Queue, Lock ,Manager
import uuid

class lockQueue():
    def __init__(self):
        self.q1=Queue()
        self.q2=Queue()
        self.l1=Lock()
        self.d1 = Manager().dict()
        self.l2 = Manager().list()
        self.l3 = Manager().list()
    def put(self,o1):
        self.q1.put(o1)
    def get_for_proccess(self):
        o1=self.q1.get()
        cid=uuid.uuid4()
        self.l1.acquire()
##        print len(self.q1._buffer)
        self.l2.append(cid)
        self.l3.append(False)
        self.l1.release()
        return (cid,o1) 
    def put_proccessed(self,cid,o1):
        self.l1.acquire()
        cc=self.l2.index(cid)
        self.l2[cc]=o1
        self.l3[cc]=True
        while (len(self.l3)>0) and self.l3[0]:
            self.l3.pop(0)
            self.q2.put(self.l2.pop(0))
        self.l1.release()
        
    def get(self):
        return self.q2.get()
