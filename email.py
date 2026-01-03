import datetime


# 1. Создайте словарь email
email = {
    "subject": "   ",
    "from": "   alex@business.net ",
    "to": "   hr@company.ru ",
    "body": "Hi HR,\nPlease find attached my updated CV.\nThanks!"
}

# 2. Добавьте дату отправки
date_time = datetime.datetime.now()
email['date_time'] = date_time.strftime("%Y-%m-%d")

# 3. Нормализуйте e-mail адреса
email['from'] = email["from"].strip().lower()
email['to'] = email["to"].strip().lower()

# 4. Извлеките логин и домен отправителя
login = email["from"].split('@')[0]
domain = email["from"].split('@')[1]

# 5. Создайте сокращённую версию текста
short_body = f'{email["body"][0:10]}...'
email['short_body'] = short_body

# 6. Списки доменов. 7 пункт уехал в конец, т.к. все принты там
personal_domains = {'gmail.com', 'list.ru', 'yahoo.com', 'outlook.com', 'hotmail.com', 'icloud.com', 'yandex.ru',
                    'mail.ru', 'list.ru', 'bk.ru', 'inbox.ru', 'corporation.com', 'university.edu'}
corporate_domains = {'company.ru', 'corporation.com', 'university.edu', 'organization.org', 'company.ru',
                     'business.net'}

# 7. Проверьте что в списке личных и корпоративных доменов нет пересечений (вывод результата проверки в конце после
# print(short_body))
intersection = personal_domains & corporate_domains

# 8. Проверьте «корпоративность» отправителя
is_corporate = domain in corporate_domains
email['is_corporate'] = is_corporate

# 9. Соберите «чистый» текст сообщения
clean_body = email["body"].replace('\t', ' ').replace('\n', ' ')
email['clean_body'] = clean_body


# 10. Сформируйте текст отправленного письма
sent_text = f'''Кому: {email["to"]},
От {email["from"]}
Тема: {email["subject"]},
Дата {email["date_time"]}
{email["clean_body"]}'''
email["sent_text"] = sent_text

# 11. Рассчитайте количество страниц печати
pages = (len(sent_text) + 499) // 500

# 12. Проверьте пустоту темы и тела письма
is_subject_empty = not email["subject"]
is_body_empty = not email["body"]

# 13. Создайте «маску» e-mail отправителя
masked_from = f'{login[:2]}***@{domain}'
email['masked_from'] = masked_from

# 14. Удалите из списка личных доменов
personal_domains.remove("list.ru")
personal_domains.remove("bk.ru")

# --- Вывод результатов ---
print(email)
print(login)
print(domain)
print(short_body)

if intersection:
    str_intersection = str(intersection).strip('{}').replace("'", '')
    print(f'В списках есть пересечения по доменам: {str_intersection}')
else:
    print('Пересечений доменов нет')

print(sent_text)
print(pages)

if is_subject_empty:
    print('Тема пустая')
else:
    print('Тема не пустая')

if is_body_empty:
    print('Тело пустое')
else:
    print('Тело не пустое')

print(masked_from)
