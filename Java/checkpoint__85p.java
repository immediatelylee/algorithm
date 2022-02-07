public class checkpoint__85p {
    public static void doIt() {
        System.out.println("doIT: A class method");
    }

    public void doThat() {
        System.out.println("doThat: A class method");
    }
}

public class A1 extends checkpoint__85p {
    public static void doIt() {
        System.out.println("doIt:A1 class method");
    }

    public void doThat() {
        System.out.println("doTaht:A1 method");
    }
}

public class Main {
    public static void main(String[] args) {
        checkpoint__85p a1 = new A1();
        A1 a2 = new A1();

        a1.doIt();
        a1.doTaht();
        a2.doIt();
    }
}

// Doit:A class method
// DoThat: A1 class method
// DoIt:A1 class method