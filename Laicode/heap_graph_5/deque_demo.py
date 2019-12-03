from collections import deque

'''
deque: 
- stacks and queues (double ended queue0 
- thread-save, memory efficient appends and pops from either side of the deque O(1)
'''

queue = deque('Breadth-1st Search')

queue.append('algorithm')
queue.appendleft('hello')

for i in queue:
    print(i)
    
print(f'size: {len(queue)}')
first=queue.popleft()
print(f'first: {first}')


