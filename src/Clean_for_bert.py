def clean_for_bert(text):
    import re
    text = text.lower()
    text = re.sub(r"http\S+|www\S+", "", text)    # link
    text = re.sub(r"@\w+", "", text)              # mention
    text = re.sub(r"#", "", text)                 # remove #, but keep the word
    text = re.sub(r"\s+", " ", text).strip()      # extra spaces
    return text