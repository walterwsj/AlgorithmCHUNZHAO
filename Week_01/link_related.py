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

    def out_put(self):
        res = []
        tmp = self.head
        while tmp:
            res.append(tmp.data)
            tmp = tmp.next
        return res


def reverse(head):
    pre = head
    cur = head.next
    while cur:
        tmp = cur.next
        cur.next = pre
        pre = cur
        cur = tmp
    head.next = None
    return pre


def is_circled(head):
    p1, p2 = head, head
    while p1 and p2.next:
        p1 = p1.next
        p2 = p2.next.next
        if p1 == p2:
            return True
    return False


def get_circle_length(head):
    p1, p2, res = head, head, 0
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


def get_cross_node(head):
    p1, p2, res = head, head, 0
    while p1 and p1.next:
        p1 = p1.next
        p2 = p2.next.next
        if p1 == p2:
            break
    p1 = head
    while p1 != p2:
        p1 = p1.next
        p2 = p2.next
    return p1


def get_node(head, link_len):
    while link_len:
        head = head.next
        link_len -= 1
    return head


def get_last_kth_num(head, k):
    if k < 0:
        raise ValueError("Invalid param")
    link_len = get_link_length(head)
    if k > link_len:
        raise ValueError("Invalid param")
    elif k == link_len:
        return get_node(link_len)
    elif k == 0:
        return head
    else:
        return get_node(link_len - k)


def get_link_length(head):
    res = 0
    tmp = head.next
    while tmp:
        res += 1
        tmp = tmp.next
    return res


def swap_pairs(head):
    if head is None or head.next is None:
        return head
    dummy = Node(-1)
    dummy.next = head
    pre = dummy
    while pre.next and pre.next.next:
        start = pre.next
        end = pre.next.next
        pre.next = start.next
        start.next = end.next
        end.next = start
        pre = start
    return dummy.next


def swap_pairs_recurse(head):
    if head is None or head.next is None:
        return head
    next_node = head.next
    head.next = swap_pairs_recurse(next_node.next)
    next_node.next = head
    return head


def reverse_k_group_recurse(head, k):
    if head is None or head.next is None:
        return head
    cur, count = head, 0
    while cur and count != k:
        cur = cur.next
        count += 1
    if count == k:
        cur = reverse_k_group_recurse(cur, k)
        while count:
            tmp = head.next
            head.next = cur
            cur = head
            head = tmp
            count -= 1
        head = cur
    return head


def reverse_k_group_stack(head, k):
    if head is None or head.next is None:
        return head
    dummy = Node(0)
    pre = dummy
    while True:
        stack, count, tmp = [], k, head
        while count and tmp:
            stack.append(tmp)
            tmp = tmp.next
            count -= 1
        if count:
            pre.next = head
            break
        while stack:
            pre.next = stack.pop()
            pre = pre.next
        pre.next = tmp
        head = tmp
    return dummy.next


def reverse_k_group(head, k):
    if head is None or head.next is None:
        return head
    dummy = Node(0)
    dummy.next = head
    pre, tail = dummy, dummy
    while True:
        count = k
        while count and tail:
            tail = tail.next
            count -= 1
        if not tail:
            break
        head = pre.next
        while pre.next != tail:
            cur = pre.next
            pre.next = cur.next
            cur.next = tail.next
            tail.next = cur
        pre = head
        tail = head
    return dummy.next
