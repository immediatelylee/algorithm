

public class Kid {
    private Robot toy;

    public void setToy(Robot toy){
        this.toy = toy;
    }

    public void play() {
        System.out.println(toy.toString());
    }
}

public class Main {
    pulbic static void main(String[] args){
        Robot t = new Robot();
        Kid k = new Kid();
        k.setToy(t);
        k.play();
    }
}