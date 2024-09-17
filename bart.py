import torch
from transformers import BartTokenizer, BartForConditionalGeneration
import nltk
from nltk.tokenize import sent_tokenize

# Download NLTK tokenizers if not already available
nltk.download('punkt')

class BartQuestionGenerator:
    def __init__(self):
        # Load the BART model and tokenizer for question generation
        self.tokenizer = BartTokenizer.from_pretrained('facebook/bart-large')
        self.model = BartForConditionalGeneration.from_pretrained('facebook/bart-large')
        
    def preprocess_text(self, text):
        """ Tokenizes and processes text data into sentences. """
        sentences = sent_tokenize(text)
        print("Preprocessed Sentences:", sentences)  # Debugging step
        return sentences

    def generate_questions(self, text, prompt, max_length=60, min_length=20, num_beams=4):
        """
        Generate questions from the given text and prompt.
        """
        # Preprocess the text into sentences
        sentences = self.preprocess_text(text)

        # Combine the text and the prompt
        combined_input = prompt + " " + " ".join(sentences)
        print("Combined Input:", combined_input)  # Debugging step

        # Tokenize the combined input
        inputs = self.tokenizer([combined_input], max_length=1024, return_tensors="pt", truncation=True)
        print("Tokenized Input IDs:", inputs['input_ids'])  # Debugging step

        # Generate questions using BART
        summary_ids = self.model.generate(
            inputs['input_ids'],
            max_length=max_length,
            min_length=min_length,
            num_beams=num_beams,
            length_penalty=2.0,
            early_stopping=True
        )

        print("Generated IDs:", summary_ids)  # Debugging step

        # Decode the generated questions
        generated_text = self.tokenizer.decode(summary_ids[0], skip_special_tokens=True)
        print("Generated Text:", generated_text)  # Debugging step

        # Split the generated output into questions (assuming they end with '?')
        questions = [q.strip() + '?' for q in generated_text.split('.') if '?' in q]
        print("Generated Questions:", questions)  # Debugging step
        return questions

# Usage Example
if __name__ == "__main__":
    # Example web-scraped text data
    web_scraped_data = """
    Artificial intelligence (AI) is intelligence demonstrated by machines, in contrast to the natural intelligence displayed by humans and animals.
    Leading AI textbooks define the field as the study of "intelligent agents": any device that perceives its environment and takes actions that maximize its chance of successfully achieving its goals.
    Colloquially, the term "artificial intelligence" is often used to describe machines (or computers) that mimic cognitive functions such as learning and problem-solving.
    """

    # Define the prompt
    prompt = "Generate 5 questions about artificial intelligence."

    # Create an instance of the question generator
    question_generator = BartQuestionGenerator()

    # Generate questions from the web-scraped text
    questions = question_generator.generate_questions(web_scraped_data, prompt)

    # Print the generated questions
    if questions:
        for idx, question in enumerate(questions, 1):
            print(f"Question {idx}: {question}")
    else:
        print("No questions were generated.")
