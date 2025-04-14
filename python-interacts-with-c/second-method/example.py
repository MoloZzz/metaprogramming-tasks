import wordfreq # type: ignore

# Example usage
text = """
This is a sample text. This text contains some words.
Some words are repeated in this sample text!
Some more text to test the word frequency.
This is a test text to check the word frequency.
"""
n = 10
result = wordfreq.get_frequent_words(text, n)
print(f"Input text: {text.strip()}")
print(f"Top {n} frequent words: {result}")