# -*- coding: cp936 -*-
'''
Python��û��һ���������������б����������ݽṹ��
ֵ�����ҵ��ǣ���Python�д�����ʾ���ݽṹ���������!

'''
## ������һ��Ԫ�صĴ��룬������һ�������еĵ�����Ԫ:
class Element(object):
    def __init__(self, value):
        self.value = value
        self.next = None
######################################################################################
'''
�ڼ���֮ǰ��
��ȷ������������δ���!����ʹ��__init__����ʼ��һ����Ԫ�ء�
Ԫ����һЩ��֮�������ֵ(�������κζ�������һ�����֡�һ���ַ�����һ���ַ��ȵ�)��
��������һ��ָ�������е���һ��Ԫ�صı�����
'''
## ���ڣ������ǽ���һ��LinkedList��:
class LinkedList(object):
    def __init__(self, head=None):
        self.head = head

    def append(self, new_element):
        current = self.head
        if self.head:
            while current.next:
                current = current.next
            current.next = new_element
        else:
            self.head = new_element

    def get_position(self, position):
        """��һ���ض���λ�û�ȡһ��Ԫ�ء�
            �����һ��λ���ǡ�1����
            ���λ�ò����б��У����ء�None����"""
        counter = 1
        current = self.head
        if position < 1:
            return None
        while current and counter <= position:
            if counter == position:
                return current
            current = current.next
            counter += 1
        return None
    
    def insert(self, new_element, position):
        """��ָ��λ�ò���һ���½ڵ㡣
            �����һ��λ���ǡ�1����
            ��3��λ�ò��롣
            �ڶ��͵�����Ԫ�ء�"""
        counter = 1
        current = self.head
        if position > 1:
            while current and counter < position:
                if counter == position - 1:
                    new_element.next = current.next
                    current.next = new_element
                current = current.next
                counter += 1
        elif position == 1:
            new_element.next = self.head
            self.head = new_element
    
    def delete(self, value):
        """ɾ�����и���ֵ�ĵ�һ���ڵ㡣"""
        current = self.head
        previous = None
        while current.value != value and current.next:
            previous = current
            current = current.next
        if current.value == value:
            if previous:
                previous.next = current.next
            else:
                self.head = current.next
######################################################################################
'''��δ���ǳ����ơ������Ǹոս�����һ��LinkedList��
����һ��headԪ�أ������б��еĵ�һ��Ԫ�ء�
������ǽ���һ��û��ͷ���µ�LinkedList������Ĭ��ΪNone��

'''
## ̫����!������ΪLinkedList����һ��������ʹ�������á�
## �÷�������LinkedList��ĩβ����һ����Ԫ�ء�
#    def append(self, new_element):
#        current = self.head
#        if self.head:
#            while current.next:
#                current = current.next
#            current.next = new_element
#        else:
#            self.head = new_element
######################################################################################
'''
ͬ�����ⲿ�ַǳ���Ҫ�����Բ�Ҫ�ִ���ɡ�����������ִ�У�ȷ��һ�ж������塣
���LinkedList�Ѿ���һ��ͷ����ô����ÿ��Ԫ�ص���һ������ֱ���б���ĩβ��
���б���ĩβ����Ϊnew_element�����ߣ����û��head����Ӧ�ý�new_element���������ʲô��������
'''

# Test cases
# Set up some Elements
e1 = Element(1)
e2 = Element(2)
e3 = Element(3)
e4 = Element(4)

# Start setting up a LinkedList
ll = LinkedList(e1)
ll.append(e2)
ll.append(e3)

# Test get_position
# Should print 3
print ll.head.next.next.value
# Should also print 3
print ll.get_position(3).value

# Test insert
ll.insert(e4,3)
# Should print 4 now
print ll.get_position(3).value

# Test delete
ll.delete(1)
# Should print 2 now
print ll.get_position(1).value
# Should print 4 now
print ll.get_position(2).value
# Should print 3 now
print ll.get_position(3).value