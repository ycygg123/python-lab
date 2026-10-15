from __future__ import annotations

def main():
    class Node:
        def __init__(self,value,next:Node | None = None) -> None:
            self.value = value
            self.next_node = next

    class Linked_list:
        def __init__(self) -> None:
            self.head:Node | None = None
            self.size = 0

        def add_new_node(self,value):
            self.head = Node(value,self.head)
            self.size += 1

        def pop_top_node(self):
            if self.head is None:
                raise IndexError("当前链表为空！")
            popped_value = self.head.value
            self.head = self.head.next_node
            self.size -= 1
            print(f"已经删除节点{popped_value},更新当前头节点为：{self.head.value}")

        def show_len(self):
            print(self.size)

        def show_whole_lkls(self):
            print("现在开始打印该链表：\n")
            while self.head.next_node is not None:
                print(self.head.value)

    linklist = Linked_list()
    for i in range(1,11):
        linklist.add_new_node(i)
        linklist.show_len()
    linklist.show_whole_lkls()
    for i in range(5):
        linklist.pop_top_node()
    linklist.show_len()
    linklist.show_whole_lkls()

if __name__ == "__main__":
    main()
