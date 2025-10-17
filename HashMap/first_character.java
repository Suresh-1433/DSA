import  java.util.HashMap;
import  java.util.Map;

public class first_character {
  
  public static void main(String[] args) {
    String s= "aabbcdjkl";
     Map <Character,Integer> firstRepeating =  new HashMap<>();
     for (char c:s.toCharArray()){

      int x =firstRepeating.getOrDefault(c,0)+1;
      firstRepeating.put(c,x);

     }
     for(char res: firstRepeating.keySet()){
         if (firstRepeating.get(res) == 1){
          System.out.println("First Repeating Val: "+ res );
          break;
         }

     }
     
     System.err.println(firstRepeating);
  }
}
