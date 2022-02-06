
public class ArrayStack_2_4 { // public class ArrayStack 으로 했으나 하도 오류났다고 해서 그냥 클래스로 바꿈
    public int top;
    public int[] itemArray;
    public int stackSize;

    public ArrayStack_2_4(int stackSize) {
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

    public int pop() { // 스택의 톱에 있는 아이템 반환 왜 int pop() 인데 오류가 나지?
        // int 타입인데 int를 return 안해서 인듯하다 return -1 하면됨.
        if (isEmpty()) {
            System.out.println("Deleting fail ! Array Stack is empty!");
            return -1; // 본문에는 없음

        } else {
            return itemArray[top]; // [top-] 원본은 이렇게 되어 있음.
        }
    }

    public int peek() {
        if (isEmpty()) {
            System.out.println("Peeking fail ! Array Stack is empty!");
            return -1; // 본문에는 없음
        } else {
            return itemArray[top]; // [top-] 원본은 이렇게 되어 있음.
        }
    }
}