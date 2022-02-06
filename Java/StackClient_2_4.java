
public class StackClient_2_4 {
    public static void main(String[] args) {
        ArrayStack_2_4 st = new ArrayStack_2_4(10);
        st.itemArray[++st.top] = 20;
        System.out.println(st.itemArray[st.top]);
    }
}