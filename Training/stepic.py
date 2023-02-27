import re

text = "молоко, малако, Им0л0коИхлеб"
out = re.search(r"м.л.к.", text)
print(out)





"""
d = {'Дили': list(), 'Вили': list(), 'Били': list()}
lst = [i.split(': ') for i in iter(input, 'конец')]

for elem in lst:
    d.setdefault(elem[0], []).append(elem[1])
for keys in d:
    unic = {}
    for kom in d[keys]:
        unic.setdefault(kom, 0)
        unic[kom] += 1
    d[keys] = len(unic)
for k,v in sorted(d.items(), key= lambda k_v_list: (-k_v_list[1], k_v_list[0])):
    print(f'Количество уникальных комментаторов у {k} - {v}')

"""

"""
book_of_birthday = {}
for i in range(int(input())):
    name, num, month = input().split()
    book_of_birthday.setdefault(month, []).append(name)
months = []
for i in range(int(input())):
    months.append(input())
for elem in months:
    if book_of_birthday.get(elem) is None:
        print("Нет данных")
    else:
        s = ' '
        print(s.join(sorted(book_of_birthday.get(elem))))

"""

'''
def shift_letter(letter: str, shift: int) -> str:
    "Функция сдвигает символ letter на shift позиций"
    ans = chr(ord(letter)+shift)
    if 'a' <= ans <= 'z':
        return ans
    else:
        if shift > 0:
            # в любом случае ans > 'z'
            delta = ord(ans) - ord('z') - 1
            ans = chr(ord('a') + delta)
            if 'a' <= ans <= 'z':
                return ans
            else:
                delta = ord(ans) - ord('z') - 1
                ans = chr(ord('a') + delta)
                if 'a' <= ans <= 'z':
                    return ans
        if shift < 0:
            delta = ord('a') - ord(ans)
            ans = chr(ord('z') - delta + 1)
            if 'a' <= ans <= 'z':
                return ans
            else:
                delta = ord('a') - ord(ans)
                ans = chr(ord('z') - delta + 1)
                if 'a' <= ans <= 'z':
                    return ans

def caesar_cipher(line: str, shift: int) -> str:
    "Шифр цезаря"
    string_ans = str()
    for elem in line:
        if not "a" <= elem <= "z":
            string_ans += elem
        else:
            string_ans += shift_letter(elem, shift)
    return string_ans

print(caesar_cipher('from the inside',10))
help(shift_letter)
help(caesar_cipher)
'''
'''
def check_password(pw):
    def check_num(w):
        w = list(w)
        k = 0
        for elem in w:
            if elem.isnumeric():
                k += 1
        if k >= 3:
            return True
        else:
            return False

    def isBigLitera(x):
        x = list(x)
        k = False
        for elem in x:
            if "A" <= elem <= "Z":
                k = True
                break
        return k

    def isSize(y):
        y = list(y)
        c = False
        for elem in y:
            if elem in "!@#$%*":
                c = True
                break
        return c


    if len(pw) >= 10 and check_num(pw) and isBigLitera(pw) and isSize(pw):
        print("Perfect password")
    else:
        print("Easy peasy")
'''


'''
n = int(input())
spisok = []
ansver = []
for i in range(n):
    a = str(input())
    k = 1
    if a not in spisok:
        spisok.append(a)
        ansver.append('OK')
    else:
        while a in spisok:
            if k != 1:
                a = a[:len(a)-1]
            a += str(k)
            k += 1
        spisok.append(a)
        ansver.append(a)
for elem in ansver:
    print(elem,end='\n')
'''


'''
user = {
    "id": 4170,
    "uid": "5e941db5-9e0f-4f94-9fc5-734110c6be14",
    "password": "SyUpfo1ljm",
    "first_name": "Teresa",
    "last_name": "Wehner",
    "username": "teresa.wehner",
    "email": "teresa.wehner@email.com",
    "gender": "Non-binary",
    "phone_number": "+674 424.561.2776",
    "social_insurance_number": "637316241",
    "date_of_birth": "1993-08-17"
}
user["secret"] = user.pop("password")
user["surname"] = user.pop("last_name")
'''


'''
calcul = {}
word = input()
for el in word:
    if el.isalpha() and 97 <= ord(el) <= 122:
        if el in calcul:
            calcul[el] += 1
        else:
            calcul[el] = 1
    if el.isalpha() and 65 <= ord(el) <= 90:
        if chr(ord(el)+32) in calcul:
            calcul[chr(ord(el)+32)] += 1
        else:
            calcul[chr(ord(el)+32)] = 1
print(calcul)
'''


