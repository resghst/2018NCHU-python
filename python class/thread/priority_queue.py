import threading
import time

exitFlag = 0

class myThread(threading.Thread):
    def __init__(self, threadID, name, counter):
        threading.Thread.__init__(self)
        self.threadID = threadID
        self.name = name
        self.counter = counter
    def run(self):
        print "Starting " + self.name
        # threadLock.acquire()
        process_data(self.name, self.q)
        print "Exiting " + self.name
        # threadLock.release()

def process_data(threadName, q):
    while not exitFlag:
        queueLock.acquire()
        if not workQueue.empty():
            data = q.get()
            queueLock.release()
            print "%s %s" %  ( threadName, data )
        else: 


if __name__ == '__main__':
    threadLock = threading.Lock()
    threads = []
    try:
        thread1=myThread(1, 'thread-1', 1)
        thread2=myThread(2, 'thread-2', 2)
        thread1.start()
        thread2.start()
        threads.append(thread1) 
        threads.append(thread1)
        for t in threads:
            t.join()
    except: print "Error: unable to start thread."
    # while 1: pass