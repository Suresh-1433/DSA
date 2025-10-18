import java.util.*;

class Pair<A, B> {
    public  A first;
    public  B second;

    public Pair(A first, B second) {
        this.first = first;
        this.second = second;
    }
}

class _1twosumArray {
    public static int[] twoSum(int[] arr, int k) {
        int n = arr.length;
        List<Pair<Integer, Integer>> indexArr = new ArrayList<>();

        for (int i = 0; i < n; i++) {
            indexArr.add(new Pair<>(arr[i], i));
        }

        indexArr.sort(Comparator.comparingInt(o -> o.first));

        int i = 0;
        int j = n - 1;

        while (i < j) {
            int sum = indexArr.get(i).first + indexArr.get(j).first;
            if (sum == k) {
                return new int[]{indexArr.get(i).second, indexArr.get(j).second};
            }
            if (sum < k) {
                i++;
            } else {
                j--;
            }
        }

        return new int[]{-1, -1};
    }


    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        int n = scanner.nextInt();
        int[] arr = new int[n];
        for (int i = 0; i < n; i++) {
            arr[i] = scanner.nextInt();
        }
        int k = scanner.nextInt();
        
        int[] x = twoSum(arr, k);
        System.out.println(x[0] + " " + x[1]);
    }

}