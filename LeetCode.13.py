class Solution:
    def Roman_to_int(self, S: str) -> int:
        roman = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
        sum = 0
        for i in range(len(S) -1, -1, -1):
            num = roman[S[i]]
            if 3 * num < sum: 
                sum = sum - num
            else: 
                sum = sum + num
        return sum
