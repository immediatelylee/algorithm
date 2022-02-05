
public class ArrayStack {
    public int top;
    public int[] itemArray;
    public int stackSize;

    public ArrayStack(int stackSize) {
        itemArray = new int[stackSize];
        top = -1;
        this.stackSize = stackSize;
    }

    public boolean isEmpty() { // 스택이 비어있는지 검사
        return (top == -1);
    }

    public boolean isFull() { // 스택이 가득차 있는지 검사
        return (top == this.stackSize - 1);
    }

    public void push(int item) { // 스택에 아이템 추가
        if (isFull()) {
            System.out.println("Inserting fail! Array Stack is full!!");
        } else {
            itemArray[++top] = item;
            System.out.println("Inserted Item : " + item);
        }
    }

    public int pop() { // 스택의 톱에 있는 아이템 반환
        if (isEmpty()) {
            System.out.println("Deleting fail ! Array Stack is empty!");
        } else {
            return itemArray[top]; // [top-] 원본은 이렇게 되어 있음.
        }
    }

    public int peek() {
        if (isEmpty()) {
            System.out.println("Peeking fail ! Array Stack is empty!");
        } else {
            return itemArray[top]; // [top-] 원본은 이렇게 되어 있음.
        }
    }
}

public class StackClient_2_4 {
    public static void main(String[] args) {
        ArrayStack st = new ArrayStack(10);
        st.itemArray[++st.top] = 20;
        System.out.println(st.itemArray[st.top]);
    }
}