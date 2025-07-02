import ollama

print("Offline LLM Test")
input=input("Enter your question for the LLM: ")
try:
    response = ollama.chat(
        model='mistral',
        messages=[{"role": "user", "content": input}]
    )
    print(response['message']['content'])
except Exception as e:
    print(f"An error occured: {e}")
    print("Please ensure the Ollama application us running.")