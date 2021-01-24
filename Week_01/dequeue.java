// 用 addFirst 或 add last 这套新的 API 改写 Deque 的代码
Deque<String> deque = new LinkedList<String>();

deque.addFirst("a");
deque.addFirst("b");
deque.addFirst("c");
System.out.println(deque);

deque.addLast("d");
deque.addLast("e");
deque.addLast("f");
System.out.println(deque);

String first_str = deque.getFirst();
String last_str = deque.getLast();
System.out.println(first_str);
System.out.println(last_str);
System.out.println(deque);

while (deque.size() > 0) {
    System.out.println(deque.removeFirst());
}
System.out.println(deque);