import string
from collections import Counter

def analyze_text(text_input):

    translator = str.maketrans('', '', string.punctuation)
    cleaned_text = text_input.lower().translate(translator)
    
    words = cleaned_text.split()
    
    total_words = len(words)
    
    word_frequencies = Counter(words)
    distinct_word_count = len(word_frequencies)
    
    palindromes = {word for word in words if len(word) > 1 and word == word[::-1]}
    
    report = [
        "========================================",
        "        TEXT ANALYTICAL REPORT          ",
        "========================================",
        f"Total Word Count   : {total_words}",
        f"Distinct Words     : {distinct_word_count}",
        "----------------------------------------",
        f"Palindromes Detected ({len(palindromes)}):"
    ]
    
    if palindromes:
        report.append(" > " + ", ".join(sorted(palindromes)))
    else:
        report.append(" > None found.")
        
    report.append("----------------------------------------")
    report.append("Word Frequency Table (Top 10):")
    
    for word, count in word_frequencies.most_common(10):
        report.append(f" > {word} : {count}")
        
    report.append("========================================")
    
    return "\n".join(report)

if __name__ == "__main__":
    sample_text = """
    Madam, in Eden, I'm Adam. 
    This is a test text! It contains some words, and some words are repeated multiple times.
    Radar, level, rotor, and kayak are all fun palindromes. 
    Let's test this text analyzer tool!
    """
    
    print(analyze_text(sample_text))