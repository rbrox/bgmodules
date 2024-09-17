import nltk
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer

# Download resources from NLTK if necessary
nltk.download('stopwords')
nltk.download('wordnet')

def preprocess_text(text):
    """Preprocess the input text to reduce token usage and improve efficiency."""
    
    # Initialize stopwords and lemmatizer
    stop_words = set(stopwords.words('english'))
    lemmatizer = WordNetLemmatizer()
    
    # Tokenize and preprocess text
    words = text.split()
    
    # Lowercase, remove stopwords, and lemmatize
    processed_words = [
        lemmatizer.lemmatize(word.lower()) 
        for word in words 
        if word.lower() not in stop_words
    ]
    
    return ' '.join(processed_words)

# Example usage
text = "Artificial Intelligence (AI) is the simulation of human intelligence in machines designed to think like humans."
processed_text = preprocess_text(text)
print(processed_text)
