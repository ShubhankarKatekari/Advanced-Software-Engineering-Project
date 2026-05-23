from app.business_profile import BusinessProfile
from app.openai_service import OpenAIService
from app.response_formatter import ResponseFormatter


class BusinessChatbotFacade:
    def __init__(self, api_key):
        self.profile = BusinessProfile()
        self.ai_service = OpenAIService(api_key)
        self.formatter = ResponseFormatter()

    def answer_question(self, user_question):
        business_info = self.profile.get_summary()
        business_profile_text = self.profile.get_prompt_text()

        answer = self.ai_service.get_response(
            user_question,
            business_profile_text
        )

        return self.formatter.format_response(
            business_info["name"],
            answer
        )