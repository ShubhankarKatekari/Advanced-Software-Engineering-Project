class BusinessProfile:
    def __init__(self):
        self.name = "BrightCare Dental"
        self.hours = "Monday to Friday, 9:00 AM to 5:00 PM"
        self.phone = "(555) 123-4567"
        self.location = "123 Main Street, Orlando, FL"

    def get_summary(self):
        return {
            "name": self.name,
            "hours": self.hours,
            "phone": self.phone,
            "location": self.location
        }
