class Solution {
    public boolean isAnagram(String s, String t) {

        // First check if the strings are the same length. If not, it's not an Anagram.
        if (s.length() != t.length()) {
            return false;
        }

        // Crate array of int with index for each letter
        // Add count from string 's' and subtract count from string 't'
        // Sum of s+ and t- should be all zero if a valid anagram
        int[] count = new int[26];
        for (int i = 0; i < s.length(); i++) {
            count[s.charAt(i) - 'a']++;
            count[t.charAt(i) - 'a']--;
        }

        // Loop through count to find any non-zero counts
        for (int c : count) {
            if (c != 0) {
                return false;
            }
        }
        return true;
    }
}
