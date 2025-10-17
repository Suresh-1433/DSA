
import java.util.HashMap;
import java.util.Map;

public class frequencyCount{
    public static void main(String[] args) {
        String s = "programming";
        Map <Character,Integer> frequency =  new HashMap<>();

        for (char c :s.toCharArray()){
          int cCount = frequency.getOrDefault(c, 0)+1;
          frequency.put(c,cCount);
        }
        System.err.println(frequency);
    }


}