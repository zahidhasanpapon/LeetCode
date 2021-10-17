class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        seenCharacters = {}
        leftPointer, longestLength = 0, 0

        for rightPointer in range(len(s)):

            """if
            If s[rightPointer] is not in seenCharacters, we keep increasing the window
            by size by moving right pointer
            """
            """else
            There are 2 cases if s[rightPointer] is seen:
            
            case1: s[rightPointer] is inside the current window, we need to change the window
            by moving left pointer to seenCharacters[s[rightPointer]] + 1
            
            case2: s[rightPointer] is not inside the current window, we can keep increase the window
            """

            if s[rightPointer] not in seenCharacters:
                longestLength = max(
                    longestLength, rightPointer - leftPointer + 1)
            else:
                if seenCharacters[s[rightPointer]] < leftPointer:
                    longestLength = max(
                        longestLength, rightPointer - leftPointer + 1)
                else:
                    leftPointer = seenCharacters[s[rightPointer]] + 1

            seenCharacters[s[rightPointer]] = rightPointer

        return longestLength
