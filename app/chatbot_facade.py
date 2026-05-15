from app.business_profile import BusinessProfile
from app.faq_data import FAQData
from app.response_formatter import ResponseFormatter


class BusinessChatbotFacade:
    def __init__(self):
        self.profile = BusinessProfile()
        self.faq_data = FAQData()
        self.formatter = ResponseFormatter()

    def answer_question(self, user_question):
        business_info = self.profile.get_summary()
        answer = self.faq_data.find_answer(user_question)
        return self.formatter.format_response(business_info["name"], answer)
