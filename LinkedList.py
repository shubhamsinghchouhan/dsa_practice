class Node:
    def __init__(self, value):
        self.value = value
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def append(self, value):
        node = Node(value)

        if self.head is None:
            self.head = node
            self.tail = node
        else:
            self.tail.next = node
            self.tail = node

        print(f"Appended node:", "Head ->", self.head.value, "Tail ->", self.tail.value)

    def traverse(self):
        current_node = self.head
        print(f"Traversal: [{current_node.value}] ->", end=' ')
        while current_node.next != None:
            current_node = current_node.next
            print(f"[{current_node.value}] ->", end=' ')
        print("[None]")

    def insert(self, index, value):
        current_node = self.head
        insert_node = Node(value)
        i = 0
        while i != index - 1:
            current_node = current_node.next
            i += 1
        if i == index - 1:
            temp = current_node.next
            current_node.next = insert_node
            insert_node.next = temp

    def delete(self, index):
        current_node = self.head
        i = 0
        while i != index - 1:
            current_node = current_node.next
            i += 1

        if i == index - 1:
            current_node.next = current_node.next.next

    def make_cycle(self, index):
        current_node = self.head
        i = 0
        while i != index - 1:
            current_node = current_node.next
            i += 1

        if i == index - 1:
            self.tail.next = current_node.next

    def detect_cycle(self):
        current_node = self.head
        slow = current_node
        fast = current_node
        while fast.next is not None:
            slow = slow.next
            fast = fast.next.next
            if slow == fast:
                print("Cycle detected")
                return

        print("Not a cycle")


ll = LinkedList()
ll.append(2)
ll.append(7)
ll.append(11)
ll.append(20)
ll.traverse()
ll.insert(2, 21)
ll.delete(2)
ll.insert(2, 21)
ll.traverse()
ll.make_cycle(2)
# ll.traverse() # will go in infinite because it's a cycle
ll.detect_cycle()



