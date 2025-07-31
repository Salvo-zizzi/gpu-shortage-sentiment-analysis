def extract_brand(text):
    text = text.lower()
    if 'nvidia' in text or 'rtx' in text or 'geforce' in text:
        return 'NVIDIA'
    elif 'amd' in text or 'radeon' in text:
        return 'AMD'
    elif 'intel' in text:
        return 'Intel'
    else:
        return 'Altro'

df['Brand'] = df['Text'].astype(str).apply(extract_brand)