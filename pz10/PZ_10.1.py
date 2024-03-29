# Книжные магазины предлагают следующие коллекции книг.
# Магистр — Лермонтов,Достоевский,Пушкин,Тютчев
# ДомКниги — Толстой,Грибоедов,Чехов,Пушкин
# БукМаркет — Пушкин,Достоевский,Маяковский
# Галерея — Чехов,Тютчев, Пушкин
# Определить в каких магазинах нельзя приобрести книги Грибоедова и Маяковского.
magistr = {"Лермонтов" , "Достоевский" , "Пушкин", "Тютчев"}
dom_knigi = {"Толстой", "Грибоедов", "Чехов", "Пушкин"}
buk_market = {"Пушкин", "Достоевский", "Маяковский"}
gallery = {"Чехов", "Тютчев", "Пушкин"}

all_books = magistr.union(dom_knigi, buk_market, gallery)
notbooks = {'Грибоедов', 'Маяковский'}

for store, books in {"Магистр": magistr, "ДомКниги": dom_knigi, "БукМаркет": buk_market, "Галерея": gallery}.items():
    if notbooks.isdisjoint(books):
        print(f'В магазине {store} нельзя приобрести книги Грибоедова и Маяковского')