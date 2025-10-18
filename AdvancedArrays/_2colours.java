import java.util.*;

public class _2colours {
    public static void arrangeColorsInOrder(int[] arr) {
        int n = arr.length;
        int low = 0;
        int mid = 0;
        int high = n - 1;

        while (mid <= high) {
            if (arr[mid] == 0) {
                swap(arr, low, mid);
                low++;
                mid++;
            } else if (arr[mid] == 1) {
                mid++;
            } else if (arr[mid] == 2) {
                swap(arr, mid, high);
                high--;
            }
        }
    }
    
    private static void swap(int[] arr, int i, int j) {
        int temp = arr[i];
        arr[i] = arr[j];
        arr[j] = temp;
    }
    
    
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        int n = scanner.nextInt();
        int[] arr = new int[n];
        for (int i = 0; i < n; i++) {
            arr[i] = scanner.nextInt();
        }
        
        arrangeColorsInOrder(arr);
        for (int num : arr) {
            System.out.print(num + " ");
        }
    }
    
    
}

// import java.util.*;

// public class Main {
//     public static void arrangeColorsInOrder(int[] arr) {
//         int n = arr.length;
//         int low = 0;
//         int mid = 0;
//         int high = n - 1;

//         while (mid <= high) {
//             if (arr[mid] == 0) {
//                 swap(arr, low, mid);
//                 low++;
//                 mid++;
//             } else if (arr[mid] == 1) {
//                 mid++;
//             } else if (arr[mid] == 2) {
//                 swap(arr, mid, high);
//                 high--;
//             }
//         }
//     }
    
//     private static void swap(int[] arr, int i, int j) {
//         int temp = arr[i];
//         arr[i] = arr[j];
//         arr[j] = temp;
//     }
    
//     /*
//     public static void main(String[] args) {
//         Scanner scanner = new Scanner(System.in);
//         int n = scanner.nextInt();
//         int[] arr = new int[n];
//         for (int i = 0; i < n; i++) {
//             arr[i] = scanner.nextInt();
//         }
        
//         arrangeColorsInOrder(arr);
//         for (int num : arr) {
//             System.out.print(num + " ");
//         }
//     }
//     */
    
}
//+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
// import java.util.*;

// public class Main {
//     public static void arrangeColorsInOrder(int[] arr) {
//         int n = arr.length;
//         int[] count = new int[3];

//         for (int i = 0; i < n; i++) {
//             count[arr[i]]++;
//         }

//         for (int i = 0; i < n; i++) {
//             if (i < count[0]) {
//                 arr[i] = 0;
//             } else if (i < count[0] + count[1]) {
//                 arr[i] = 1;
//             } else {
//                 arr[i] = 2;
//             }
//         }
//     }
    
//     /*
//     public static void main(String[] args) {
//         Scanner scanner = new Scanner(System.in);
//         int n = scanner.nextInt();
//         int[] arr = new int[n];
//         for (int i = 0; i < n; i++) {
//             arr[i] = scanner.nextInt();
//         }
        
//         arrangeColorsInOrder(arr);
//         for (int num : arr) {
//             System.out.print(num + " ");
//         }
//     }
//     */
// // }