# s550_glyph_correction 🏁

Srilipi and the Glyph Font s-550, which were utilized to type the Bengali/Bangla script in Meiteilon, are incompatible with Unicode. This project facilitates the conversion of glyphs to unicode characters. Resources are included as well.

🏁 This repository is fully developed!

## 1. Testing

Run `main.py` and check `data/`

## 2. Testing with custom input

1. Put file containing the s550 script or utterance in data directory
2. Run `main.py`

Output is in `data/output.txt`

## 3. Use as Module

Clone `src` folder in your `main_project/src` and rename it to your choice, say `glyph_correction`.

Then, Import and create `GlyphCorrection` class from `glyph_correction` and call `correct()` , `correct_script()` or `correct_utterances()`

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
# From a python file inside main_project/src
from glyph_correction import GlyphCorrection
from src.utils.dir import process_directory

input_dir = "data/inputs"
gc = GlyphCorrection()

# For normal files
process_directory(gc.correct_script, dir=input_dir)

# For utterance files
process_directory(gc.correct_utterances, dir=input_dir)
```

Output files will be inside `data/outputs`

## 6. Script mode

usage: script.py [-h] [-f | -d] input_string

Converts s-550 glyphs into correct Bengali Unicode characters

positional arguments:
input_string Input string to correct

options:

1. -h, --help show this help message and exit
2. -f, --file Input is a file name
3. -d, --dir Input is a directory

## 7. Algorithm 🚧

Yet to be written!

## See also

- [Speech Dataset](https://github.com/hoomexsun/speech_dataset).
- [Meetei/Meitei Mayek Transliteration](https://github.com/hoomexsun/mm_transliteration).
- [Meetei/Meitei Mayek Keyboard for Windows](https://github.com/hoomexsun/mm_keyboard).
- [IPA Keyboard for Windows](https://github.com/hoomexsun/ipa_keyboard).
- [S-550 Glyph Correction](https://github.com/hoomexsun/s550_glyph_correction).
- [Epaomayek Glyph Correction](https://github.com/hoomexsun/epaomayek_glyph_correction).
