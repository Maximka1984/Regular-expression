
import re
from pprint import pprint
# читаем адресную книгу в формате CSV в список contacts_list
import csv
with open("phonebook_raw.csv", encoding="utf-8") as f:
  rows = csv.reader(f, delimiter=",")
  contacts = list(rows)
#pprint(contacts)

# TODO 1: выполните пункты 1-3 ДЗ

list_contacts = []
pattern_full_name = r'(^[А-Я]\w+) ?,?(\w+) ?,?(\w+)?'
substitution_pattern_full_name = r'\1,\2,\3'
for contact in contacts:
    while '' in contact:
        contact.remove('')
    result = re.sub(pattern_full_name, substitution_pattern_full_name, ','.join(contact))
    list_contacts.append(result)
#pprint(list_contacts)


pattern_phone_number = r'(\+7|8) ?\(?(\d{3})\)?-? ?(\d{3})\-? ?(\d{2})-? ?(\d{2}) ?\(?(доб\.)? ?(\d+)?(\))?'
substitution_pattern_phone_number = r'+7(\2)\3-\4-\5 \6\7'
for a, b in enumerate(list_contacts):
  b = b.split(',')
  result = re.sub(pattern_phone_number,substitution_pattern_phone_number, ','.join(b))
  list_contacts[a] = result
#pprint(list_contacts)


list_contacts_dict = {}
for _ in list_contacts:
    if list(list_contacts_dict.keys()).count(','.join(_.split(',')[0:2])):
        list_contacts_dict[','.join(_.split(',')[0:2])] += f",{','.join(_.split(',')[2:])}"
    else:
        list_contacts_dict.setdefault(','.join(_.split(',')[0:2]), ','.join(_.split(',')[2:]))
#pprint(list_contacts_dict)


list_contacts_sort = []
for j, k in list_contacts_dict.items():
    list_contacts_sort.append(list(j.split(',')) + list(k.split(',')))
#pprint(list_contacts_sort)


list_contacts_winner = []
for u in list_contacts_sort:
    u = list(dict().fromkeys(u))
    for m in u:
        if m[0] == '+':
            if m.count('доб'):
                u.append(u.pop(u.index(m)))
            else:
                if m.count(' '):
                    u.append(u.pop(u.index(m)).replace(' ', ''))


    for k in u:
        if k.count('@'):
            u.append(u.pop(u.index(k)))
    list_contacts_winner.append(u)
pprint(list_contacts_winner)




# TODO 2: сохраните получившиеся данные в другой файл
# код для записи файла в формате CSV
with open("phonebook.csv", "w", encoding="utf-8") as f:
    datawriter = csv.writer(f, delimiter=',')
# Вместо contacts_list подставьте свой список
    datawriter.writerows(list_contacts_winner)