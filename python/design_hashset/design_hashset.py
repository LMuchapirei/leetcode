class ListNode:
    def __init__(self,key):
        self.key = key
        self.next = None


class MyHashSet:
    def __init__(self):
        self.set = [ListNode(0) for i in range(10**4)]
        

    def add(self, key: int) -> None:
        cur = self.set[key % len(self.set)]
        # Skip over the dummy node
        while cur.next:
            # if we find a duplicate return immediately
            if cur.next.key == key:
                return
            # go to the next item in the linked list
            cur = cur.next
        # create the new node at the empty slot
        cur.next = ListNode(key)

    def remove(self, key: int) -> None:
        cur = self.set[key % len(self.set)]
        # iterate till we find the node we are looking for 
        while cur.next:
            if cur.next.key == key:
                # skip over to the next node removing reference of the current one
                cur.next = cur.next.next
                return
            cur = cur.next

    def contains(self, key: int) -> bool:
        cur = self.set[key % len(self.set)]
        # replicate the same logic aswell
        while cur.next:
            if cur.next.key == key:
                return True
            cur = cur.next
        return False
        


# Your MyHashSet object will be instantiated and called as such:
# obj = MyHashSet()
# obj.add(key)
# obj.remove(key)
# param_3 = obj.contains(key)