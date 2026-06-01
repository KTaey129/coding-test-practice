# 문제 3. 애너그램 그룹화 — 정렬 키 vs 빈도 키
# 난이도: Medium
# 문자열 리스트 words가 주어진다. 서로 애너그램인 단어끼리 묶어서 반환하라. (애너그램 = 글자 구성이 같은 단어)
# 입력:  words = ["eat", "tea", "tan", "ate", "nat", "bat"]
# 출력:  [["eat","tea","ate"], ["tan","nat"], ["bat"]]
#        # 그룹 순서·그룹 내 순서는 무관
# 제약: 1 ≤ len(words) ≤ 10⁴. 그룹을 묶는 키를 어떻게 만들지가 핵심.

def group_anagrams(words):
    anagram_map = {}
    # group by sorted word
    for word in words:
        sorted_word = ''.join(sorted(word))
        # .join() is used to concatenate the sorted characters back into a string
        # sorted() returns a list of characters, so we need to join them to form the key
        if sorted_word not in anagram_map:
            # If the sorted word is not already a key in the anagram_map, we create a new entry with an empty list
            anagram_map[sorted_word] = []
        # append the original word to the list corresponding to the sorted key
        anagram_map[sorted_word].append(word)
    # return the values of the anagram_map, which are lists of anagrams
    return list(anagram_map.values())
    # return anagram_map.values()
        # it returns like this: dict_values([['eat', 'tea', 'ate'], ['tan', 'nat'], ['bat']])
        
    # values() returns a view of the values in the dictionary, which are the lists of anagrmas
    # what is the view? A view is a dynamic window into the dictionary's values. It reflects changes to the dictionary, so if we modify the anagram_map after calling values(), the view will reflect those changes. However, since we want to return a list of lists, we need to convert this view into a list using list(). This way, we get a static list of the groups of anagrams that we can return as the final output.
    # what is the dynamic window? A dynamic window means that the view will automatically update to reflect any changes made to the dictionary. For example, if we add a new key-value pair to the anagram_map after calling values(), the view will include this new pair when we access it. However, since we want to return a fixed list of groups of anagrams, we need to convert the view into a list at the time of return, ensuring that we have a snapshot of the current state of the anagram groups.
    # is view a type of list? No, a view is not a type of list. It is a special object that provides a dynamic view of the dictionary's values. It behaves like a list in some ways (e.g., you can iterate over it), but it is not an actual list and does not support all list operations. Therefore, we need to convert it to a list to get the desired output format.
    # so list type is static? Yes, a list is a static data structure in the sense that it holds a fixed set of elements at the time it is created. Once we convert the view into a list, we have a snapshot of the current state of the anagram groups, and this list will not change even if we modify the original dictionary afterward. This is why we use list() to convert the view into a list before returning it, ensuring that our output is consistent and does not reflect any future changes to the anagram_map.
    # why do we need to convert the view into a list? We need to convert the view into a list because the output format requires a list of lists. The values() method returns a view object that provides a dynamic view of the dictionary's values, but it is not a list itself. By converting it to a list, we can ensure that we are returning the correct data structure that matches the expected output format. Additionally, converting to a list allows us to have a static snapshot of the anagram groups at the time of return, which is important for ensuring that our output does not change if we modify the original dictionary afterward.

    # list() is used to convert the view into a list, which is the required output format

# Example usage:
words = ["eat", "tea", "tan", "ate", "nat", "bat"]
print(group_anagrams(words))

assert group_anagrams(words) == [["eat","tea","ate"], ["tan","nat"], ["bat"]]

# solution of it as using tuple
# Instead of sorting the word (which is O(k log k)), you use a character frequency count as the key.
#Since the problem says only lowercase letters, there are always exactly 26 possible characters. So you make a tuple of 26 counts:
def group_anagrams(words):
    anagram_map = {}
    for word in words:
        count = [0] * 26  # Initialize a list of 26 zeros for character counts
        for char in word:
            count[ord(char) - ord('a')] += 1  # Increment the count for the corresponding character
        key = tuple(count)  # Convert the list to a tuple to use as a dictionary key
        if key not in anagram_map:
            anagram_map[key] = []  # Create a new entry if the key is not already in the map
        anagram_map[key].append(word)  # Append the original word to the list corresponding to the key
    return list(anagram_map.values())  # Return the values of the anagram_map as a list of lists
    # In practice for coding tests, the sorting approach is fine — word lengths are rarely long enough for this to matter. But it's a good optimization to mention in an interview.
    