"""
В этот раз у нас есть компания, в ней отделы, в отделах люди. У людей есть имя, должность и зарплата.
Ваши задачи такие:
1. Вывести названия всех отделов
2. Вывести имена всех сотрудников компании.
3. Вывести имена всех сотрудников компании с указанием отдела, в котором они работают.
4. Вывести имена всех сотрудников компании, которые получают больше 100к.
5. Вывести позиции, на которых люди получают меньше 80к (можно с повторениями).
6. Посчитать, сколько денег в месяц уходит на каждый отдел – и вывести вместе с названием отдела
Второй уровень:
7. Вывести названия отделов с указанием минимальной зарплаты в нём.
8. Вывести названия отделов с указанием минимальной, средней и максимальной зарплаты в нём.
9. Вывести среднюю зарплату по всей компании.
10. Вывести названия должностей, которые получают больше 90к без повторений.
11. Посчитать среднюю зарплату по каждому отделу среди девушек (их зовут Мишель, Николь, Кристина и Кейтлин).
12. Вывести без повторений имена людей, чьи фамилии заканчиваются на гласную букву.
Третий уровень:
Теперь вам пригодится ещё список taxes, в котором хранится информация о налогах на сотрудников из разных департаметов.
Если department None, значит, этот налог применяется ко всем сотрудникам компании.
Иначе он применяется только к сотрудникам департмента, название которого совпадает с тем, что записано по ключу department.
К одному сотруднику может применяться несколько налогов.
13. Вывести список отделов со средним налогом на сотрудников этого отдела.
14. Вывести список всех сотрудников с указанием зарплаты "на руки" и зарплаты с учётом налогов.
15. Вывести список отделов, отсортированный по месячной налоговой нагрузки.
16. Вывести всех сотрудников, за которых компания платит больше 100к налогов в год.
17. Вывести имя и фамилию сотрудника, за которого компания платит меньше всего налогов.
"""

departments = [
    {
        "title": "HR department",
        "employers": [
            {"first_name": "Daniel", "last_name": "Berger", "position": "Junior HR", "salary_rub": 50000},
            {"first_name": "Michelle", "last_name": "Frey", "position": "Middle HR", "salary_rub": 75000},
            {"first_name": "Kevin", "last_name": "Jimenez", "position": "Middle HR", "salary_rub": 70000},
            {"first_name": "Nicole", "last_name": "Riley", "position": "HRD", "salary_rub": 120000},
        ]
    },
    {
        "title": "IT department",
        "employers": [
            {"first_name": "Christina", "last_name": "Walker", "position": "Python dev", "salary_rub": 80000},
            {"first_name": "Michelle", "last_name": "Gilbert", "position": "JS dev", "salary_rub": 85000},
            {"first_name": "Caitlin", "last_name": "Bradley", "position": "Teamlead", "salary_rub": 950000},
            {"first_name": "Brian", "last_name": "Hartman", "position": "CTO", "salary_rub": 130000},
        ]
    },
]

taxes = [
    {"department": None, "name": "vat", "value_percents": 13},
    {"department": "IT department", "name": "hiring", "value_percents": 6},
    {"department": "BizDev department", "name": "sales", "value_percents": 20},
]


def get_employer():
    lst_ans = []
    for department in departments:
        for employer in department["employers"]:
            lst_ans.append(employer)
    return lst_ans


def get_title(department):
    return department['title']


def get_name(employer):
    return employer['first_name']


def get_tax():
    dict_ans = {}
    for tax in taxes:
        dict_ans[tax['department']] = tax['value_percents']
    return dict_ans


print('Номер 1')
print(', '.join([department['title'] for department in departments]))
print('Номер 2')
lst_ans_for_num2 = []
for i in get_employer():
    lst_ans_for_num2.append(get_name(i))
print(', '.join(lst_ans_for_num2))
print('Номер 3')
lst_ans_for_num3 = []
for department in departments:
    for employer in department["employers"]:
        lst_ans_for_num3.append(f"{get_name(employer)} работает в отделе {get_title(department)}.")
print(*lst_ans_for_num3)
print('Номер 4')
lst_ans_for_num4 = []
for department in departments:
    for employer in department["employers"]:
        if employer["salary_rub"] > 100000:
            lst_ans_for_num4.append(get_name(employer))
print(', '.join(lst_ans_for_num4))
print('Номер 5')
lst_ans_for_num5 = []
for i in get_employer():
    if i['salary_rub'] < 80000:
        lst_ans_for_num5.append(i['position'])
print(', '.join([*set(lst_ans_for_num5)]))
print('Номер 6')
lst_ans_for_num6 = []
sum_for_depart = 0
for department in departments:
    for employer in department["employers"]:
        sum_for_depart += employer["salary_rub"]
    lst_ans_for_num6.append(f'На отдел "{get_title(department)}" уходит {sum_for_depart} руб.')
    sum_for_depart = 0
