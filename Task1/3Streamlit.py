from datetime import datetime
import re
import random
import streamlit as st

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

st.title("Mischievous Text Transformer")

user_input=st.text_area("Enter text to transform:", height=100)

if st.button("Transform Text!", type="primary"):
    if user_input:
        transformed=transform_text(user_input)
        
        st.write("Transformed:")
        st.code(transformed,language="text")

        st.write("1. Phone Number redaction: numbers->[REDACTED]")
        st.write("2. Date formatting")
        st.write("3. Python and Java replacement: Python->🐍, Java->☕")
        st.write("4. Replace all spaces with '-'")
        st.write("5. Implemented Random casing")
    else:
        st.warning("Please enter some text")