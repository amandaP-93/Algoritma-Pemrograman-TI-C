# match.py
# Contoh match-case di Python

hari = 3

match hari:
    case 1:
        print("Monday")
    case 2:
        print("Selasa")
    case 3:
        print("Wednesday")
    case _:
        print("Hari tidak diketahui")
