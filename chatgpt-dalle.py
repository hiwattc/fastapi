import streamlit as st
import openai 
openai.api_key=st.secrets["api_key"]

st.title("ChatGTP Plus DALL-E")
with st.form("form"):
    user_input = st.text_input("Prompt")
    user_size = st.selectbox("Size",["1024x1024","512x512","256x256"])
    submit = st.form_submit_button("Submit")

if submit and user_input:
    gpt_prompt = [{
        "role":"system",
        "content":"Imagine the detail appearance of the input. Response it shortly."
    }]

    gpt_prompt.append({
        "role":"user",
        "content":user_input
    })
    
    with st.spinner("Waiting for ChatGPT..."):
        gpt_responese = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=gpt_prompt
        )

    prompt = gpt_responese["choices"][0]["message"]["content"]
    st.write(prompt)

    with st.spinner("Drawing image with dalle...wait...please..."):
        dalle_response=openai.Image.create(
            prompt=prompt,
            size=user_size
        )
        st.image(dalle_response["data"][0]["url"])