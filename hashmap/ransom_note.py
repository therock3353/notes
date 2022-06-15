"""
383 Ransom Note: https://leetcode.com/problems/ransom-note/
    Time Complexity O(n) + O(m) where n = num of char in note.
                                      m = num of char in text
"""

class Solution(object):
    def canConstruct(self, ransomNote, magazine):
        if not magazine or not ransomNote:
            return False
        if len(ransomNote) > len(magazine):
            return False
        mag_char_count_map = {}
        note_char_count_map = {}
        for char in magazine:
            if char in mag_char_count_map:
                mag_char_count_map[char] += 1
            else:
                mag_char_count_map[char] = 1

        for char in ransomNote:
            if char in note_char_count_map:
                note_char_count_map[char] += 1
            else:
                note_char_count_map[char] = 1

        for char, count in note_char_count_map.iteritems():
            if char not in mag_char_count_map:
                return False
            if count > mag_char_count_map.get(char):
                return False
        return True

if __name__=="__main__":
    text = "abcdeffa0oIdhskdsjmrrmsi"
    note = "I am a hero"
    print Solution().canConstruct(note, text)