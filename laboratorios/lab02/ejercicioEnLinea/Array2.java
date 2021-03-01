public class Array2 {

    public int countEvens(int[] nums) {
        int count = 0;//        C
        for (int n : nums) {//  n
            if (n % 2 == 0) {// n
                count++;    //  n
            }
        }
        return count;       //C
        //Complejidad O(n)
    }

    public int[] post4(int[] nums) {
        int i = nums.length - 1;
        for(; i > -1; i--){
          if(nums[i] == 4){break;}
        }
        int[] nNums = new int[nums.length - i - 1];
        i++;
        for(int j = 0;j < nNums.length && i < nums.length; j++){
          nNums[j] = nums[i];
          i++;
        }
        return nNums;
    }
    

    public boolean only14(int[] nums) {
        for(int i = 0; i < nums.length; i++){
          if(nums[i] != 1 && nums[i] != 4)return false;
        }
        return true;
      }
      

    public String[] fizzArray2(int n) {
       
    }

    public boolean has12(int[] nums) {
       
    }
}
