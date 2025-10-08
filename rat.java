public class rat {
  static int rat(int x,int y,int grid[][]){
    int rowlen = grid.length;
    int col = grid[0].length;
    if (x<0 || y<0 || x>=rowlen || y>=col){
      return 0;
    }
    if(x==0 && y==0){
      return 1;
    }
    if (grid[x][y] == 0){
      return 0;
    }

    int right =  rat(x,y-1,grid);
    int down = rat(x-1,y,grid);
    int ans = right+down;
    return ans;

  }
  public static void main(String[] args) {
      int grid[][] = {
        {1,1,0},
        {0,1,1},
        {0,0,1},
      };
    int x = 2;
    int y = 2; 
    System.out.println(rat(x,y,grid));
      
  }
}
