///search insert position
import java.util.Scanner;
 
 public class Binarysearch {
 
 	 public static int searchInsert(int[] nums, int target) {
 	 	 
 	 //Write your code here.
      int l=0 , r =nums.length - 1 , mid = 0;
      while(l <= r){
           mid = l + ( r - l ) / 2;
          if(nums[mid] == target){
              return mid;
          }
          else if(nums[mid] < target){
              l = mid +1;
          }else{
              r= mid -1 ;
          }
      }
      return l;
 
 
 	 }
 
 	 public static void main(String[] args) {
 
 	 	 Scanner s = new Scanner(System.in);
 	 	 int n = s.nextInt();
 	 	 int[] nums = new int[n];
 	 	 for (int i = 0; i < nums.length; i++) {
 	 	 	 nums[i] = s.nextInt();
 	 	 }
 	 	 int target = s.nextInt();
 	 	 System.out.println(searchInsert(nums, target));
 	 }
 
 }