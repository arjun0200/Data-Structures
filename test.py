from linkedlist import Linkedlist, Node

def nthtolast(ll, n):
    pointer1 = ll.head
    pointer2 = ll.head

    for i in range(n):
        if pointer2 is None:
            return None
        pointer2 = pointer2.next
    while pointer2:
        pointer1 = pointer1.next
        pointer2 = pointer2.next
    return pointer1

def partion(ll, x):
    currNode = ll.head
    ll.tail = ll.head

    while currNode:
        nextNode = currNode.next
        currNode.next = None
        if currNode.value < x:
            currNode.next = ll.head
            ll.head = currNode
        else:
            ll.tail.next = currNode
            ll.tail = currNode
        currNode = nextNode

    if ll.tail.next is not None:
        ll.tail.next = None


def sumlist(llA, llB):
    n1 = llA.head
    n2 = llB.head
    carry = 0
    ll = Linkedlist()
    while n1 or n2:
        result = carry
        if n1:
            result += n1.value
            n1 = n1.next
        if n2:
            result += n2.value
            n2 = n2.next
        ll.add(int(result % 10))
        carry = result / 10

    return ll




# llA = Linkedlist()
# llB = Linkedlist()
# llA.generate(3, 0, 9)
# llB.generate(3, 0, 9)
# print(llA)
# print(llB)
# #print(nthtolast(customll, 4))
# # print(partion(customll, 30))
# # print(customll)
# print(sumlist(llA, llB))

def intersection(llA, llB):
    if llA.tail is not llB.tail:
        return False
    
    lenA = len(llA)
    lenB = len(llB)

    shorter = llA if lenA < lenB else llB
    longer = llB if lenA < lenB else llA

    diff = len(longer) - len(shorter)
    longerNode = longer.head
    shorterNode = shorter.head

    for i in range(diff):
        longerNode = longerNode.next
    
    while shorterNode is not longerNode:
        shorterNode = shorterNode.next
        longerNode = longerNode.next
    
    return longerNode


# Helper addition method
def addSameNode(llA, llB, value):
    tempNode = Node(value)
    llA.tail.next = tempNode
    llA.tail = tempNode
    llB.tail.next = tempNode
    llB.tail = tempNode

llA = Linkedlist()
llA.generate(3,0, 10)

llB = Linkedlist()
llB.generate(4,0, 10)

addSameNode(llA, llB, 11)
addSameNode(llA, llB, 14)

print(llA)
print(llB)

print(intersection(llA, llB))




    
