#20.1
msg1 = 'Привет'
msg2 = 'Пока'
msg3 = 'Зачем ты это читаешь?'
msgs = [msg1,msg2,msg3]
def show_message():
    for msg in msgs:
        return msgs
print(show_message())
#20.2
def send_messages(messages):
    sent_messages = []
    while messages:
            message = messages.pop(0)
            print(f'Отправлено сообщение: {message}')
            sent_messages.append(message)
    return sent_messages
msg1 = 'Привет'
msg2 = 'Пока'
msg3 = 'Зачем ты это читаешь?'
messages = [msg1,msg2,msg3]
sent_messages = send_messages(messages)
print('Исходные сообщения', messages)
print('Отправленные сообщения', sent_messages)
#20.3
def send_messages(message):
    copy = []
    copy.extend(messages)
    return copy
msg1 = 'Привет'
msg2 = 'Пока'
msg3 = 'Зачем ты это читаешь?'
messages = [msg1,msg2,msg3]
copy = send_messages(messages)
print('Копированный список:', copy)
print('Исходный список:', messages)