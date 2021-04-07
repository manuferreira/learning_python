# stack implementation using a list

stack = [1,2,3,4]

def top(stack):
    result = isEmpty(stack)
    if not result:
        return stack[len(stack)-1]
    return 'empty stack'

def isEmpty(stack):
    if len(stack) == 0:
        return True
    return False

""" stack.append(25)
print(stack)
stack.pop()
print(stack)
print(top(stack))
print(isEmpty(stack))
print(stack) """