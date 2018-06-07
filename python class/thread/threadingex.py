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
        threadLock.acquire()
        print_time(self.name, self.counter, 3)
        print "Exiting " + self.name
        threadLock.release()

def print_time(threadName, delay, counter):
    while counter:
        time.sleep(delay)
        print "%s %s" %  ( threadName, time.ctime(time.time()) )
        counter-=1



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