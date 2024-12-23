from openpyxl import Workbook # type: ignore

# Abuur workbook cusub oo xulo worksheet-ka firfircoon
wb = Workbook()
ws = wb.active

# U magac dar worksheet-ka
ws.title = "Joogitaanka"

# Ku dar cinwaannada (headers)
headers = ["Magaca Ardayga", "Taariikhda", "Joogitaanka"]
ws.append(headers)

# Liiska magacyada ardayda
ardayda = ["Aamina", "Axmed", "Cabdi", "Degan"]
taariikhaha = ["2024-12-01", "2024-12-02", "2024-12-03"]

# Ku qor xogta joogitaanka
for taariikh in taariikhaha:
    for arday in ardayda:
        ws.append([arday, taariikh, "Haa"])  # "Haa" macnaheedu waa joogitaan.

# Faylka ku keydi magaca "joogitaanka.xlsx"
wb.save("joogitaanka.xlsx")

print("Faylka joogitaanka waa la abuuray!")