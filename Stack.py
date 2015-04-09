__author__ = 'Roberto'

class myStack:
    def __init__(self):
        pass

    ## pushes item to the top of the stack S
    def push(self,item,S):
        S.append(item)

    ## pops top item from the stack S
    def pop(self,S):
       return S.pop()

    ## checks if stack S is Empty
    def isEmpty(self,S):
        return S == []

    ## returns size of the Stack S
    def size(self,S):
        return len(S)



