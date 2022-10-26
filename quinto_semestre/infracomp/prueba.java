import java.util.LinkedList;

public class prueba{
    public void hacer(){
        LinkedList<Integer> list = new LinkedList<Integer>();
        for (int i = 0; i < 10; i++) {
            System.out.println(i);
            list.add(i);
        }
        System.out.println(list);
        list.removeFirst();
        System.out.println("removefirst"+list);
        list.add(11);
        System.out.println("add10:"+list);
    }
    public static void main(String[] args) {
        prueba p = new prueba();
        tlbSize = 5;
        System.out.println(TLB_SIZE);
        tlbSize = 6;
        System.out.println(TLB_SIZE);

    }
}
