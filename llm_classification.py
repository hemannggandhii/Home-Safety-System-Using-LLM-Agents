from langchain_openai import ChatOpenAI
import os

api_key = os.getenv('OPENAI_API_KEY', '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')  # Replace with your actual key or ensure the variable is set in your environment

llm = ChatOpenAI(model_name='gpt-3.5-turbo', openai_api_key=api_key)
def classify_activity(description):
    prompt = (
        f"You are a home security system expert. Classify activities detected by a motion sensor as "
        f"either 'normal' or 'suspicious'.\n\n"
        f"Activity description: {description}\n\n"
        f"Classify this activity with a single word: 'normal' or 'suspicious'."
    )

    print(f"Prompt sent to LLM: {prompt}")  

    response = llm.generate(prompt)  
    print(f"Raw LLM Response: {response.generations[0][0].text}")  
    raw_response = response.generations[0][0].text.strip().lower()

    if "suspicious" in raw_response:
        return "suspicious"
    elif "normal" in raw_response:
        return "normal"
    else:
        return "undetermined"


