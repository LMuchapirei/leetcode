# dummy nodes to avoid edge cases and invalid pointer references

class ListNode:
    def __init__(self,key=-1,val=-1,next=None) -> None:
        self.key = key
        self.val = val
        self.next = next

class MyHashMap:
    def __init__(self):
        self.map = [ListNode(0) for i in range(100)]
    def hash(self,key):
        return key % len(self.map)
    def put(self,key:int,value:int)-> None: 
        index = self.hash(key)
        cur = self.map[index]
        while cur.next:
            if cur.next.key == key:
                cur.next.val = value
                return
            cur = cur.next
        cur.next = ListNode(key,value)

    def get(self,key:int)->int:
        index = self.hash(key)
        cur = self.map[index].next
        while cur:
            if cur.key == key:
                return cur.val
        return -1

    def remove(self,key:int)-> None:
        index = self.hash(key)
        cur = self.map[index]
        while cur and cur.next:
            if cur.next.key == key:
                cur.next = cur.next.next
                return 
            cur = cur.next