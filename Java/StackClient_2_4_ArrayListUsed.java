
public class StackClient_2_4_ArrayListUsed {
    public static void main(String[] args) {
        ArrayListStack_2_4 st = new ArrayListStack_2_4(10);
        st.push(20); // st.itemArray[++st.top] = 20; -> st.push(20);
        System.out.println(st.peek()); // System.out.println(st.itemArray[st.top]); -> System.out.println(st.peek());
    }
}