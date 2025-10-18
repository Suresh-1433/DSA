import java.util.*;

public class _4LargestSubarraySum {
    public static int largestSubarraySum(int[] arr) {
        int n = arr.length;
        int curSum = 0;
        int maxSum = Integer.MIN_VALUE;

        for (int i = 0; i < n; i++) {
            curSum += arr[i];
            maxSum = Math.max(maxSum, curSum);

            if (curSum < 0) {
                curSum = 0;
            }
        }

        return maxSum;
    }

  
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        int n = scanner.nextInt();
        int[] arr = new int[n];
        for (int i = 0; i < n; i++) {
            arr[i] = scanner.nextInt();
        }
        System.out.println(largestSubarraySum(arr));
    }
    
}
// import java.util.*;    

// public class Main {
//     public static int largestSubarraySum(int[] arr) {
//         int n = arr.length;
//         int ans = Integer.MIN_VALUE;

//         for (int i = 0; i < n; i++) {
//             int sum = 0;
//             for (int j = i; j < n; j++) {
//                 sum += arr[j];
//                 ans = Math.max(ans, sum);
//             }
//         }

//         return ans;
//     }

//     /*
//     public static void main(String[] args) {
//         Scanner scanner = new Scanner(System.in);
//         int n = scanner.nextInt();
//         int[] arr = new int[n];
//         for (int i = 0; i < n; i++) {
//             arr[i] = scanner.nextInt();
//         }
//         System.out.println(largestSubarraySum(arr));
//     }
//     */
// }