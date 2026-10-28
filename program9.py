def clean_text(text: str) -> str:
    """
    Cleans formatting variances by removing whitespace, punctuation, and lowercasing.
    Input:
        text (str): The raw input string (e.g., "Dirty room!").
    Output:
        str: The cleaned string containing only lowercase alphanumeric characters (e.g., "dirtyroom").
    """
    return ''.join(char.lower() for char in text if char.isalnum())


def is_anagram_sorting(text1: str, text2: str) -> bool:
    """
    Determines if two phrases are anagrams using list sorting algorithms.
    Input:
        text1 (str): First text phrase.
        text2 (str): Second text phrase.
    Output:
        bool: True if the cleaned phrases are valid anagrams, False otherwise.
    """
    clean1 = clean_text(text1)
    clean2 = clean_text(text2)
    return sorted(list(clean1)) == sorted(list(clean2))


def is_anagram_counting(text1: str, text2: str) -> bool:
    """
    Determines if two phrases are anagrams using dictionary counting techniques.
    Input:
        text1 (str): First text phrase.
        text2 (str): Second text phrase.
    Output:
        bool: True if the cleaned phrases are valid anagrams, False otherwise.
    """
    clean1 = clean_text(text1)
    clean2 = clean_text(text2)
    if len(clean1) != len(clean2):
        return False
        
    char_counts = {}
    for char in clean1:
        char_counts[char] = char_counts.get(char, 0) + 1

    for char in clean2:
        if char not in char_counts:
            return False
        char_counts[char] -= 1
        if char_counts[char] < 0:
            return False   
    return True


def build_anagram_lookup(phrases: list) -> dict:
    """
    Groups valid anagram pairs from a list using immutable tuple keys for fast lookup matchings.
    Input:
        phrases (list of str): A list of raw phrases to group.
    Output:
        dict: A dictionary where the key is an immutable tuple of sorted characters, 
              and the value is a list of matching anagram phrases.
    """
    lookup = {}
    for phrase in phrases:
        cleaned = clean_text(phrase)
        key = tuple(sorted(cleaned))
        if key not in lookup:
            lookup[key] = []
        lookup[key].append(phrase)  
    return lookup


if __name__ == "__main__":
    print("--- Text Anagram and Pattern Matcher Tool ---\n")
    phrase_a = "Listen"
    phrase_b = "Silent"
    phrase_c = "Dormitory"
    phrase_d = "Dirty room!"
    
    print("1. List Sorting Algorithm:")
    print(f"'{phrase_a}' & '{phrase_b}' -> {is_anagram_sorting(phrase_a, phrase_b)}")
    
    print("\n2. Dictionary Counting Technique:")
    print(f"'{phrase_c}' & '{phrase_d}' -> {is_anagram_counting(phrase_c, phrase_d)}")
    print(f"'{phrase_a}' & '{phrase_c}' -> {is_anagram_counting(phrase_a, phrase_c)}")
    print("\n3. Fast Lookup Grouping (Immutable Tuple Keys):")
    word_list = ["Listen", "Silent", "Enlist", "Rat", "Art", "Tar", "Hello", "Ohell"]
    anagram_groups = build_anagram_lookup(word_list)
    
    for key, group in anagram_groups.items():
        if len(group) > 1:
            print(f"Anagram Group for key {key}: {group}")