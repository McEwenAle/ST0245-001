/**
 * 
 * @author anietog1, ditrefftzr
 */
public class Recursion1 {
    public int triangle(int rows) {
        if (rows == 0) return 0; //C
        return rows + triangle(rows - 1); //C + T(n-1)
        //MODELO: T(n) =   |C, n=0
        //                 |C + T(n-1), n>0
        //ECUACION DE RECURRENCIA: 
        //          T(n) = C*n + C1
        //CÁLCULO DE COMPLEJIDAD:
        //          O(C*n + C1)
        //          O(C*n)      -> Por regla de la suma
        //          O(n)        -> Por regla de la multiplicación
    }
    
    public int fibonacci(int n) {
        if(n == 0)return 0;
        if(n <= 2)return 1;
        return fibonacci(n - 1) + fibonacci(n - 2);
    }
    
    public int sumDigits(int n) {
        if(n == 0) return 0;
        return sumDigits(n/10) + n % 10;
     }
    
     public int countX(String str) {
        if(str.lastIndexOf("x") == -1 ) return 0;
        return 1 + countX(str.substring(0,str.lastIndexOf("x")));
      }
    
    public int countHi(String str) {
        if(str.lastIndexOf("hi")==-1) return 0;
        return 1 + countHi(str.substring(0,str.lastIndexOf("hi")));
    }
    
    public int count11(String str) {
        if(str.lastIndexOf("11")==-1) return 0;
        return 1 + count11(str.substring(0,str.lastIndexOf("11")));
      }
}
