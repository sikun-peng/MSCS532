from assignment6 import *

def test_quickselect():
    assert quickselect([5, 3, 1, 4, 2], 2) == 3

def test_median_of_medians():
    assert median_of_medians([5, 3, 1, 4, 2], 2) == 3

def test_stack():
    s = Stack()
    s.push(1)
    s.push(2)
    assert s.pop() == 2
    assert s.peek() == 1

def test_linked_list():
    l = LinkedList()
    l.insert_front(1)
    l.insert_front(2)
    l.delete(1)
    assert l.head.value == 2
    assert l.head.next is None

if __name__ == "__main__":
    test_quickselect()
    test_median_of_medians()
    test_stack()
    test_linked_list()
    print("All tests passed.")