import sys
from collections import defaultdict

class MinHeap:
    """
    This class is an implementation for MinHeap in python
    """

    def __init__(self, array= []):
        self.heap_size = len(array)
        self.nodes = array.copy()
        self.hash_node = defaultdict(list)

        if self.heap_size > 0:
            self.build_min_heap()
            self.insert_list_hash(self.nodes)

    def left(self, node_index):
        return 2 * node_index + 1

    def right(self, node_index):
        return 2 * (node_index + 1)

    def parent(self, node_index):
        if node_index != 0:
            return (node_index - 1) // 2
        return 0

    def swap(self, first_index:int, second_index:int):
        self.modify_hash(self.nodes[first_index], first_index, second_index)
        self.modify_hash(self.nodes[second_index], second_index, first_index)
        self.nodes[first_index], self.nodes[second_index] = self.nodes[second_index], self.nodes[first_index]

    def is_leaf(self, node_index) -> bool:
        if node_index >= (self.heap_size // 2):
            return True
        return False

    def get_minimum(self):
        if self.heap_size > -1:
            return self.nodes[0]


    """
    Heapify Functions
    """
    def min_heapify_top_down(self, root_index):
        
        left_index = self.left(root_index)
        right_index = self.right(root_index)
        least = root_index

        # print('node =', root_index , 'value =', self.nodes[root_index])

        if left_index < self.heap_size and self.nodes[left_index] < self.nodes[root_index]:
            # print('left =', left_index , 'value =', self.nodes[left_index])
            least = left_index

        if right_index < self.heap_size and self.nodes[right_index] < self.nodes[least]:
            # print('right =', right_index , 'value =', self.nodes[right_index])
            least = right_index

        if least != root_index:
            self.swap(least, root_index)
            self.min_heapify_top_down(least)


    def min_heapify_bottom_up(self, node_index):

        parent_index = self.parent(node_index)
        if self.nodes[node_index] < self.nodes[parent_index]:
            self.swap(node_index, parent_index)
            self.min_heapify_bottom_up(parent_index)


    def build_min_heap(self):
        for position in range(self.heap_size//2, 0, -1):
            self.min_heapify_top_down(position - 1)


    """
    Mutator Function
    """
    def insert(self, value):
        self.nodes.append(value)
        self.heap_size += 1
        self.hash_node
        self.insert_hash(value, self.heap_size - 1)
        self.min_heapify_bottom_up(self.heap_size - 1)

    def delete_min(self):
        min_value = self.nodes[0]
        self.delete_hash(min_value, 0)
        self.nodes[0] = self.nodes[self.heap_size - 1]
        self.heap_size -= 1
        self.nodes.pop()
        self.min_heapify_top_down(0)

    def modify(self, value, new_value):
        self.delete(value)
        self.insert(new_value)

    def delete(self, value):
        index = self.find_hash(value)
        if index:
            self.delete_hash(value, index)
            self.nodes[index] = self.nodes[self.heap_size - 1]
            self.heap_size -= 1
            self.nodes.pop()
            self.min_heapify_top_down(index)


    """
    HashTable functions
    """
    def hash_key(self, value):
        return int(value) % 11

    def find_hash(self, value):
        hash_list = self.hash_node[self.hash_key(value)]
        for index in hash_list:
            if self.nodes[index] == value:
                return index

    def insert_hash(self, value, index):
        self.hash_node[self.hash_key(value)].append(index)

    def insert_list_hash(self, array):
        for index, value in list(enumerate(array)):
            self.insert_hash(value, index)

    def modify_hash(self, value, index, new_index):
        try:
            exp_list = self.hash_node[self.hash_key(value)]
            hash_index = exp_list.index(index)
            exp_list[hash_index] = new_index

        except ValueError:
            print('this value doesn\'t exist!', file=sys.stderr)

    def delete_hash(self, value, index):
        self.hash_node[self.hash_key(value)].remove(index)
        last_value = self.nodes[self.heap_size - 1]
        self.modify_hash(last_value, self.heap_size - 1, index)


    """
    String represtion of MinHeap is like list in python
    """
    def __repr__(self):
        return self.nodes.__repr__()


        
