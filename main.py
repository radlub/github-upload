class listNode():
    def __init__(self, val):
        self.val = val
        self.next = None

class linkedList():
    def __init__(self, head):
        self.head = head
    def __str__(self):
        result = ""
        while self.head is not None:
            result += str(self.head.val) + " -> "
            self.head = self.head.next
        return result + "None"


a = listNode(1)
b = listNode(2)
c = listNode(3)

a.next = b
b.next = c

linkedA = linkedList(a)

print(linkedA)

def addTwoNumbers(l1, l2):

    dummyHead = listNode(0)
    resultTail = dummyHead
    carry = 0

    while l1 or l2 or carry:
        val1 = l1.val if l1 else 0
        val2 = l2.val if l2 else 0

        carry, out = divmod(val1 + val2 + carry, 10)

        result

