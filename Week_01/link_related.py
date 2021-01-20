class Node:
    def __init__(self, data=None):
        self.data = data
        self.next = None


class LinkList:
    def __init__(self):
        self.head = None
        self.last = None
        self.size = 0

    def insert(self, data, index):
        if index < 0 or index > self.size:
            raise ValueError("Invalid Index")
        node = Node(data)
        if self.size == 0:
            self.head = node
            self.head = node
        elif index == 0:
            node.next = self.head
            self.head = node
        elif index == self.size:
            self.last.next = node
            self.last = node
        else:
            pre_node = self.get_node(index - 1)
            node.next = pre_node.next
            pre_node.next = node
        self.size += 1

    def remove(self, index):
        if index < 0 or index > self.size:
            raise ValueError("Invalid Index")
        node = None
        if index == 0:
            node = self.head
            self.head = self.head.next
        elif index == self.size - 1:
            pre_node = self.get_node(index - 1)
            node = pre_node.next
            pre_node.next = None
            self.last = pre_node
        else:
            pre_node = self.get_node(index - 1)
            next_node = pre_node.next.next
            node = pre_node.next
            pre_node.next = next_node
        self.size -= 1
        return node

    def get_node(self, param):
        tmp_node = self.head
        while param:
            tmp_node = tmp_node.next
            param -= 1
        return tmp_node

    def reverse(self):
        pre = self.head
        cur = self.head.next
        while cur:
            tmp = cur.next
            cur.next = pre
            pre = cur
            cur = tmp
        self.head.next = None
        self.head = pre

    def out_put(self):
        res = []
        tmp = self.head
        while tmp:
            res.append(tmp.data)
            tmp = tmp.next
        return res

    def is_circled(self):
        p1, p2 = self.head, self.head
        while p1 and p2.next:
            p1 = p1.next
            p2 = p2.next.next
            if p1 == p2:
                return True
        return False

    def get_circle_length(self):
        p1, p2, res = self.head, self.head, 0
        while p1 and p2.next:
            p1 = p1.next
            p2 = p2.next.next
            if p1 == p2:
                break
        if p2 is None or p2.next is None:
            return 0
        else:
            tmp = p1
            while tmp != p1.next:
                res += 1
                p1 = p1.next
        return res

    def get_cross_node(self):
        p1, p2, res = self.head, self.head, 0
        while p1 and p1.next:
            p1 = p1.next
            p2 = p2.next.next
            if p1 == p2:
                break
        p1 = self.head
        while p1 != p2:
            p1 = p1.next
            p2 = p2.next
        return p1

    def get_last_kth_num(self, k):
        if k < 0:
            raise ValueError("Invalid param")
        link_len = self.get_link_length()
        if k > link_len:
            raise ValueError("Invalid param")
        elif k == link_len:
            return self.head
        elif k == 0:
            return self.last
        else:
            return self.get_node(link_len - k)

    def get_link_length(self):
        res = 0
        tmp = self.head.next
        while tmp:
            res += 1
            tmp = tmp.next
        return res
