def check_grammar(text, letter_combination):
    # Split the text into sentences
    sentences = text.split('.')

    results = []

    for sentence in sentences:
        # Split each sentence into words
        words = sentence.split()

        # Check if there are at least two words in the sentence
        if len(words) >= 1:
            last_word = words[-1].strip(".,!?")

            # Check if the last two letters of the last word match the specified letter combination
            if last_word[-2:].lower() == letter_combination.lower():
                results.append("Correct Grammar")
            else:
                results.append("Incorrect Grammar")
        else:
            # If there are no words in the sentence, it's considered incorrect grammar
            results.append("Incorrect Grammar")

    return results

def count_correct_grammar_sentences(english_text,letter_combination):
    # Check grammar using the previous code
    results = check_grammar(english_text,letter_combination)

    correct_grammar_count = results.count("Correct Grammar")
    incorrect_grammar_count = results.count("Incorrect Grammar")

    return correct_grammar_count, incorrect_grammar_count
# Example usage:
input_text = "I am a banana. Apples are red. Dogs are fun. The sky is blue."
letter_combination = "na"

results = check_grammar(input_text, letter_combination)
for i, sentence in enumerate(input_text.split('.')):
    print(f"Sentence {i + 1}: {sentence.strip()}")
    print(f"Grammar: {results[i]}\n")

correct_grammar_count, incorrect_grammar_count = count_correct_grammar_sentences(input_text,letter_combination)

print(f"Number of Correct Grammar Sentences: {correct_grammar_count}")
print(f"Number of Incorrect Grammar Sentences: {incorrect_grammar_count - 1}")