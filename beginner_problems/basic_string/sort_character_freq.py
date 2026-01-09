=================================================================================================
# 6. Sort Character by Frequency
=================================================================================================
'''
Given a string s, sort it in decreasing order based on the frequency of the characters.
The frequency of a character is the number of times it appears in the string.
Return the sorted string. If there are multiple answers, return any of them.

Example 1:

Input: s = "tree"
Output: "eert"
Explanation: 'e' appears twice while 'r' and 't' both appear once.
So 'e' must appear before both 'r' and 't'. Therefore "eetr" is also a valid answer.

Example 2:

Input: s = "cccaaa"
Output: "aaaccc"
Explanation: Both 'c' and 'a' appear three times, so both "cccaaa" and "aaaccc" are valid answers.
Note that "cacaca" is incorrect, as the same characters must be together.

Example 3:

Input: s = "Aabb"
Output: "bbAa"
Explanation: "bbaA" is also a valid answer, but "Aabb" is incorrect.
Note that 'A' and 'a' are treated as two different characters.
'''
=================================================================================================
# Solution
=================================================================================================
class Solution:
    def frequencySort(self, s: str) -> str:
        # empty dictionay
        freq = {}

        # if key present add + 1 or remain 1 
        for ch in s:
            freq[ch] = freq.get(ch, 0) + 1
        
        # Change dict to list inside tuple
        freq_items = [(v, k)for k, v in freq.items()]

        # Sort the values
        freq_items.sort(key= lambda x : (-x[0], x[1]))

        # Return Result
        result = []
        for f, ch in freq_items:
            result.append(ch * f)
        return "".join(result)

        '''
freq.get('e', 0)
Python checks:
Is 'e' in freq? ✅ Yes
Return stored value → 1
Then:
freq['e'] = 1 + 1
freq['e'] = 2
        '''
=================================================================================================
