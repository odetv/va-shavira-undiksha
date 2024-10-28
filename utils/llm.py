from openai import OpenAI
from langchain_groq import ChatGroq
from dotenv import load_dotenv
import os
from langchain_ollama import OllamaLLM


load_dotenv()
ollama_base_url = os.getenv('OLLAMA_BASE_URL')
openai_api_key = os.getenv('OPENAI_API_KEY')


def chat_ollama(question: str, model = "gemma2"):
    ollama = OllamaLLM(base_url=ollama_base_url, model=model, verbose=True)
    result = ollama.invoke(question)
    return result


def chat_openai(question: str, system_prompt: str, model = 'gpt-4o-mini'):
    try:
        client = OpenAI()
        completion = client.chat.completions.create(
            model=model,
            messages=[
                {"role": "system", "content": system_prompt},
                {
                    "role": "user",
                    "content": question
                }
            ],
            temperature=0.0
        )

        return completion.choices[0].message.content
    
    except Exception as e:
        print("Ada masalah dengan GPT")
        print("Ini errornya: ", e)



def chat_groq(question: str):
    groq = ChatGroq(
        model="gemma2-9b-it",
        max_tokens=None,
        timeout=None,
    )
    result = groq.invoke(question).content if hasattr(groq.invoke(question), "content") else groq.invoke(question)
    return result

