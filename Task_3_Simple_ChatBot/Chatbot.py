def chatbot(name):
    print(f"Chatbot: Hello, {name}! I am a simple chatbot.")
    print(f"Chatbot:{name} You can say hello, ask how I am, or say bye to exit.")
    while True:
        user = input("You: ").strip().lower()
        if (user=="hi"  or user=="hello"):
            print(f"Chatbot: Hi! {name}")
        elif user=="how are you":
            print(f"Chatbot: I am fine, thanks! How are you {name}?")  
        elif user=="bye":
            print(f"Chatbot: Goodbye, {name}!")
            break
        else:
            print("Chatbot: Sorry! I don't understand.")    
name=input("Enter name")
chatbot(name) 
