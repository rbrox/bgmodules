import nltk
from nltk.corpus import words
from collections import Counter
import re



# Download word frequency corpus
nltk.download('words')
nltk.download('brown')
nltk.download('punkt')
nltk.download('punkt_tab')

# Load the Brown corpus (pre-trained word frequencies)
from nltk.corpus import brown

# Function to get word frequency from the corpus
def get_word_frequency(word):
    word_freq = nltk.FreqDist(brown.words())
    return word_freq[word.lower()] if word.lower() in word_freq else 1  # Return 1 if the word is rare

# Function to compute word rarity score
def calculate_rarity_score(text):
    # Tokenize the text
    words_in_text = nltk.word_tokenize(text.lower())
    
    # Create a dictionary with word frequencies (rarer words get higher scores)
    word_rarity = {word: 1 / get_word_frequency(word) for word in words_in_text if word.isalpha()}
    
    return word_rarity

# Function to generate the fill-in-the-blank version of the text
def fill_in_the_blanks(text, top_n=5):
    word_rarity = calculate_rarity_score(text)
    
    # Sort words by their rarity score (descending order)
    rarest_words = sorted(word_rarity.items(), key=lambda x: x[1], reverse=True)[:top_n]
    
    # Create a version of the text where the rarest words are replaced with blanks
    blanked_text = text
    for rare_word, _ in rarest_words:
        blanked_text = re.sub(rf'\b{rare_word}\b', '_____', blanked_text, flags=re.IGNORECASE)

    # Output the original rarest words
    return blanked_text, [word for word, score in rarest_words]

# Test with a sample text
text = """
In a quaint village nestled between verdant hills, there stood a grandiose manor. Its majestic towers pierced the heavens, 
and its opulent halls echoed with the laughter of aristocrats. Every intricate detail in the manor's architecture told a story 
of a bygone era, a time of opulence and grandeur.
"""

# Generate fill-in-the-blank text
blanked_text, rare_words = fill_in_the_blanks(text)

print("Fill-in-the-Blank Text:\n", blanked_text)
print("\nTop 5 Rare Words:\n", rare_words)
