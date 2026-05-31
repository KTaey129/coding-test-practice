# 문제 2. 빈도수 세기 — 카운터 패턴
# 난이도: Easy
# 문자열 s가 주어진다. 가장 많이 등장한 문자와 그 횟수를 반환하라. 동률이면 사전순으로 앞선 문자를 반환한다.
# 입력:  s = "banana"
# 출력:  ('a', 3)

# 입력:  s = "abccba"
# 출력:  ('a', 2)        # a,b,c 모두 2회 → 사전순 'a'
# 제약: 1 ≤ len(s) ≤ 10⁵, 소문자 알파벳만.
def most_frequent_char(s):
    freq = {}
    # freq: save the frequency of each character. it's a hash map (dictionary) where the key is the character and the value is its count.
    for char in s:
    # iterate through each character in the string s
        if char in freq:
            # if the character is already in the freq dictionary, increment its count by 1
            freq[char] += 1
        else:
            # if the character is not in the freq dictionary, add it with a count of 1
            freq[char] = 1

    # find the character with the highest frequency. if there is a tie, return the character that comes first in alphabetical order.
    max_freq = 0
    max_char = ''
    for char, count in freq.items():
        if count > max_freq:
            # if the current character's count is greater than the max frequency found so far, update max_freq and max_char
            max_freq = count
            max_char = char
        elif count == max_freq and char < max_char:
            # if the current character's count is equal to the max frequency and the character is alphabetically smaller than the current max_char, update max_char
            max_char = char
    return (max_char, max_freq)

# Example usage:
assert most_frequent_char("banana") == ('a', 3)
assert most_frequent_char("abcaba") == ('a', 3)