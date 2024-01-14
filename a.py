class Solution:
    def halvesAreAlike(self, s: str) -> bool:
        # Helper function to count vowels in a given string
        def count_vowels(string):
            vowels = set('aeiouAEIOU')
            return sum(1 for char in string if char in vowels)

        # Calculate the length of the input string
        length = len(s)
        
        # Find the midpoint of the string
        mid_point = length // 2

        # Extract the first and second halves of the string
        first_half = s[:mid_point]
        second_half = s[mid_point:]

        # Compare the counts of vowels in the first and second halves
        return count_vowels(first_half) == count_vowels(second_half)
