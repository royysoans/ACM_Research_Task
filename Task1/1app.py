from datetime import datetime
import re
import random

def Randomcase(word: str) -> str:
    return "".join(random.choice([str.upper, str.lower])(c) for c in word)

def transform_text(text: str) -> str:
    phone_patterns=[r'\b\d{5}-\d{5}\b', r'\b\d{3}-\d{3}-\d{4}\b', r'\b\d{10}\b']
    for pattern in phone_patterns:
        text=re.sub(pattern, '[REDACTED]', text)
    
    words=text.split() #list of words
    new_words=[]
    date_formats=['%Y/%m/%d', '%Y/%d/%m', '%d/%m/%Y', '%m/%d/%Y', '%m/%d/%Y', '%d/%m/%Y', '%Y/%m/%d']
    
    for word in words:
        for fmt in date_formats:
            try:
                date_obj=datetime.strptime(word, fmt)
                word=date_obj.strftime("%d %B %Y")
                break
            except ValueError:
                continue

        if word.lower()=="python":
            word="🐍"
        if word.lower()=="java":
            word="☕"

        word=Randomcase(word)

        new_words.append(word) #new list will the transformed words

    text="-".join(new_words) #joins them with -
    return text


original="Hello,I am Royston, Today's date is 8/31/2006 , my phone number is +91 8369036325, In my opinion Python is better than Java ."
transformed=transform_text(original)
    
print(f"Transformed: {transformed}")
print(f"\nTransformations applied:")
print("1. Phone Number redaction: numbers->[REDACTED]")
print("2. Date formatting")
print("3. Python and Java replacement: Python -> 🐍 Java -> ☕")
print("4. Replace all spaces with -")
print("5. Implemented Random Casing")