'''
Cracking the coding interview
Chapter 2 - Linked List pg 94
Linked List - Return Nth to last 
----------------------------------------
Question: implment an algorithm to find the Nth to last elemend of a singly linked list
Constraits or Questions you need to ask:
N can't be negative, 0 or more than the length of the linked list
Solution notes:
Get the length of the list
length - nth is the index at which in the length you want to return
'''
#Class node
class node:
    def __init__(self,data=None):
        self.data = data
        self.next = None

#Wrapper class
class linked_list:
    def __init__(self):
        self.head = node()

    #Get length of linked list
    def length(self):
            cur = self.head
            total = 0
            while cur.next != None:
                total += 1
                cur = cur.next
            return total

    #print list
    def display(self):
            elements = []
            cur = self.head
            while cur.next != None:
                cur = cur.next
                elements.append(cur.data)
            print(elements)

    #Append data to the end of a linked list
    def append(self,data):
            new_node = node(data)
            current = self.head
            while current.next != None:
                current = current.next
            current.next = new_node

    def returnNthToLast(self, nth):
        #Get length of the list
        listLength = self.length()
        #Check if nth is less than length and more than 0
        if nth > listLength or nth == 0:
            print("Error: 'ReturnNtoLast index out of bounds")
            return None
        #Grab the index by doing length - nth to last 
        index = listLength - nth

        #current index and current node
        curIndex = 0
        curNode = self.head

        #Loop through list to get to index
        while True:
            curNode = curNode.next
            if curIndex == index:
                return curNode.data
            curIndex += 1

    #Method 2
    def print_n_th_from_last(self,n):
        #Get length of the list
        total_length = self.length()

        #Current head varible
        cur = self.head

        #Loop until the end
        while cur:
            if total_length == n - 1:
                print(cur.data)
                return cur
            total_length -= 1
            cur = cur.next
        if cur is None:
            return











myList = linked_list()
#Append data to linked list
myList.append(2)
myList.append(4)
myList.append(5)
myList.append(2)
myList.append(8)
myList.append(7)
#Print list
myList.display()

#Get Nth last from linked list
#print(myList.returnNthToLast(1))
#print(myList.returnNthToLast(2))
#print(myList.returnNthToLast(3))
#print(myList.returnNthToLast(4))
#print(myList.returnNthToLast(5))
#print(myList.returnNthToLast(6))


print(myList.print_n_th_from_last(2))


    