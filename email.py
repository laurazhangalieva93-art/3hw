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

personal_domains = [
    "gmail.com",
    "list.ru",
    "yahoo.com",
    "outlook.com",
    "hotmail.ru",
    "icloud.com",
    "yandex.ru"
    "bk.ru"
]

corporate_domains = [
    "company.ru",
    "corporation.com",
    "university.edu",
    "organisation.org"]

personal_domains = list(set(personal_domains))
corporate_domains = list(set(corporate_domains))

print(personal_domains)
print(corporate_domains)

common_domains = list(set(personal_domains) & set(corporate_domains))
print(common_domains)

is_corporate = domain in corporate_domains
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

personal_domains.remove("list.ru")
if "bk.ru" in  personal_domains: personal_domains.remove("bk.ru")
print(personal_domains)

