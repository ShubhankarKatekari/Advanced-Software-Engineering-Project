from app.chatbot_facade import BusinessChatbotFacade


def main():
    chatbot = BusinessChatbotFacade()

    print("AI Front Desk Assistant")
    print("Type a question or type 'exit' to close the application.")

    while True:
        user_question = input("You: ")

        if user_question.lower() == "exit":
            print("Closing AI Front Desk Assistant.")
            break

        response = chatbot.answer_question(user_question)
        print(response)


if __name__ == "__main__":
    main()
