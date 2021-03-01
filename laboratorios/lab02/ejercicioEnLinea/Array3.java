public class Array3 {

    public int maxSpan(int[] nums) {
        int max = 0;//C
        for (int i = 0; i < nums.length; i++) {//n*C

            int j = nums.length - 1;//n*C
            for (;; j--) {//n*n*C
                if (nums[j] == nums[i]) {//n*n*C
                    break;//n*n*C
                }
            }

            int span = j - i + 1;//n*C

            if (span > max) {//n*C
                max = span;//n*C
            }
        }
        return max;//C
        //Complejidad O(n*n)
    }

    public int[] fix45(int[] nums) {
        for(int i = 0; i < nums.length; i++){
          if(nums[i] == 4 && nums[i+1] != 5){
            for(int j = 0; j < nums.length; j++){
              if(nums[j] == 5 && !(j != 0 && nums[j-1] == 4)){
                nums[j] = nums[i + 1];
                nums[i + 1] = 5;
                break;
              }
            }
          }
        }
        return nums;
      }
      

      public boolean canBalance(int[] nums) {
        int sum = nums[0];
        int sum2 = 0;
        for(int i = 1; i < nums.length; i++)sum2 += nums[i];
        for(int i = 1; i < nums.length; i++){
          if(sum == sum2)return true;
          sum += nums[i];
          sum2 -= nums[i];
        }
        return false;
      }
      

      public boolean linearIn(int[] outer, int[] inner) {
        int j = 0;
        if(j == inner.length)return true;
        for(int i = 0; i < outer.length; i++){
          if(outer[i] == inner[j])j++;
          if(j == inner.length)return true;
        }
        return false;
      }
      

    public int[] seriesUp(int n) {
      
    }
}
