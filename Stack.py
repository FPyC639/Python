from typing import *


class Stack:
    """
    The generic stack class is a data structure that has many versatitle applications.
    """
    def __init__(self):
        super()
        self.__ult_ls = list()
    def push(self, a) -> NoReturn:
        """
        Add item to Stack.
        """
        self.__ult_ls.append(a)
    def pop(self) -> Any:
        """
        Remove and return last item from Stack.
        """
        b = self.__ult_ls.pop()
        return b
    def isEmpty(self) -> bool:
        """
        Is Stack Empty
        """
        return not self.__ult_ls

if __name__ in "__main__":
    a1 = Stack()
    for i in range(4):
        a1.push(i)
    while a1.isEmpty() != True:
        print(a1.pop())