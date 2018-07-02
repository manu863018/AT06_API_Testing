class SMS_store:
    def __init__(self):
        self.my_inbox = {}
        self.messageId = 0


    def add_new_arrival(self, from_number, time_arrived, text_of_SMS):
        self.message = {"has_been_viewed": False,
                        "from_number": from_number,
                        "time_arrived": time_arrived,
                        "text_of_SMS": text_of_SMS}
        self.my_inbox[len(self.my_inbox) + 1] = self.message



    def message_count(self):
        return len(self.my_inbox)


    def get_unread_indexes(self):
        unreadMessages = []
        for messages in self.my_inbox:
            if not self.my_inbox[messages]["has_been_viewed"]:
                unreadMessages.append(messages)
        return unreadMessages


    def get_message(self, messageIndex):
        if messageIndex not in self.my_inbox:
            return None
        self.my_inbox[messageIndex]["has_been_viewed"] = True
        return self.my_inbox[messageIndex]


    def delete(self, messageIndex):
        del self.my_inbox[messageIndex]


    def clear(self):
        self.my_inbox.clear()


