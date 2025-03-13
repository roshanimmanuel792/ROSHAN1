def create_alphabet_file(n, filename='alphabet.txt'):
    import string
    
    alphabet = string.ascii_uppercase
    with open(filename, 'w') as file:
        for i in range(0, len(alphabet), n):
            file.write(alphabet[i:i+n] + '\n')

# Sample input
n = 5
create_alphabet_file(n)




def read_first_n_lines(file_path, n):
    try:
        with open(file_path, 'r') as file:
            for _ in range(n):
                line = file.readline()
                if not line:
                    break
                print(line.strip())
    except FileNotFoundError:
        print(f"The file {file_path} does not exist.")
    except Exception as e:
        print(f"An error occurred: {e}")

# Sample usage
file_path = 'example.txt'
n = 5
read_first_n_lines(file_path, n)













from collections import Counter
import re

def count_word_frequency(file_path):
    try:
        with open(file_path, 'r') as file:
            text = file.read()
            # Remove punctuation and convert to lowercase
            words = re.findall(r'\b\w+\b', text.lower())
            word_count = Counter(words)
            for word, count in word_count.items():
                print(f"{word}: {count}")
    except FileNotFoundError:
        print(f"The file {file_path} does not exist.")
    except Exception as e:
        print(f"An error occurred: {e}")

# Sample usage
file_path = 'sample.txt'
count_word_frequency(file_path)
