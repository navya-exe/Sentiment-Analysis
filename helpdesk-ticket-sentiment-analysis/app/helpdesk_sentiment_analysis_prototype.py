import streamlit as st
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer
import speech_recognition as sr

def main():
    st.title("Speech to Sentiment Analyzer")
    
    if st.button("Record"):
        analyze_sentiment()

def analyze_sentiment():
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        st.text('Clearing background noise...')
        recognizer.adjust_for_ambient_noise(source, duration=1)
        st.text('Waiting for your message...')
        recordedaudio = recognizer.listen(source)
        st.text('Done recording..')

    text = ""  # Initialize the text variable
    try:
        st.text('Printing the message..')
        text = recognizer.recognize_google(recordedaudio, language='en-US')
        st.text('Your message: {}'.format(text))
    except Exception as ex:
        st.text(str(ex))

    # Sentiment analysis
    Sentence = str(text)
    analyser = SentimentIntensityAnalyzer()
    v = analyser.polarity_scores(Sentence)
    
    # Map sentiment labels
    sentiment_labels = {
        'pos': 'Positive',
        'neg': 'Negative',
        'neu': 'Neutral',
    }
    
    # Determine the sentiment with the highest probability
    sentiment = max(v, key=lambda k: v[k])
    
    # Define emojis for each sentiment
    emojis = {
        'pos': '😄',  # Positive sentiment
        'neg': '😞',  # Negative sentiment
        'neu': '😐',  # Neutral sentiment
    }
    
    # Display the sentiment in bold and with a higher font size
    st.markdown(f'<p style="font-size: 40px; font-weight: bold;">This is {sentiment_labels[sentiment]} {emojis[sentiment]}</p>', unsafe_allow_html=True)

if __name__ == "__main__":
    main()