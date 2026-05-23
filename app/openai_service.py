from openai import OpenAI


class OpenAIService:
    def __init__(self, api_key):
        if api_key == "":
            self.client = None
        else:
            self.client = OpenAI(api_key=api_key)

    def get_response(self, user_question, business_profile):
        if self.client is None:
            return (
                "The OpenAI API key has not been added yet. "
                "Please add the API key to the .env file."
            )

        instructions = (
            "You are a helpful front desk assistant for a business.\n"
            "Use only the business profile below to answer the user.\n"
            "Do not make up services, hours, prices, policies, or contact details.\n"
            "If the answer is not in the business profile, politely tell the user "
            "to contact the business directly.\n"
            "Keep the answer short, clear, and professional.\n\n"
            "Business Profile:\n"
            f"{business_profile}"
        )

        try:
            result = self.client.responses.create(
                model="gpt-4o-mini",
                input=[
                    {
                        "role": "system",
                        "content": instructions
                    },
                    {
                        "role": "user",
                        "content": user_question
                    }
                ]
            )

            return result.output_text

        except Exception:
            return (
                "Sorry, the assistant could not respond right now. "
                "Please try again later or contact the front desk directly."
            )