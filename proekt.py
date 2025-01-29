import streamlit as st
from openai import OpenAI
#import os

#HugginFace_Token = os.getenv("HugginFace_Token")


client = OpenAI(
	base_url="https://api-inference.huggingface.co/v1/",
	api_key="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"
    #api_key=HugginFace_Token 
)

zapros=st.text_input("Введите запрос", "Напиши сказку про кота")

messages = [
	{
		"role": "user",
		"content": zapros
	}
]

completion = client.chat.completions.create(
    model="mistralai/Mistral-Nemo-Instruct-2407", 
	messages=messages, 
	max_tokens=500
)

st.title("Генерация текста")
st.write(f"Текст: {completion.choices[0].message}")