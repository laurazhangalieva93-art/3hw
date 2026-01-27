email = {
    "subject": "Everyweekly meeting",
    "from": "Laurazhangaliyeva@gmail.com",
    "to": "Kimnastya@gmail.com",
    "body": "Hello!\n\tI want to announce the meeting on Wednesday.\n\tPlease review and let me know your feedback."
}
from datetime import date
send_date = str(date.today())
email["date"] = send_date
print(email)

email ["from"] = email["from"].strip().lower()
print(email)

email ["to"] = email["to"].strip().lower()
print(email)

login, domain = email["from"].split("@")
print(login)
print(domain)

email["short_body"] = email["body"][:10] + "..."
print(email["short_body"])
