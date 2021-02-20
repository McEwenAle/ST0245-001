/**
 * 
 * @author anietog1, ditrefftzr
 */
public class Recursion2 {
    public boolean groupSum6(int start, int[] nums, int target) {
        if (start >= nums.length) return target == 0; //C

        if (groupSum6(start + 1, nums, target - nums[start])) return true; //C + T(n-1)
        
        if (nums[start] == 6) target -= 6; //C
        
        return groupSum6(start + 1, nums, target); //C + T(n+1)
        //MODELO: T(n) =    |C, n=0
        //                  |C + T(n-1) + T(n-1), n>0
        //ECUACION DE RECURRENCIA:
        //              C(2^n - 1) + C1*2^(n-1)
        //COMPLEJIDAD
        //          O(C(2^n - 1) + C1*2^(n-1))
        //          O(C(2^n) + C1*2^(n))        -> Por regla de la suma             (2 veces)
        //          O(2^n + 2^n)                -> Por regla de la multiplicacion   (2 veces)
        //          O(2*2^n)
        //          O(2^n)                      -> Por regla de la multiplicacion
    }
    
    public boolean groupNoAdj(int start, int[] nums, int target) {
        if(start >= nums.length)return target == 0;
        boolean a = groupNoAdj(start+2, nums, target - nums[start]);
        boolean b = groupNoAdj(start+1, nums, target);
        return a || b;
      }
      
    
      public boolean groupSum5(int start, int[] nums, int target) {
        if (start == nums.length) return target == 0; //C
        if (nums[start] % 5 == 0){
          if(!(start + 1 == nums.length) && nums[start+1] == 1)return groupSum5(start + 2, nums, target - nums[start]);
          return groupSum5(start + 1, nums, target - nums[start]);
        }
        return groupSum5(start + 1, nums, target) || groupSum5(start + 1, nums, target - nums[start]);
      }
      
    
      public boolean groupSumClump(int start, int[] nums, int target) {
        if(start >= nums.length)return target == 0;
        int i;
        for(i = start + 1; i < nums.length; i++){
          if(nums[start] != nums[i])break;
        }
        boolean a = groupSumClump(i, nums, target - ((i-start)*nums[start]));
        boolean b = groupSumClump(i, nums, target);
        return a || b;
      }
      
    
    public boolean splitArray(int[] nums) {
        return helperSplitArray(0, nums, 0, 0);
    }
      
    private boolean helperSplitArray(int index, int[] nums, int sum1, int sum2) {
        if(index >= nums.length) return sum1==sum2;
        return helperSplitArray(index+1, nums, sum1+nums[index], sum2) || helperSplitArray(index+1, nums, sum1, sum2+nums[index]);
    }
    
    public boolean splitOdd10(int[] nums) {
      return helperOdd10(0, nums, 0, 0);
    }
    private boolean helperOdd10(int index, int[] nums, int sumOdd, int sum10) {
      if(index >= nums.length) return sumOdd % 2 == 1 && sum10 % 10 == 0;
      return helperOdd10(index+1, nums, sumOdd + nums[index], sum10) || helperOdd10(index+1, nums, sumOdd, sum10 + nums[index]); 
    }
}
  
