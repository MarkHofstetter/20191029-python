from Message import SMS, Email
# user = UserObject

sms = SMS()
sms.content = "Hallo Welt"
sms.recipient = 'Eva'
print("recipient", sms.recipient)
sms.send()
print(sms)


email = Email()
email.content = "Hallo Email Welt"
# email.subject = "Hallo"
email.recipient = "Tom"
email.send()

print(SMS.at_int_dial())

