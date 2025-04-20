import streamlit as st
import openai

st.set_page_config(page_title="MemeShastra - College Meme Generator", layout="centered")

st.title("🎓 MemeShastra")
st.subheader("College Life. Memeified. 😎")
st.markdown("---")

st.markdown("👋 **Describe your college moment or mood below:**")
user_input = st.text_area("Example: 'Boring 8am chemistry class after night out'")

if st.button("Generate Meme Caption 💥") and user_input:
    try:
        openai.api_key = st.secrets["OPENAI_API_KEY"]
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": "You are a witty and funny meme generator who only responds with hilarious meme-style one-liners for college students."},
                {"role": "user", "content": user_input}
            ]
        )
        meme = response.choices[0].message.content.strip()
        st.success("Here's your meme caption:")
        st.markdown(f"> *{meme}*")
    except Exception as e:
        st.error("Something went wrong while generating your meme. Please check your API key.")

st.markdown("---")
st.markdown("🔗 [Follow @waseem.diaries on Instagram](https://instagram.com/waseem.diaries) for more fun!")
st.markdown("💡 Made with ❤️ by MemeShastra")
