class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        if len(strs) == 1:
            return [strs]

        # dict key: cnt tuple -> value: list
        anagram_dict = defaultdict(list)

        for word in strs:
            cnt = [0] * 26
            for char in word:
                cnt[ord(char) - ord('a')] += 1
            anagram_dict[tuple(cnt)].append(word)

        return list(anagram_dict.values())