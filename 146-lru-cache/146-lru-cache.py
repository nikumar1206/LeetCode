class Node:
    def __init__(self, key, val):
        self.key = key
        self.val = val
        self.prev = None
        self.next = None

class DoublyLinkedList:
    def __init__(self):
        self.head = Node(0,0)
        self.tail = Node(0,0) # these values dont matter, we will never need them
        
        self.head.next = self.tail
        self.tail.prev = self.head
        self.length = 0 # increment or decrement the value when adding and subtracting
    def remove(self, node):
        prv = node.prev
        nxt = node.next
        
        
        prv.next = nxt
        nxt.prev = prv

        self.length -= 1
        
    def push(self, node):
        prv = self.tail.prev
        nxt = self.tail
        
        prv.next = node
        nxt.prev = node
        
        node.next = nxt
        node.prev = prv
        
        self.length += 1
        return node
        
class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.hash = {}
        self.DLL = DoublyLinkedList()

    def get(self, key: int) -> int:
        if key not in self.hash:
            return -1
        self.DLL.remove(self.hash[key])
        self.hash[key] = self.DLL.push(self.hash[key])
        return self.hash[key].val
        
    def put(self, key: int, value: int) -> None:
        if key in self.hash:
            self.DLL.remove(self.hash[key])
        newNode = Node(key, value)
        self.hash[key] = self.DLL.push(newNode)
        
        if self.DLL.length > self.capacity:
            lru = self.DLL.head.next
            del self.hash[lru.key] # remove from hash
            self.DLL.remove(lru) #remove from list
