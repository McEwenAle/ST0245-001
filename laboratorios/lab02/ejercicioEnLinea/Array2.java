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
        for(; i > -1; i--){// n
          if(nums[i] == 4){break;}
        }
        int[] nNums = new int[nums.length - i - 1];
        i++;
        for(int j = 0;j < nNums.length && i < nums.length; j++){ // n
          nNums[j] = nums[i];
          i++;
        }
        return nNums;
    }
    

    public boolean only14(int[] nums) {
        for(int i = 0; i < nums.length; i++){ // n
          if(nums[i] != 1 && nums[i] != 4)return false;
        }
        return true;
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

    public boolean twoTwo(int[] nums) {
  
      for(int i = 0; i<nums.length; i++){
        if(nums[i]==2){
          if(nums.length == 1){
            return false;
          }
          switch(i){
            case 0:
              if(nums[i+1] != 2){
                return false;
              }
              break;
            default:
              if(i == nums.length-1 && nums[i-1] != 2){
                return false;
              }else if(i != nums.length-1 && nums[i+1] != 2 && nums[i-1] != 2){
                return false;
              }
              break;
          }
        }
      }
      return true;
    }
    
    public boolean sum28(int[] nums) {
      int sum = 0;
      for(int i = 0; i < nums.length; i++){
        if(nums[i] == 2){
          sum+=2;
        }
      }
      if(sum == 8){
        return true;
      }else{
        return false;
      }
    }
}
