import math

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

email["from"] = email["from"].strip().lower()
print(email)

email["to"] = email["to"].strip().lower()
print(email)

login, domain = email["from"].split("@")
print(login)
print(domain)

email["short_body"] = email["body"][:10] + "..."
print(email["short_body"])

personal_domeins = [
    "gmail.com",
    "list.ru",
    "yahoo.com",
    "outlook.com",
    "hotmail.ru",
    "icloud.com",
    "yandex.ru"
    "bk.ru"
]

corporate_domeins = [
    "company.ru",
    "corporation.com",
    "university.edu",
    "organisation.org"]

personal_domeins = list(set(personal_domeins))
corporate_domeins = list(set(corporate_domeins))

print(personal_domeins)
print(corporate_domeins)

common_domeins = list(set(personal_domeins) & set(corporate_domeins))
print(common_domeins)

is_corporate = domain in corporate_domeins
print(is_corporate)

clean_body = email["body"].replace("\n", " ").replace("\t", " ")
email["clean_body"] = clean_body
print(email["clean_body"])

email["sent_text"] = f""" Кому: {email['to']} 
    От {email['from']}, 
    Тема: {email['subject']} 
    Дата: {email['date']} 
 {email['clean_body']}"""
print(email["sent_text"])

pages = math.ceil(len(email["clean_body"]) / 500)
print(pages)

is_subject_empty = not email["subject"].strip()
is_body_empty = not email["body"].strip()
print(is_subject_empty)
print(is_body_empty)

email["masked_from"] = login[:2] + "***@" + domain

print(email["masked_from"])

personal_domeins.remove("list.ru")
personal_domeins.remove("bk.ru")
print(personal_domeins)
