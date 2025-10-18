
public class _5maximizeShareProfit {
    public static int maximizeShareProfit(int[] arr) {
        int n = arr.length;
        int minimum = arr[0];
        int max_profit = 0;
        for (int i = 1; i < n; i++) {
            int profit = arr[i] - minimum;
            max_profit = Math.max(max_profit, profit);
            minimum = Math.min(minimum, arr[i]);
        }
        return max_profit;
    }

    
    public static void main(String[] args) {
        int[] arr = {10, 11, 7, 10, 6, 9, 4};
        System.out.println(maximizeShareProfit(arr));
    }
    
}


// import java.util.*;

// public class Main {
//     public static int maximizeShareProfit(int[] arr) {
//         int n = arr.length;
//         int max_profit = 0;
//         for (int i = 0; i < n - 2; i++) {
//             for (int j = i + 1; j < n - 1; j++) {
//                 int profit = arr[j] - arr[i];
//                 max_profit = Math.max(max_profit, profit);
//             }
//         }
//         return max_profit;
//     }
    
    
//     public static void main(String[] args) {
//         int[] arr = {10, 11, 7, 10, 6, 9, 4};
//         System.out.println(maximizeShareProfit(arr));
//     }
    
// }