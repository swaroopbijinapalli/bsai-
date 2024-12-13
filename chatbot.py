# Basic Chatbot in Python

def chatbot():
    print("Chatbot: Hi there! I'm a simple chatbot. Type 'bye' to exit.")
    
    while True:
        user_input = input("You: ").lower()
        
        if user_input == 'bye':
            print("Chatbot: Goodbye! Have a great day!")
            break
        elif 'hello' in user_input or 'hi' in user_input:
            print("Chatbot: Hello! How can I assist you today?")
        elif 'your name' in user_input:
            print("Chatbot: I'm Chatbot, your virtual assistant!")
        elif 'weather' in user_input:
            print("Chatbot: Sorry, I can't check the weather yet. But it's always sunny when we chat!")
        else:
            print("Chatbot: I'm not sure how to respond to that. Can you try asking something else?")

# Run the chatbot
if _name_ == "_main_":
    chatbot()
