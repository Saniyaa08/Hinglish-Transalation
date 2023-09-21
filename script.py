from translate import Translator

def translate_to_hinglish(text):
    translator = Translator(to_lang="hi")
    hinglish_text = translator.translate(text)
    return hinglish_text

if __name__ == "__main__":
    # Provide the English sentences for translation
    english_sentences = [
        "Definitely share your feedback in the comment section.",
        "So even if it's a big video, I will clearly mention all the products.",
        "I was waiting for my bag."
    ]

    # Translate each English sentence to Hinglish
    hinglish_sentences = [translate_to_hinglish(sentence) for sentence in english_sentences]

    # Print the Hinglish translations
    print("Translated Hinglish sentences:")
    for i, sentence in enumerate(hinglish_sentences, start=1):
        print(f"{i}. {sentence}")