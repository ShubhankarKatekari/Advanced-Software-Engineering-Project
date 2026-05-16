class FAQData:
    def __init__(self):
        self.answers = {
            "hours": "We are open Monday to Friday from 9:00 AM to 5:00 PM.",
            "location": "We are located at 123 Main Street, Orlando, FL.",
            "appointment": "To schedule an appointment, please call (555) 123-4567.",
            "insurance": "We accept most major dental insurance plans. Please call the office to confirm your coverage.",
            "services": "We provide dental cleanings, exams, fillings, whitening, and appointment support.",
            "phone": "You can call us at (555) 123-4567."
        }

    def find_answer(self, user_question):
        question = user_question.lower()

        for keyword, answer in self.answers.items():
            if keyword in question:
                return answer

        return "I am sorry, I do not have that information yet. Please contact the front desk for help."