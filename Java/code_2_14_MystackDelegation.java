
//74p 위임 설명하면서 나온 클래스 
// 1. 자식클래스에서 부모클래스의 인스턴스를 참조하는 속성을 만든다. 이를 this로 초기화 한다.
// 2. 서브 클래스에 정의된 각 메서드에 1번 에서 위임 속성 필드를 참조하도록 변경한다. 
// 3. 서브 클래스에서 일반화 관계 선언을 제거하고 위임 속성 필드에 슈퍼 클래스의 객체를 생성해 대입한다.
// 4. 서브 클래스에서 사용된 슈퍼클래스의 메서드에도 위임 메서드를 추가한다.
// 5.컴파일 하고 잘 동작하는지 확인한다.

// 결론 private으로 인스턴스 하나 만들고 이것을 통하여 push,poop같은 메소드를 진행

import java.util.ArrayList;

public class code_2_14_MystackDelegation<String> {
    private ArrayList<String> arList = new ArrayList<String>();

    public void push(String element) {
        arList.add(element);
    }

    public String pop() {
        return arList.remove(arList.size() - 1);

    }

    public boolean isEmpty() {
        return arList.isEmpty();
    }

    public int size() {
        return arList.size();
    }
}
