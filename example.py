from util.ai_client import chat_completion_request
from util.memory import SlidingWindowMemory

model = "deepseek-coder-6.7b-instruct"
memory = SlidingWindowMemory(window_size=5)  # Adjust as needed

def deepseek_predict(prompt: str):
    """Generates a response using DeepSeek with memory support."""
    
    # Add user message to memory
    memory.add_message("user", prompt)

    # Retrieve conversation history
    messages = memory.get_memory()

    # Call DeepSeek API
    response = chat_completion_request(model, messages)
    
    # Extract and store assistant's response
    response_content = response["choices"][0]["message"]["content"]
    memory.add_message("assistant", response_content)

    return response_content

# Main interaction loop
while True:
    inputprompt = input("\nEnter your question (or type 'exit' to quit): ")
    
    if inputprompt.lower() == "exit":
        print("Exiting...")
        break

    response = deepseek_predict(inputprompt)

    print("\n====== Model response =====\n")
    print(response)