print(*lst_ans_for_num6)
print('Номер 7')
min_salary = 0
for department in departments:
    for employer in department["employers"]:
        if min_salary > employer["salary_rub"]:
            min_salary = employer
        else:
            if min_salary == 0:
                min_salary = employer["salary_rub"]
    print(f'В отделе "{get_title(department)}" самый маленький заработок - {min_salary}')
    min_salary = 0
print('Номер 8')
min_salary = 0
max_salary = 0
sum_ = 0
for department in departments:
    for employer in department["employers"]:
        if min_salary > employer["salary_rub"]:
            min_salary = employer
        else:
            if min_salary == 0:
                min_salary = employer["salary_rub"]
        if max_salary < employer["salary_rub"]:
            max_salary = employer["salary_rub"]
        sum_ += employer["salary_rub"]
    print(f'В отделе "{get_title(department)}" самый маленький заработок - {min_salary},'
          f' самый большой заработок - {max_salary}, а средний заработок равен {sum_ / len(department["employers"])}')
    min_salary = 0
    max_salary = 0
    sum_ = 0
print('Номер 9')
sum_ = 0
count = 0
for department in departments:
    for employer in department["employers"]:
        sum_ += employer["salary_rub"]
        count += 1
print(sum_ / count)
print('Номер 10')
lst_ans_for_num10 = []
for i in get_employer():
    if i["salary_rub"] > 90000:
        lst_ans_for_num10.append(i["position"])
print(', '.join([*set(lst_ans_for_num10)]))
print('Номер 11')
lst_ans_for_num11 = []
female_salary = 0
female_count = 0
for department in departments:
    for employer in department["employers"]:
        if employer['first_name'] in ["Michelle", "Nicole", "Christina", "Caitlin"]:
            female_salary += employer["salary_rub"]
            female_count += 1
    female_salary = female_salary / female_count
    print(f'Средняя зарплата по отделу {get_title(department)} среди девушек равна {female_salary}')
    female_count = 0
    female_salary = 0
print('Номер 12')
lst_ans_for_num12 = []
for i in get_employer():
    if i['last_name'][-1] in 'aeiouyj':
        lst_ans_for_num12.append(i['first_name'])
print(', '.join([*set(lst_ans_for_num12)]))
print('Номер 13')
sum_ = 0
for department in departments:
    for employer in department["employers"]:
        sum_ += employer["salary_rub"]
    sum_ = sum_ / len(department["employers"])
    if get_title(department) in get_tax():
        tax = sum_ / 100 * get_tax()[get_title(department)]
    else:
        tax = sum_ / 100 * get_tax()[None]
    print(f'Средний налог на отдел {get_title(department)} - {tax} руб.')
    sum_ = 0
print('Номер 14')
for department in departments:
    for employer in department["employers"]:
        salary = employer["salary_rub"]
        if get_title(department) in get_tax():
            print(f'Зарплата на руки для {get_name(employer)} равна {salary}, но с учетем налогов:'
                  f' {salary - salary / 100 * get_tax()[get_title(department)]} руб.')
        else:
            print(f'Зарплата на руки для {get_name(employer)} равна {salary}, но с учетем налогов:'
                  f' {salary - salary / 100 * get_tax()[None]} руб.')
print('Номер 15')
sum_ = 0
taxes_dict = {}
for department in departments:
    for employer in department["employers"]:
        sum_ += employer["salary_rub"]
    if get_title(department) in get_tax():
        tax = sum_ / 100 * get_tax()[get_title(department)]
    else:
        tax = sum_ / 100 * get_tax()[None]
    taxes_dict[get_title(department)] = tax
    sum_ = 0

sorted_taxes_dict = dict(sorted(taxes_dict.items(), key=lambda item: item[1]))
print(', '.join(sorted_taxes_dict.keys()))
print('Номер 16')
lst_ans_for_num16 = []
for department in departments:
    for employer in department["employers"]:
        salary = employer["salary_rub"]
        if get_title(department) in get_tax():
            tax = salary / 100 * get_tax()[get_title(department)]
        else:
            tax = salary / 100 * get_tax()[None]
        annual_tax = tax * 12
        if annual_tax > 100000:
            lst_ans_for_num16.append(get_name(employer))
print(', '.join(lst_ans_for_num16))
print("Номер 17")
lst_ans_for_num17 = []
min_tax = 0
for department in departments:
    for employer in department["employers"]:
        salary = employer["salary_rub"]
        if get_title(department) in get_tax():
            tax = salary / 100 * get_tax()[get_title(department)]
        else:
            tax = salary / 100 * get_tax()[None]
        if min_tax > tax:
            min_tax = tax
            lst_ans_for_num17.append([get_name(employer), employer['last_name']])
        else:
            if min_tax == 0:
                min_tax = tax
                lst_ans_for_num17.append(get_name(employer))
print(*lst_ans_for_num17[-1])





