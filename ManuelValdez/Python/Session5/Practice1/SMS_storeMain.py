from SMS_store import SMS_store

my_inbox = SMS_store()
my_inbox.add_new_arrival("123456789", "21:05", "test text 1")
my_inbox.add_new_arrival("987654310", "09:05", "test text 2")
my_inbox.add_new_arrival("147252836", "08:13", "test text 3")
my_inbox.add_new_arrival("916321587", "10:10", "test text 4")
print(my_inbox.message_count())
print(my_inbox.get_unread_indexes())
print(my_inbox.get_message(2))
print(my_inbox.get_unread_indexes())
my_inbox.delete(3)
print(my_inbox.get_unread_indexes())
my_inbox.clear()
print(my_inbox.get_unread_indexes())