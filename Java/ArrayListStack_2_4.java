import java.util.ArrayList;

public class ArrayListStack_2_4 { // 클래스 ArrayListStack으로 변경

    public ArrayList<Integer> items; // top 을 제거하고 배열에서 ArrayList로 변경 int[] -> ArrayList<Integer>
    public int stackSize;

    public ArrayListStack_2_4(int stackSize) {
        items = new ArrayList<Integer>(stackSize); // int[stackSize] -> ArrayListStack<Integer>(stackSize)
        this.stackSize = stackSize;
    }

    public boolean isEmpty() { // 스택이 비어있는지 검사
        return items.isEmpty(); // return (top == -1); -> return items.isEmpty()
    }

    public boolean isFull() { // 스택이 가득차 있는지 검사
        return (items.size() >= this.stackSize); // top == this.stackSize - 1 -> items.size() >= this.stackSize
    }

    public void push(int item) { // 스택에 아이템 추가
        if (isFull()) {
            System.out.println("Inserting fail! Array Stack is full!!");
        } else {
            items.add(new Integer(item));
            // new Integer(item)이 왜 밑줄이 되지? It is rarely appropriate to use this //
            // constructor. The static factory Integer.valueOf(int) is generally a
            // better choice, as it is likely to yield significantly better space
            // and time performance.
            // Java9 이상부터는 new Integer() 를 deprecated하였음. 성능향상을 위한것이라고 함. 수정
            // https://cr.openjdk.java.net/~vromero/constant.api/javadoc.04/deprecated-list.html
            System.out.println("Inserted Item : " + item); // itemArray[++top] = item; 제거
        }
    }

    public int pop() { // 스택의 톱에 있는 아이템 반환
        if (isEmpty()) {
            System.out.println("Deleting fail !");
            return -1;

        } else {
            return items.remove(items.size() - 1); // [top-] 원본은 이렇게 되어 있음.
            // return itemArray[top]; 제거
        }
    }

    public int peek() {
        if (isEmpty()) {
            System.out.println("Peeking fail ! Array Stack is empty!");
            return -1;
        } else {
            return items.get(items.size() - 1); // [top-] 원본은 이렇게 되어 있음.
            // itemArray[top]; 제거
        }
    }
}
