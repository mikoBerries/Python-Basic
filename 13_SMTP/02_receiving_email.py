# grapping email from out email in gmail
import imaplib
import getpass
import email

# Setting object
M = imaplib.IMAP4_SSL('imap.gmail.com') 

user = input("Enter your email: ")
# Remember , you may need an app password if you are a gmail user
# 
password = getpass.getpass("Enter your password: ") 
M.login(user,password)

# M.list() - >all thing wes can check and use
# 
# ('OK',
#  [b'(\\HasNoChildren) "/" "INBOX"',
#   b'(\\HasNoChildren) "/" "Personal"',
#   b'(\\HasNoChildren) "/" "Receipts"',
#   b'(\\HasNoChildren) "/" "Sent"',
#   b'(\\HasNoChildren) "/" "Trash"',
#   b'(\\HasNoChildren) "/" "Travel"',
#   b'(\\HasNoChildren) "/" "Work"',
#   b'(\\HasChildren \\Noselect) "/" "[Gmail]"',
#   b'(\\All \\HasNoChildren) "/" "[Gmail]/All Mail"',
#   b'(\\Drafts \\HasNoChildren) "/" "[Gmail]/Drafts"',
#   b'(\\HasNoChildren \\Important) "/" "[Gmail]/Important"',
#   b'(\\HasNoChildren \\Sent) "/" "[Gmail]/Sent Mail"',
#   b'(\\HasNoChildren \\Junk) "/" "[Gmail]/Spam"',
#   b'(\\Flagged \\HasNoChildren) "/" "[Gmail]/Starred"',
#   b'(\\HasNoChildren \\Trash) "/" "[Gmail]/Trash"'])

# Connect to your inbox
M.select("inbox")


# Use if you get an error saying limit was reached
imaplib._MAXLINE = 10000000

# Search Subject "this is a test email for python"
# string structure are `target "things you want to search"`
typ ,data = M.search(None,'SUBJECT "this is a test email for python"')

result, email_data = M.fetch(data[0],"(RFC822)")
raw_email = email_data[0][1]
raw_email_string = raw_email.decode('utf-8')


# Cleaning raw data coming from imaplib 
email_message = email.message_from_string(raw_email_string)
for part in email_message.walk():
    if part.get_content_type() == "text/plain":
        body = part.get_payload(decode=True)
        print(body)