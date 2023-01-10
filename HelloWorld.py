with open("email.txt", "r") as emails:
    emails = emails.readlines()

print(emails)
for email in emails:
    if "gmail" in email:
        print(email.rstrip())    
    
    