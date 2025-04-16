import streamlit as st
from predict import predict_sentiment
from absa import analyze_aspects_vader  # your ABSA function
from emoji_analyzer import extract_emojis, map_emojis_to_emotions


st.set_page_config(page_title="IMDB Review Sentiment Analyzer", layout="centered")

st.title("🎬 IMDB Review Analyzer")
st.markdown("Analyze **overall sentiment** and **aspects** like Acting, Story, Visuals.")

# Input text
review = st.text_area("Enter a movie review:")

if st.button("Analyze"):
    if not review.strip():
        st.warning("Please enter a review.")
    else:
        # Overall sentiment
        overall = predict_sentiment(review, return_label=True)
        st.subheader(" Overall Sentiment:")
        st.success(overall)

        # Aspect-Based Sentiment
        aspects = analyze_aspects_vader(review)
        if aspects:
            st.subheader(" Aspect-Based Sentiment:")
            for asp, sentiment in aspects.items():
                emoji = "" if sentiment == "Positive" else "" if sentiment == "Negative" else ""
                st.write(f"{emoji} **{asp}**: {sentiment}")
        else:
            st.info("No aspects found in the review.")

# Emoji-based emotion detection
emojis_found = extract_emojis(review)
emotions = map_emojis_to_emotions(emojis_found)

if emojis_found:
    st.subheader(" Emoji-Based Emotions:")
    for emoji, emotion in zip(emojis_found, emotions):
        st.write(f"{emoji}: {emotion}")
else:
    st.info("No emojis detected.")

def generate_summary(overall_sentiment, aspect_sentiments, emojis_found, emotions):
    # Fallback if sentiment is None
    if not overall_sentiment:
        overall_sentiment = "Uncertain"

    summary = f" The review expresses an **{overall_sentiment.lower()}** overall sentiment.\n\n"

    if aspect_sentiments:
        aspect_lines = []
        for aspect, sentiment in aspect_sentiments.items():
            aspect_name = aspect.capitalize()
            if sentiment == "Positive":
                line = f" **{aspect_name}** was praised."
            elif sentiment == "Negative":
                line = f" **{aspect_name}** was criticized."
            else:
                line = f" **{aspect_name}** was mentioned, but the opinion was unclear."
            aspect_lines.append(line)
        summary += "\n".join(aspect_lines) + "\n\n"

    if emojis_found:
        emoji_lines = [f"{emoji} → *{emotion}*" for emoji, emotion in zip(emojis_found, emotions)]
        summary += " Emoji analysis: " + ", ".join(emoji_lines) + "."

    return summary

