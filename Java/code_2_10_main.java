// 72p ArrayList클래스에 정의 된 스택과 관련없는 연산이나 속성도 물려받기때문에 2-10처럼 직접 만들어준것
// push 나 pop을 직접 만들어준것이지만 스택의 무결성 조건인 LIFO를 위배한다. 

public class code_2_10_main {
    public static void main(String[] args) {
        MyStack<String> st = new MyStack<String>();

        st.push("insang1");
        st.push("insang2");
        st.set(0, "insang3"); // 허용되어서는 안됨
        System.out.println(st.pop());
        System.out.println(st.pop());

    }
}
// the type parameter String is hiding the type String 오류는 왜나지?
