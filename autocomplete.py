import nltk
from nltk.util import ngrams
from nltk.tokenize import word_tokenize
from collections import defaultdict, Counter
import random

nltk.download('punkt')

# Sample corpus
sample_text = """
Artificial intelligence is transforming the world. It powers self-driving cars, understands speech,
and makes decisions. Natural language processing helps machines understand human language.
Machine learning is a core part of AI, enabling systems to learn from data and improve over time.
"""

# Tokenize the text
tokens = sample_text.lower().split()

# Generate trigrams (n=3)
trigrams = list(ngrams(tokens, 3))

# Build a trigram model
model = defaultdict(Counter)
for w1, w2, w3 in trigrams:
    model[(w1, w2)][w3] += 1

# Auto-complete function
def autocomplete(w1, w2, top_k=3):
    candidates = model.get((w1.lower(), w2.lower()))
    if not candidates:
        return []

    # Return top_k suggestions
    return [word for word, _ in candidates.most_common(top_k)]

# Test input
word1 = "natural"
word2 = "language"

suggestions = autocomplete(word1, word2)
print(f"Suggestions after '{word1} {word2}': {suggestions}")
