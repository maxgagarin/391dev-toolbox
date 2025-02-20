## text_utils.py
# Набір корисних функцій для обробки тексту
def capitalize_words(text):
    return ' '.join(word.capitalize() for word in text.split())

def reverse_string(text):
    return text[::-1]

if __name__ == "__main__":
    print(capitalize_words("hello world"))  # Hello World
    print(reverse_string("hello")) 
