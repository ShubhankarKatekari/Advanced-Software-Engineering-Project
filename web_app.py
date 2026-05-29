import os
import sys
from flask import Flask, render_template, request, session
from dotenv import load_dotenv
from app.chatbot_facade import BusinessChatbotFacade


load_dotenv()

OPENAI_API_KEY = os.getenv("OPENAI_API_KEY", "")


def resource_path(relative_path):
    """Get correct path for development and PyInstaller executable."""
    try:
        base_path = sys._MEIPASS
    except AttributeError:
        base_path = os.path.abspath(".")

    return os.path.join(base_path, relative_path)


app = Flask(
    __name__,
    template_folder=resource_path("templates"),
    static_folder=resource_path("static")
)

app.secret_key = "simple-course-secret-key"

chatbot = BusinessChatbotFacade(OPENAI_API_KEY)


@app.route("/", methods=["GET", "POST"])
def index():
    response = None
    error = None
    user_question = ""
    show_history = False

    conversation = session.get("conversation", [])

    if request.method == "POST":
        action = request.form.get("action", "")

        if action == "clear_history":
            session.pop("conversation", None)
            conversation = []
            response = "Conversation history has been cleared."

        elif action == "view_history":
            show_history = True

        else:
            user_question = request.form.get("question", "").strip()

            if not user_question:
                error = "Please enter a question before submitting."
            else:
                response = chatbot.answer_question(user_question)

                conversation.append({
                    "question": user_question,
                    "answer": response
                })

                session["conversation"] = conversation

    return render_template(
        "index.html",
        response=response,
        error=error,
        user_question=user_question,
        conversation=conversation,
        show_history=show_history
    )


if __name__ == "__main__":
    app.run(debug=False)