'''
supermarket = {
    "milk": {"quantity": 20, "price": 1.19},
    "biscuits": {"quantity": 32, "price": 1.45},
    "butter": {"quantity": 20, "price": 2.29},
    "cheese": {"quantity": 15, "price": 1.90},
    "bread": {"quantity": 15, "price": 2.59},
    "cookies": {"quantity": 20, "price": 4.99},
    "yogurt": {"quantity": 18, "price": 3.65},
    "apples": {"quantity": 35, "price": 3.15},
    "oranges": {"quantity": 40, "price": 0.99},
    "bananas": {"quantity": 23, "price": 1.29}
}
sum = 0
for elem in supermarket:
    sum += supermarket[elem]["quantity"] * supermarket[elem]["price"]
print(sum)
'''


'''
S1, S2 = input(), input()
tup_S1 = {}
tup_S2 = {}

for el in S1:
    if el in tup_S1:
        tup_S1[el] += 1
    else:
        tup_S1[el] = 1

for el in S2:
    if el in tup_S2:
        tup_S2[el] += 1
    else:
        tup_S2[el] = 1

if tup_S2 == tup_S1:
    print("YES")
else:
    print("NO")
'''


'''
morze = {'a': '•—', 'b': '—•••', 'c': '—•—•', 'd': '—••',
         'e': '•', 'f': '••—•', 'g': '——•', 'h': '••••',
         'i': '••', 'j': '•———', 'k': '—•—', 'l': '•—••',
         'm': '——', 'n': '—•', 'o': '———', 'p': '•——•',
         'q': '——•—', 'r': '•—•', 's': '•••', 't': '—',
         'u': '••—', 'v': '•••—', 'w': '•——', 'x': '—••—',
         'y': '—•——', 'z': '——••'}
tekst = list(input().split())
for word in tekst:
    for letter in word:
        if "A" <= letter <= "Z":
            print(morze[chr(ord(letter)+32)], end=' ')
        else:
            print(morze[letter],end=' ')
    print(end='\n')
'''


'''
persons= [
    ('Allison Hill', 334053, 'M', '1635644202'),
    ('Megan Mcclain', 191161, 'F', '2101101595'),
    ('Brandon Hall', 731262, 'M', '6054749119'),
    ('Michelle Miles', 539898, 'M', '1355368461'),
    ('Donald Booth', 895667, 'M', '7736670978'),
    ('Gina Moore', 900581, 'F', '7018476624'),
    ('James Howard', 460663, 'F', '5461900982'),
    ('Monica Herrera', 496922, 'M', '2955495768'),
    ('Sandra Montgomery', 479201, 'M', '5111859731'),
    ('Amber Perez', 403445, 'M', '0602870126')
]
data = dict()
for person in persons:
    data[person[0]] = {}
    data[person[0]]['salary'] = person[1]
    data[person[0]]['gender'] = person[2]
    data[person[0]]['passport'] = person[3]
print(data)
'''


'''
user = {
    "id": 4170,
    "uid": "5e941db5-9e0f-4f94-9fc5-734110c6be14",
    "password": "SyUpfo1ljm",
    "first_name": "Teresa",
    "last_name": "Wehner",
    "username": "teresa.wehner",
    "email": "teresa.wehner@email.com",
    "gender": "Non-binary",
    "phone_number": "+674 424.561.2776",
    "social_insurance_number": "637316241",
    "date_of_birth": "1993-08-17",
    "employment": {
        "title": "Central Hospitality Liaison",
        "key_skill": "Organisation"
    },
    "subscription": {
        "plan": "Essential",
        "status": "Idle",
        "payment_method": "Debit card",
        "term": "Annual"
    }
}
print({key: user[key] for key in list(input().split())})
'''


'''
people = [
    ['Amy Smith', '694.322.8133x22426'],
    ['Brian Shaw', '593.662.5217x338'],
    ['Christian Sharp', '118.197.8810'],
    ['Sean Schmidt', '9722527521'],
    ['Thomas Long', '163.814.9938'],
    ['Joshua Willis', '+1-978-530-6971x601'],
    ['Ann Hoffman', '434.104.4302'],
    ['John Leonard', '(956)182-8435'],
    ['Daniel Ross', '870-365-8303x416'],
    ['Jacqueline Moon', '+1-757-865-4488x652'],
    ['Gregory Baker', '705-576-1122'],
    ['Michael Spencer', '(922)816-0599x7007'],
    ['Austin Vazquez', '399-813-8599'],
    ['Chad Delgado', '979.908.8506x886'],
    ['Jonathan Gilbert', '9577853541']
]
phone_book = {name[1]: name[0] for name in people}
'''
