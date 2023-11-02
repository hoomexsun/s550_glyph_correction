# s550_glyph_correction 🏁

Glyph Font s-550 used along with srilipi for typing Bengali/Bangla script in Meiteilon is not unicode compatible. This project makes it possible to correct the glyphs into unicode compatible. Also includes resources.

🏁 This repository is fully developed!

## 1. Testing

Run `main.py` and check `data/`

## 2. Testing with custom input

1. Put file containing the s550 script or utterance in data directory
2. Run `main.py`

Output is in `data/output.txt`

## 3. Use as Module

Clone `src` folder in your `main_project/src` and rename it to your choice, say `glyph_correction`.

Then, Import and create `MMTransliteration` class from `glyph_correction` and call `correct()` , `correct_script()` or `correct_utterances()`

```python
# From a python file inside main_project/src
from glyph_correction import GlyphCorrection

gc = GlyphCorrection()

# 1. Correct s550 string
output_1 = gc.correct("<your-input-here>")

# 2. Correct s550 script
output_2 = gc.correct_script("<your-file-here>")

# 3. Correct s550 utterances
output_3 = gc.correct_utterances("<your-utterance-file-here>")

```

## 4. Generating wordmap

You can generate wordmap of your word list as follows

1. Put your `words.txt` inside `data`.
2. From `main.py`, write a function referring to `generate_wordmap` function and `main` function.
3. Run it.

Writing Wordmap file in text format, json format and csv format are all included as utility functions.

Refer `src/utils/file.py`

## 5. Correcting files in bulk

Put all files inside a directory say `data/inputs/` and write as

```python
from src.utils.dir

input_dir = "data/inputs
gc = GlyphCorrection()
process_directory(gc.correct, dir=input_dir)
```

Output files will be inside `data/output`

## 6. Script mode

usage: script.py [-h] [-f | -d] input_string

Converts s-550 glyphs into correct Bengali Unicode characters

positional arguments:
input_string Input string to correct

options:
-h, --help show this help message and exit
-f, --file Input is a file name
-d, --dir Input is a directory

## See also

- [Speech Dataset](https://github.com/hoomexsun/speech_dataset).
- [Meetei/Meitei Mayek Transliteration](https://github.com/hoomexsun/mm_transliteration).
- [Meetei/Meitei Mayek Keyboard for Windows](https://github.com/hoomexsun/mm_keyboard).
- [IPA Keyboard for Windows](https://github.com/hoomexsun/ipa_keyboard).
- [S-550 Glyph Correction](https://github.com/hoomexsun/s550_glyph_correction).
- [Epaomayek Glyph Correction](https://github.com/hoomexsun/epaomayek_glyph_correction).
