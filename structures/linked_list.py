from __future__ import annotations


class Node:
    def __init__(self, value, next: Node | None = None) -> None:
        self.value = value
        self.next_node = next


class Linked_list:
    def __init__(self) -> None:
        self.head: Node | None = None
        self.size = 0

    def add_new_node(self, value):
        self.head = Node(value, self.head)
        self.size += 1

    def pop_top_node(self):
        if self.head is None:
            raise IndexError("当前链表为空！")
        popped_value = self.head.value
        self.head = self.head.next_node
        self.size -= 1
        return popped_value

    def __len__(self):
        return self.size

    def to_list(self):
        result = []
        temp = self.head
        while temp is not None:
            result.append(temp.value)
            temp = temp.next_node
        return result


def main():
    """main程序仅作生成示例代码用"""
    ll = Linked_list()
    for i in range(1, 11):
        ll.add_new_node(i)
    print(ll.to_list())


if __name__ == "__main__":
    main()
