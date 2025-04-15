import streamlit as st
from predict import predict_sentiment
from absa import analyze_aspects_vader  # your ABSA function

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
        st.subheader("🧠 Overall Sentiment:")
        st.success(overall)

        # Aspect-Based Sentiment
        aspects = analyze_aspects_vader(review)
        if aspects:
            st.subheader("🔍 Aspect-Based Sentiment:")
            for asp, sentiment in aspects.items():
                emoji = "✅" if sentiment == "Positive" else "❌" if sentiment == "Negative" else "⚪"
                st.write(f"{emoji} **{asp}**: {sentiment}")
        else:
            st.info("No aspects found in the review.")
