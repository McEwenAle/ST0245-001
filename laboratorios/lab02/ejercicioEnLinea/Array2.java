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

    public boolean haveThree(int[] nums) {
        int count = 0;
        for(int i = 0; i < nums.length; i++){
          if(nums[i] == 3){
            count += 1;
            if(i > 0 && nums[i] == nums[i-1]){
            return false;
            }
          }
        }
        if(count == 3){
          return true;
        }else{
          return false;
        }
      }

    public boolean only14(int[] nums) {
     
    }

    public String[] fizzArray2(int n) {
       
    }

    public boolean has12(int[] nums) {
       
    }
}
