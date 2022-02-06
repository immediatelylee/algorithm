// 72p ArrayList클래스에 정의 된 스택과 관련없는 연산이나 속성도 물려받기때문에 2-10처럼 직접 만들어준것
// push 나 pop을 직접 만들어준것이지만 스택의 무결성 조건인 LIFO를 위배한다. 

import java.util.ArrayList;

class MyStack<String> extends ArrayList<String> {
    public void push(String element) {
        add(element);
    }

    public String pop() {
        return remove(size() - 1);
    }

}
// the type parameter String is hiding the type String 오류는 왜나지?
