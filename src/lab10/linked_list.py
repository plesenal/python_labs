class Node:
    def __init__(self, value, next=None):
        self.value = value
        self.next = next


class SinglyLinkedList:
    def __init__(self,data = None):
        self.head = None
        self.tail = None
        self._size = 0
        if data is not None:
            for item in data:

                self.append(item)

    def __len__(self):
        return self._size

    def append(self, value):
        new_node = Node(value)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node
        self._size += 1

    def prepend(self, value):

        new_node = Node(value, next=self.head)
        self.head = new_node
        if self.tail is None:
            self.tail = new_node
        self._size += 1


    def insert(self, idx, value):

        if idx < 0:
            raise IndexError("negative index is not supported")

        if idx == 0:
            self.prepend(value)
            return
        if idx == self._size:
            self.append(value)
            return
        current = self.head

        if idx > self._size:
            raise IndexError("index out of range")
        for _ in range(idx - 1):
            current = current.next

        new_node = Node(value, next=current.next)
        current.next = new_node
        self._size += 1
    def remove_at(self,idx: int):
        if idx < 0 or idx >= self._size:
            raise IndexError("Index out of range")

        if idx == 0:
            value = self.head.value
            self.head = self.head.next
            if self.head is None:
                self.tail = None
            self._size -= 1
            return value
        current = self.head
        for _ in range(idx - 1):
            current = current.next
        re_node = current.next
        value = re_node.value
        current.next = re_node.next
        if idx == self._size - 1:
            self.tail = current
        self._size -= 1
        return value


    def __iter__(self):
        current = self.head
        while current is not None:
            yield current.value
            current = current.next

    def __repr__(self):
        ls = list(self)
        out_str = f"{ls[0]}"
        if len(ls) > 1:
            for i in ls[1:]:
                out_str += f" -> {i}"
        return out_str
        return f"SinglyLinkedList({values})"

def main():
    ll = SinglyLinkedList()
    ll.append('▐')
    ll.append('▟')
    ll.prepend('▖')
    ll.insert(1,'▄')
    print(len(ll))
    print(ll)
    ll.remove_at(0)
    print(ll)
if __name__ == "__main__":
    main()