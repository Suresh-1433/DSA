public class coins {
  static void denotionCon(int amount,int count[],int coinInd,int coins[])
  {
    if (amount == 0){
      count[0]++;
      return;
    }

    for (int ci = coinInd; ci < coins.length; ci++) {
        if (amount - coins[ci]>0){
          denotionCon(amount- coins[ci] ,count, ci, coins);
        }
         
    }
   
  }
  public static void main(String[] args) {
      int coins[] = {2,5,7};
      int count[] = {0};
      denotionCon(12,count,0,coins);
      
  }
}
