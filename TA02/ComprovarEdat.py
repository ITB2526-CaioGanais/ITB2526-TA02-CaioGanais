from datetime import date
from datetime import datetime


def comproveAge():
    today = date.today()
    print("Fecha actual:", today)

    birth = input("¿En qué año naciste? (Introduzca la fecha en forma YYYY-MM-DD): ")
    year, month, day = map(int, birth.split('-'))
    birth_date = date(year, month, day)
    age = today.year - birth_date.year - ((today.month, today.day) < (birth_date.month, birth_date.day))
    print("Edad:", age, "años")

    if age >= 18:
        print("Ets major d'edat")
    else:
        print("Ets menor d'edat")



