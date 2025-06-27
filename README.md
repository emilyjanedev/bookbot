# 📚 BookBot

**BookBot** is a simple Python program that:

- Takes in the path to a `.txt` file of a book
- Counts and reports how many words are in the book
- Counts and reports how many times each alphabetical character appears

---

## 🚀 How to Run BookBot

1. Clone this repository to your local machine:

   ```bash
   git clone https://github.com/emilyjanedev/bookbot.git
   cd bookbot
   ```

2. Run the program from your terminal:
   `bash python3 main.py <path_to_book>`

   Replace `<path_to_book>` with the relative or absolute path to your `.txt` file.

   For example:
   `bash python3 main.py books/frankenstein.txt`

## 🛠 Requirements

- Python 3.x

No additional packages or dependencies required.

## 📝 Example Output

```
============ BOOKBOT ============
Analyzing book found at books/prideandprejudice.txt...
----------- Word Count ----------
Found 130410 total words
--------- Character Count -------
e: 74451
t: 50837
a: 44834
...
z: 971
============= END ===============
```
