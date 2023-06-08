import csv
import json

with open('dengue - dengue.csv', 'r') as csvfile:
    json = []
    csv_reader = csv.reader(csvfile)
    line_number = 0
    for line in csv_reader:
        if line_number == 0:
            params = line
        else:
            kamus = dict()
            for i in range(len(params)):
                kamus[params[i]] = line[i]
            json.append(kamus)
        line_number += 1
    

"""
dengue
tidak_dengue
pain_behind_the_eyes #a
metallic_taste_in_the_mouth #b
appetite_loss #c
addominal_pain #d
nausea_vomiting #e
diarrhoea #f
temp_c #g

"""

yes_given_yes = {

        "a": 0,
        "b": 0,
        "c": 0,
        "d": 0,
        "e": 0,
        "f": 0,
        "g": 0,
        "sum": 0
}
yes_given_no = {

        "a": 0,
        "b": 0,
        "c": 0,
        "d": 0,
        "e": 0,
        "f": 0,
        "g": 0,
        "sum": 0
}
no_given_yes = {
        "a": 0,
        "b": 0,
        "c": 0,
        "d": 0,
        "e": 0,
        "f": 0,
        "g": 0,
        "sum": 0
    }
no_given_no = {

        "a": 0,
        "b": 0,
        "c": 0,
        "d": 0,
        "e": 0,
        "f": 0,
        "g": 0,
        "sum": 0
}
total_yes = 0
total_no = 0

for kamus in json:
    kamus['temp_c'] = kamus['temp_c'].replace(",", ".")
    if kamus['dengue'] == 'yes':
        total_yes += 1
        if kamus['pain_behind_the_eyes'] == 'yes':
            yes_given_yes["a"] += 1
        else:
            no_given_yes["a"] += 1
        if kamus['metallic_taste_in_the_mouth'] == 'yes':
            yes_given_yes["b"] += 1
        else:
            no_given_yes["b"] += 1
        if kamus['appetite_loss'] == 'yes':
            yes_given_yes["c"] += 1
        else:
            no_given_yes["c"] += 1
        if kamus['addominal_pain'] == 'yes':
            yes_given_yes["d"] += 1
        else:
            no_given_yes["d"] += 1
        if kamus['nausea_vomiting'] == 'yes':
            yes_given_yes["e"] += 1
        else:
            no_given_yes["e"] += 1
        if kamus['diarrhoea'] == 'yes':
            yes_given_yes["f"] += 1
        else:
            no_given_yes["f"] += 1
        if float(kamus['temp_c']) > 36:
            yes_given_yes["g"] += 1
        else:
            no_given_yes["g"] += 1
    else:
        total_no += 1
        if kamus['pain_behind_the_eyes'] == 'yes':
            yes_given_no["a"] += 1
        else:
            no_given_no["a"] += 1
        if kamus['metallic_taste_in_the_mouth'] == 'yes':
            yes_given_no["b"] += 1
        else:
            no_given_no["b"] += 1
        if kamus['appetite_loss'] == 'yes':
            yes_given_no["c"] += 1
        else:
            no_given_no["c"] += 1
        if kamus['addominal_pain'] == 'yes':
            yes_given_no["d"] += 1
        else:
            no_given_no["d"] += 1
        if kamus['nausea_vomiting'] == 'yes':
            yes_given_no["e"] += 1
        else:
            no_given_no["e"] += 1
        if kamus['diarrhoea'] == 'yes':
            yes_given_no["f"] += 1
        else:
            no_given_no["f"] += 1
        if float(kamus['temp_c']) > 37:
            yes_given_no["g"] += 1
        else:
            no_given_no["g"] += 1
yes_given_no['sum'] = total_no
no_given_no['sum'] = total_no
yes_given_yes['sum'] = total_yes
no_given_yes['sum'] = total_yes

# print("total_no: "+ str(total_no))
# print("total_yes: "+ str(total_yes))
# print("yes_given_no: "+str(yes_given_no))
# print("yes_given_yes: "+str(yes_given_yes))
# print("no_given_yes: "+str(no_given_yes))
# print("no_given_no: "+str(no_given_no))

def probability(data, gejala):
    return((data[gejala] + 1) / (data['sum'] + 7))


inate_probability_y = total_yes / (total_no + total_yes)
inate_probability_n = total_no / (total_no + total_yes)
daftar_gejala = [
    ("Sakit di belakang mata", "a"),
    ("Mulut terasa seperti darah", "b"),
    ("Kehilangan nafsu makan", "c"),
    ("Sakit addominal", "d"),
    ("Muntah dan mual", "e"),
    ("Diare", "f"),
    ("temperatur tinggi (37C < )","g")
]
probability_yes = inate_probability_y
probability_no = inate_probability_n
gejala_yang_dialami = []

print(
""" ____   ___  ____   ___      ___ ______    ___  __  _ _____ ____      ___    ____   ___   
|    \ /  _]|    \ |   \    /  _]      |  /  _]|  |/ ] ___/|    |    |   \  |    \ |   \  
|  o  )  [_ |  _  ||    \  /  [_|      | /  [_ |  ' (   \_  |  |     |    \ |  o  )|    \ 
|   _/    _]|  |  ||  D  ||    _]_|  |_||    _]|    \\__  | |  |     |  D  ||     ||  D  |
|  | |   [_ |  |  ||     ||   [_  |  |  |   [_ |     /  \ | |  |     |     ||  O  ||     |
|  | |     ||  |  ||     ||     | |  |  |     ||  .  \    | |  |     |     ||     ||     |
|__| |_____||__|__||_____||_____| |__|  |_____||__|\_|\___||____|    |_____||_____||_____|
"""
                                                                                          
)

print("\n\n\n")
for gejala in daftar_gejala:
    inputUser = input("Apakah Anda mengalami " + gejala[0] + " ? (y/n): ")
    if inputUser == "y":
        probability_yes *= probability(yes_given_yes, gejala[1])
        probability_no *= probability(yes_given_no, gejala[1])
    else:
        probability_yes *= probability(no_given_yes, gejala[1])
        probability_no *= probability(no_given_no, gejala[1])

if probability_yes > probability_no:
    print("kemungkinan positif DBD")
else:
    print("kemungkinan negatif DBD")

