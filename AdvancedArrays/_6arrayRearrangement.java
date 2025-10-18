
public class _6arrayRearrangement {
    public static int[] arrayRearrangement(int[] arr) {
        int n = arr.length;
        int[] ans = new int[n];
        int pos = 0;
        int neg = 1;
        for (int i = 0; i < n; i++) {
            if (arr[i] > 0) {
                ans[pos] = arr[i];
                pos += 2;
            } else {
                ans[neg] = arr[i];
                neg += 2;
            }
        }
        return ans;
    }

    public static void main(String[] args) {
        int[] arr = {-9, -4, 2, 3, -7, 10};
        arr = arrayRearrangement(arr);
        for (int x : arr) {
            System.out.print(x + " ");
        }
    } 
}



// import java.util.*;

// public class Main {
//     public static List<Integer> arrayRearrangement(List<Integer> arr) {
//         int n = arr.size();
//         List<Integer> positives = new ArrayList<>();
//         List<Integer> negatives = new ArrayList<>();

//         for (int i = 0; i < n; i++) {
//             if (arr.get(i) > 0) 
//                 positives.add(arr.get(i));
//             else 
//                 negatives.add(arr.get(i));
//         }

//         for (int i = 0; i < n; i++) {
//             if (i % 2 == 0) 
//                 arr.set(i, positives.get(i / 2));
//             else 
//                 arr.set(i, negatives.get(i / 2));
//         }

//         return arr;
//     }

// /*
//     public static void main(String[] args) {
//         List<Integer> arr = new ArrayList<>(List.of(-9, -4, 2, 3, -7, 10));
//         arr = arrayRearrangement(arr);
//         for (int x : arr) 
//             System.out.print(x + " ");
//     }
// */    
// }