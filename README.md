# 🔐 Custom Text Encryption & Decryption Tool (Python)

This project provides a simple yet powerful **custom encryption and decryption system** written in Python.  
The script reads text from an input file, encrypts each word with randomized logic, and writes the encrypted output.  
It can also reverse the encryption and restore the original text.

---

## 🚀 Features

### ✔ Randomized Encryption
- Random shift key between **5 and 20** for every word.
- Shift value converted into a letter (A = 1, B = 2, ...).
- Random index marker inserted at the beginning of each encrypted word.
- Supports:
  - Uppercase letters  
  - Lowercase letters  
  - Numbers  
  - Special characters (kept unchanged)

### ✔ Accurate Decryption
- Correctly extracts the shift key and index marker.
- Reverses shifts to reconstruct each original word.
- Produces exact original text in `decrypted_output.txt`.

### ✔ File-Based Workflow
- Reads from **input.txt**
- Writes encrypted data to **encrypted_output.txt**
- Writes decrypted data to **decrypted_output.txt**

### ✔ Performance Tracking
- Displays encryption/decryption execution time.

---

## 📂 File Structure

