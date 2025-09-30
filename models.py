import os
from openai import OpenAI
from dotenv import load_dotenv
from pprint import pprint

load_dotenv()

class ModelWrapper:
    def __init__(self):
        # TODO: Create OpenAI client that points to OpenRouter
        # Hint: You need to set a custom base_url
        # OpenRouter URL: "https://openrouter.ai/api/v1"
        
        # TODO: Define which models you want to use
        # Here are some options:
        # "openai/gpt-4o-mini" - OpenAI (cheap)
        # "anthropic/claude-3-haiku" - Anthropic (cheap) 
        # "google/gemini-flash-1.5" - Google (cheap)
        # "qwen/qwen-2-7b-instruct" - Free!
        # "meta-llama/llama-3-8b-instruct" - Meta
        
        api_key = os.getenv("OPENROUTER_API_KEY")

        self.client = OpenAI(base_url="https://openrouter.ai/api/v1", api_key=api_key)
        self.models = ["openai/gpt-4o-mini",
                       "anthropic/claude-3-haiku",
                       "google/gemini-2.0-flash-001",
                       "x-ai/grok-4-fast:free"]

    def query_model(self, prompt, system_prompt="You are a helpful assistant, think step by step and then answer the request", model="openai/gpt-4o-mini"):
        """
        Send a prompt to any AI model and get back a response
           
        Think about:
            - How do you make an API call?
            - What parameters do you need?
            - What happens when things go wrong?
            - How do you keep responses short for the workshop?
        """
        # TODO: Implement the API call
        # Hint: Use self.client.chat.completions.create()
        try:
            messages = [
                {"role": "system", "content": system_prompt},
                {"role": "user", "content": prompt}
                ]

            response = self.client.chat.completions.create(
                model = model,
                messages = messages,
                max_tokens = 500
            )

            return response.choices[0].message.content
        except Exception as e:
            return f"Error: {e}"
        
    def get_available_models(self):
        """Return a list of model names students can use"""
        # TODO: Return list of your available models
        return self.models
        
    def test_connection(self):
        """Quick test to see if your setup works"""
        # TODO: Try a simple API call and return True/False
        return self.client is not None

def test_models():
    m = ModelWrapper()
    print("Cliente inicializado: ", m.test_connection())
    print("Modelos disponibles: ", m.get_available_models(), "\n")

    respuesta = m.query_model("Hola, me podrias decir cuanto es la raiz de 2 aproximadamente?")
    print(respuesta)

def test_all_models():
    m = ModelWrapper()
    print("Cliente inicializado: ", m.test_connection())
    print("Modelos disponibles: ", m.get_available_models(), "\n")

    all_respuestas = {}
    prompt = "Hola, me podrias decir cuanto es la raiz de 2 aproximadamente?"
    for model in m.models:
        respuesta = m.query_model(prompt=prompt, model=model)
        all_respuestas[model]=respuesta
    pprint(all_respuestas)


#test_models()
#test_all_models()