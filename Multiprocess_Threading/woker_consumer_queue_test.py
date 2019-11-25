#! -*- coding: utf-8 -*-

from threading import Thread
from time import sleep, time
from random import randint
from queue import Queue

def writeQ(queue):
    print('producing object for Q')
    queue.put('Writer', 1)
    print('Q.size now', queue.qsize())

def readQ(queue):
    out = queue.get(1)
    print('consumed object from Q...size now', queue.qsize(), out)

def writer(queue,loops):
    #writer()函数只做i只做一件事，就是一次玩队列中放入一个对象
    for i in range(loops):
        writeQ(queue)
        sleep(1)

def reader(queue, loops):
    # reader()函数只做一件事，就是一次从队列中取出对象
    for i in range(loops):
        readQ(queue)
        sleep(2)

##设置有多少threads需要被运行
funcs = [writer, reader]
nfuncs = range(len(funcs))

def main():
    # r = random.SystemRandom()
    nloops = randint(10,20)
    q = Queue(32)
    threads = []

    for i in nfuncs:
        t = Thread(target = funcs[i], args = (q, nloops))
        threads.append(t)

    for i in nfuncs:
        threads[i].start()

    for i in nfuncs:
        threads[i].join()
        # print(threads[i].getResult())

    print('All Done')

main()




# 创建一个Thread的实例，传给它一个函数

# import threading
# from time import sleep, time
#
# loops = [4, 2]
#
# def loop(nloop, nsec):
#     print('start loop %s at: %s' % (nloop, time()))
#     sleep(nsec)
#     print('loop %s done at: %s' % (nloop, time()))
#     # 每个线程都会被分配一个事先已经获得的锁，在 sleep()的时间到了之后就释放 相应的锁以通知主线程，这个线程已经结束了。
#
#
# def main():
#     print('starting at:', time())
#     threads = []
#     nloops = range(len(loops))
#
#     for i in nloops:
#         t = threading.Thread(target=loop, args=(i, loops[i]))
#         threads.append(t)
#
#     for i in nloops:
#         # start threads
#         threads[i].start()
#
#     for i in nloops:
#         # wait for all
#         # join()会等到线程结束，或者在给了 timeout 参数的时候，等到超时为止。
#         # 使用 join()看上去 会比使用一个等待锁释放的无限循环清楚一些(这种锁也被称为"spinlock")
#         threads[i].join()  # threads to finish
#
#     print('all DONE at:', time())
#
# if __name__ == '__main__':
#     main()
