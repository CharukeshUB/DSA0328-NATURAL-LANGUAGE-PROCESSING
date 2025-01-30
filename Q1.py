#1
import re
text = "The quick brown fox jumps over the lazy dog on 2025-01-29."
pattern1 = r'\bb\w+n\b'
match1 = re.findall(pattern1, text)
print(f"Words starting with 'b' and ending with 'n': {match1}")
pattern2 = r'\b\d{4}-\d{2}-\d{2}\b'
match2 = re.search(pattern2, text)
if match2:
    print(f"Date found: {match2.group()}")
else:
    print("No date found")
pattern3 = r'\b\w{3}\b'
match3 = re.findall(pattern3, text)
print(f"Three-letter words: {match3}")
pattern4 = r'^The'
match4 = re.match(pattern4, text)
if match4:
    print("The text starts with 'The'")
else:
    print("The text does not start with 'The'")
pattern5 = r'[aeiouAEIOU]'
match5 = re.findall(pattern5, text)
print(f"All vowels in the text: {match5}")
