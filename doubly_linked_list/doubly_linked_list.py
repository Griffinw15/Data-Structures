"""
Each ListNode holds a reference to its previous node
as well as its next node in the List.
"""
class ListNode:
    def __init__(self, value, prev=None, next=None):
        self.prev = prev
        self.value = value
        self.next = next
            
"""
Our doubly-linked list class. It holds references to 
the list's head and tail nodes.
"""
class DoublyLinkedList:
    def __init__(self, node=None):
        self.head = node
        self.tail = node
        self.length = 1 if node is not None else 0

    def __len__(self):
        return self.length
    
    """
    Wraps the given value in a ListNode and inserts it 
    as the new head of the list. Don't forget to handle 
    the old head node's previous pointer accordingly.
    """
    def add_to_head(self, value):

        self.length += 1

        listnode = ListNode(value)

        if self.head is None:
            self.head = listnode
            self.head = self.tail
            
        else:
            self.head = listnode.next 
            self.head.prev = listnode
            self.head = listnode

            #self.head = current 
            #self.head = listnode
            #self.head.next = current
            #current.prev = listnode
            
        

    """
    Removes the List's current head node, making the
    current head's next node the new head of the List.
    Returns the value of the removed Node.
    """
    
    def remove_from_head(self):

        self.length -= 1

        current = self.head.value

        if self.head is self.tail:
            self.head = None
            self.tail = None
            return current
        else:
            self.head = self.head.next
            self.head.prev = None
            return current
            
    """
    Wraps the given value in a ListNode and inserts it 
    as the new tail of the list. Don't forget to handle 
    the old tail node's next pointer accordingly.
    """
    def add_to_tail(self, value):

        self.length += 1

        listnode = ListNode(value)

        if self.head is None and self.tail is None:
            self.head = listnode
            self.tail = listnode
        else:
            self.tail.next = listnode
            listnode.prev = self.tail
            self.tail = listnode

            #self.tail = current 
            #self.tail = listnode
            #self.tail.next = current
            #current.prev = listnode
        
            
    """
    Removes the List's current tail node, making the 
    current tail's previous node the new tail of the List.
    Returns the value of the removed Node.
    """
    def remove_from_tail(self):

        self.length -= 1

        current = self.tail.value

        if self.head is None and self.tail is None:
           return None

        self.tail = self.head = None

        return current

            
    """
    Removes the input node from its current spot in the 
    List and inserts it as the new head node of the List.
    """
    def move_to_front(self, node):
        if self.head is None and self.tail is None:
            return None
        elif self.tail is self.head:
            return 
        moved = node
        node.prev = None
        self.head = moved.next 
        self.head = moved
            
        
    """
    Removes the input node from its current spot in the 
    List and inserts it as the new tail node of the List.
    """
    def move_to_end(self, node):
        moved = node
        if moved == self.tail:
            return
        if moved == self.head:
            self.remove_from_head()
            self.add_to_tail(moved.value) 
        else:
            self.delete(moved)
            self.add_to_tail(moved.value)
            #end = None
            #end = self.tail.value
            #self.add_to_tail(end)
            

    """
    Deletes the input node from the List, preserving the 
    order of the other elements of the List.
    """
    def delete(self, node):

        removal = node
        
        if self.head is self.tail:
            self.head = None
            self.tail = None

        elif removal is self.head:
            self.head = removal.next
            self.head.prev = None
            
        elif removal is self.tail:
            self.tail = removal.prev
            self.tail.next = None


        else:
            removal.prev = removal.next
            removal.next = removal.prev

        self.length -= 1
        return removal.value
    """
    Finds and returns the maximum value of all the nodes 
    in the List.
    """
    def get_max(self):
        if not self.head:
            return None
        max = self.head.value
        current = self.head.next
        while current:
            if current.value > max:
                max = current.value
            current = current.next
        return max

