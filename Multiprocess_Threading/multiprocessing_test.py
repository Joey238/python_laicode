from multiprocessing import Pool
import time
import random
import os

def long_time_task(name):
    print('run task {1} ({2})...'.format(name, os.getpid()))
    start = time.time()
    time.sleep(random.random()*3)
    end = time.time()
    print('task {} run {}'.format(name,(end-start)))

def main():
    print('Parent process %s.' %(os.getpid()))
    pros = Pool(4)

    for i in range(3):
        pros.apply_async(long_time_task, (i,))
    print('Waiting all subprocess done..')
    pros.close()
    pros.join()
    print('All subprocesses done')

main()

# def f(x):
#     return x*x
#
# if __name__ == '__main__':
#     with Pool(processes=4) as pool:         # start 4 worker processes
#         result = pool.apply_async(f, (10,)) # evaluate "f(10)" asynchronously in a single process
#         print(result.get(timeout=1))        # prints "100" unless your computer is *very* slow
#
#         print(pool.map(f, range(10)))       # prints "[0, 1, 4,..., 81]"
#
#         it = pool.imap(f, range(10))
#         print(next(it))                     # prints "0"
#         print(next(it))                     # prints "1"
#         print(it.next(timeout=1))           # prints "4" unless your computer is *very* slow
#
#         result = pool.apply_async(time.sleep, (10,))
#         print(result.get(timeout=1))
