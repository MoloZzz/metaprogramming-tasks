import wordfreq # type: ignore

# Example usage
text = """
This is a sample text. This text contains some words.
Some words are repeated in this sample text!
"""
n = 3
result = wordfreq.get_frequent_words(text, n)
print(f"Input text: {text.strip()}")
print(f"Top {n} frequent words: {result}")