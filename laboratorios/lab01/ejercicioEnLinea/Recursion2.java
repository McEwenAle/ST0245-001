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
        return helper(0, nums, 0, 0);
    }

    private boolean helper(int start, int[] nums, int sum1, int sum2) {
        ...
    }
    
    public boolean split53(int[] nums) {
        return helper3(0, nums, 0, 0);
    }

    private boolean helper3(int index, int[] nums, int sum5s, int sum3n5) {
        ...
}
