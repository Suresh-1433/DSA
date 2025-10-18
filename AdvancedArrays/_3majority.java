import java.util.*;

public class _3majority {
    public static int majorityElement(List<Integer> arr) {
        int n = arr.size();
        int majority = 1;
        int leader = arr.get(0);

        for (int i = 1; i < n; i++) {
            if (majority == 0) {
                leader = arr.get(i);
                majority += 1;
            } else {
                if (arr.get(i) == leader) majority += 1;
                else majority -= 1;
            }
        }

        return leader;
    }

    
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        int n = scanner.nextInt();
        List<Integer> arr = new ArrayList<>();
        for (int i = 0; i < n; i++) {
            arr.add(scanner.nextInt());
        }
        System.out.println(majorityElement(arr)); 
    }
    
}