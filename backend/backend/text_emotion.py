from textblob import TextBlob

def detect_text_emotion(text):
    polarity = TextBlob(text).sentiment.polarity
    
    if polarity > 0:
        return "happy"
    elif polarity < 0:
        return "sad"
    else:
        return "neutral"

print(detect_text_emotion("I am very happy today"))