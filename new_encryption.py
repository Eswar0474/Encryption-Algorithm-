import random
import time
def en():
    start_time = time.time()
    input_file="input.txt"
    output_file="encrypted_output.txt"
    with open(input_file, 'r', encoding='utf-8') as f:
        lines = f.readlines()
    
    encrypted_lines = []
    
    for line in lines:
        words = line.strip().split()
        encrypted_words = []
        
        for word in words:
            if len(word) < 2:
                encrypted_words.append(word)
                continue
            
            shift = random.randint(5, 20)  # Random shift key
            shift_letter = chr(shift + ord('A') - 1)# Convert shift value to a letter
            
            
            pos = random.randint(1, len(word) - 1)  # Ensure valid position (not first character)
            
            # Randomly decide uppercase/lowercase for index marker
            index_marker = chr(pos + ord('A')) if random.randint(1, 100) % 2 == 0 else chr(pos + ord('a'))
            encrypted_word = ""
            for i, char in enumerate(word):
                if char.isupper():
                    shifted_char = chr(((ord(char) - ord('A') + shift) % 26) + ord('A'))
                    encrypted_word += shifted_char
                elif char.islower():
                    shifted_char = chr(((ord(char) - ord('a') + shift) % 26) + ord('a'))
                    encrypted_word += shifted_char
                elif char.isdigit():
                    encrypted_word += str((int(char) + shift) % 10)
                else:
                    encrypted_word += char
            
            # Insert shift key and position marker
            encrypted_word =index_marker + encrypted_word[:pos] + shift_letter + encrypted_word[pos:]
            encrypted_words.append(encrypted_word)
        
        encrypted_lines.append(' '.join(encrypted_words) + '\n')
    
    with open(output_file, 'w', encoding='utf-8') as f:
        f.writelines(encrypted_lines)
    end_time = time.time()  # End the timer
    elapsed_time = end_time - start_time
    print(f"Execution Time: {elapsed_time:.6f} seconds")

def de():
    start_time = time.time()
    input_file="encrypted_output.txt"
    output_file="decrypted_output.txt"
    with open(input_file, 'r', encoding='utf-8') as f:
        encrypted_lines = f.readlines()
    
    decrypted_lines = []
    
    for line in encrypted_lines:
        encrypted_words = line.strip().split()
        decrypted_words = []
        
        for encrypted_word in encrypted_words:
            if len(encrypted_word) < 2:  # Avoid errors if too short
                decrypted_words.append(encrypted_word)
                continue
            
            # Extract shift key and index marker
            shift_letter, index_marker = '', ''
            e=encrypted_word[0]

            if e.isupper():
                pos = ord(e) - ord('A') +1
            else:
                pos = ord(e) - ord('a') +1

            shift_letter=encrypted_word[pos]

            
            shift = ord(shift_letter) - ord('A') + 1  # Convert shift key back to number

            

            
            # Remove shift key and index marker
            encrypted_word = encrypted_word[1:pos] + encrypted_word[pos+1:]  

            decrypted_word = ""
            for char in encrypted_word:
                if char.isupper():
                    shifted_char = chr(((ord(char) - ord('A') - shift + 26) % 26) + ord('A'))
                    decrypted_word += shifted_char
                elif char.islower():
                    shifted_char = chr(((ord(char) - ord('a') - shift + 26) % 26) + ord('a'))
                    decrypted_word += shifted_char
                elif char.isdigit():
                    decrypted_word += str((int(char) - shift) % 10)
                else:
                    decrypted_word += char
            decrypted_words.append(decrypted_word)

        
        decrypted_lines.append(' '.join(decrypted_words) + '\n')
    
    with open(output_file, 'w', encoding='utf-8') as f:
        f.writelines(decrypted_lines)
    end_time = time.time()  # End the timer
    elapsed_time = end_time - start_time
    print(f"Execution Time: {elapsed_time:.6f} seconds")
# Example usage
