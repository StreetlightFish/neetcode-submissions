class Solution {
    public boolean hasDuplicate(int[] nums) {
        Set<Integer> seen = new HashSet<>();

        /* Loop through nums
        *  if int in set, return true
        *  otherwise add int to set
        *  return false after loop
        */

        for (int num : nums) {
            if (!seen.add(num)) {
                return true;
            }
        }

        // Otherwise return false
        return false;
    }
}