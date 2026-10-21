from app.main import Linked_list


class Stack:
    def __init__(self):
        self._list = Linked_list()

    def push(self, value):
        self._list.add_new_node(value)

    def pop(self):
        if self.is_empty():
            raise IndexError("当前栈为空！")
        return self._list.pop_top_node()

    def __len__(self):
        return len(self._list)

    def is_empty(self):
        return self._list.head is None


if __name__ == "__main__":
    a = Stack()
    a.push(1)
    a.push(2)
    a.push(5)
    a.pop()
    a.pop()
    a.pop()
    print(a.__len__())
    print(a.is_empty())
