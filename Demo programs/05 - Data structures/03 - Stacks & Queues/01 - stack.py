from collections import deque

stack = []

stack.append('1. last')
stack.append('2. in')
stack.append('3. last')
stack.append('4. out')

while len(stack) > 0:
    print(stack.pop())

queue = deque()

queue.append('1. first')
queue.append('2. in')
queue.append('3. first')
queue.append('4. out')

queue.appendleft('0. <== yay ==>')

while len(queue):
    print(queue.popleft())