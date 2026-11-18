import re


def analyze_text(paragraph):
    
    total_chars = len(paragraph)
    words = paragraph.split()
    word_count = len(words)

    
    vowels = 0
    consonants = 0
    digits = 0
    special_chars = 0

    vowel_set = "aeiouAEIOU"

    for char in paragraph:
        if char.isalpha():
            if char in vowel_set:
                vowels += 1
            else:
                consonants += 1
        elif char.isdigit():
            digits += 1
        elif not char.isspace():  
            special_chars += 1

    # Display analysis results
    print("\n--- Text Analysis Results ---")
    print(f"Total Words              : {word_count}")
    print(f"Total Characters (all)   : {total_chars}")
    print(f"Vowels                   : {vowels}")
    print(f"Consonants               : {consonants}")
    print(f"Digits                   : {digits}")
    print(f"Special Characters       : {special_chars}")


def search_text(paragraph, target):
    print(f"\n--- Search Results for '{target}' ---")

    
    lower_para = paragraph.lower()
    lower_target = target.lower()

    occurrences = lower_para.count(lower_target)
    first_index = lower_para.find(lower_target)

    print("[String Operations]")
    if occurrences > 0:
        print(f"Exact substring count    : {occurrences}")
        print(f"First occurrence index   : {first_index}")
    else:
        print("Substring not found.")

    
    print("\n[Regular Expressions]")
    try:
        
        pattern = re.compile(target, re.IGNORECASE)
        matches = list(pattern.finditer(paragraph))

        if matches:
            print(f"Total regex matches      : {len(matches)}")
            positions = [match.span() for match in matches]
            print(f"Match index ranges       : {positions}")
        else:
            print("No regex matches found.")
    except re.error as e:
        print(f"Invalid regular expression pattern: {e}")



if __name__ == "__main__":
    sample_paragraph = input("Enter a paragraph to analyze:\n> ")
    analyze_text(sample_paragraph)

    search_query = input("\nEnter a word or regex pattern to search:\n> ")
    search_text(sample_paragraph, search_query)
