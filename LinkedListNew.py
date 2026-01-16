class Node:
    def __init__(self, data):
        self.next = None
        self.data = data


class LinkedList:
    def __init__(self):
        self.head = None
        self.current = None
        self.prev = None
        pass

    def append(self, data):
        new_node = Node(data)
        if self.head == None:
            self.head = new_node
        if self.current != None:
            self.prev = self.current
        self.current = new_node
        if self.prev != None:
            self.prev.next = self.current

    def traverse(self):
        if self.head != None:
            temp = self.head
            while (temp != None):
                print(f"[{temp.data}] =>", end=' ')
                temp = temp.next
            print("Null")
        else:
            print("Empty LL")

    def insert_at(self, index, data):
        new_node = Node(data)
        if self.head != None:
            temp = self.head
            i = 0
            while (i != index - 1):
                temp = temp.next
                i += 1
            next_node = temp.next
            temp.next = new_node
            new_node.next = next_node
        else:
            self.head = new_node

    def delete_at(self, index):
        if self.head == None:
            print("No Elements")
        else:
            temp = self.head
            if (index == 0):
                self.head = temp.next
            i = 0
            while (i != index - 1):
                temp = temp.next
                i += 1
            if (temp.next == None):
                print("No element at given index")
            else:
                if (temp.next.next == None):
                    temp.next = None
                else:
                    temp.next = temp.next.next

    def make_cycle_to(self, index):
        if self.head != None:
            temp = self.head
            tail = None
            i = 0
            while (temp.next != None):
                if (i == index - 1):
                    tail = temp.next
                temp = temp.next
                i += 1
            if (temp.next == None):
                temp.next = tail
                print("Made Cycle")
        else:
            print("No Elements")

    def detect_cycle(self):
        if self.head != None:
            slow = fast = self.head
            is_cycle = False
            while (slow and fast and fast.next):
                slow = slow.next
                fast = fast.next.next
                if (slow == fast):
                    is_cycle = True
                    break
            if (is_cycle):
                print("Cycle detected")
            else:
                print("Cycle not detected")

    def reverse_all(self):
        prev = None
        curr = self.head
        while curr:
            next_node = curr.next
            curr.next = prev
            prev = curr
            curr = next_node
        self.head = prev


ll = LinkedList()
ll.append(5);
ll.append(6);
ll.append(7);
ll.append(8)
ll.traverse()
ll.insert_at(2, 10)
ll.traverse()
ll.delete_at(5)
ll.delete_at(2)
ll.traverse()
# ll.make_cycle_to(2)
ll.detect_cycle()
ll.reverse_all()
ll.traverse()

#  HEAD
#   ||
#  \||/
#   \/
#  [3] => [4] => [5] => null
# Output:
#
# [5] => [6] => [7] => [8] => Null
# [5] => [6] => [10] => [7] => [8] => Null
# No element at given index
# [5] => [6] => [7] => [8] => Null
# Cycle not detected
# [8] => [7] => [6] => [5] => Null