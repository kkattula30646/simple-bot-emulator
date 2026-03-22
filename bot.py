from botbuilder.core import ActivityHandler, TurnContext
from botbuilder.schema import ChannelAccount


class SimpleBot(ActivityHandler):
    async def on_members_added_activity(
        self, members_added: [ChannelAccount], turn_context: TurnContext
    ):
        for member in members_added:
            if member.id != turn_context.activity.recipient.id:
                await turn_context.send_activity(
                    "Hello and welcome! Type 'help' to see what I can do."
                )

    async def on_message_activity(self, turn_context: TurnContext):
        text = (turn_context.activity.text or "").strip().lower()

        if text in ["hello", "hi", "hey"]:
            reply = "Hello simple bot"
        elif text == "help":
            reply = (
                "I can help with:\n"
                "- hello\n"
                "- help\n"
                "- hours\n"
                "- services\n"
                "- contact\n"
                "- bye"
            )
        elif text == "hours":
            reply = "Office hours are Monday through Friday, 9:00 AM to 5:00 PM."
        elif text == "services":
            reply = "I provide information about advising, registration, and technical support."
        elif text == "contact":
            reply = "Contact student support at support@university.edu or call 555-123-4567."
        elif text in ["bye", "exit", "quit"]:
            reply = "Goodbye! Have a great day."
        elif text == "":
            reply = "You entered an empty message. Type 'help' to see available commands."
        else:
            reply = "Sorry, I did not understand that. Please type 'help' to see available commands."

        await turn_context.send_activity(reply)