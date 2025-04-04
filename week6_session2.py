class Node:
    def __init__(self, value, next=None):
        self.value = value
        self.next = next
    
# For testing
def print_linked_list(head):
    current = head
    while current:
        print(current.value, end=" -> " if current.next else "\n")
        current = current.next

def partition(suspect_ratings, threshold):
	# nodes greater than threshold come first in list
    # rest of nodes come last
    # order does not matter
    

    # iterate through linked list
    head = suspect_ratings
    curr = suspect_ratings
    while curr.next:
        if curr.next.value > threshold:
         # if node.value > threshold, assign it as head
            new_head = curr.next
            curr.next = curr.next.next
            new_head.next = head
            head = new_head
        curr = curr.next
    return head

        

suspect_ratings = Node(1, Node(4, Node(3, Node(2, Node(5, Node(2))))))

print_linked_list(partition(suspect_ratings, 3))
