import ollama

def chat():
    model_name = "stablelm-zephyr" 
    print("Welcome to the AI Chatbot! Type 'exit' to end the conversation.")

    while True:
        user_input = input("You: ")
        if user_input.lower() == "exit":
            print("Goodbye!")
            break
        
   
        response = ollama.generate(model=model_name, prompt=user_input)
        
       
        if 'response' in response:
            print(f"AI: {response['response']}")
        else:
            print("AI: Sorry, I didn't understand that response.")

if __name__ == "__main__":
    chat()
