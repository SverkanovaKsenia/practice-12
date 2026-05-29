ru_en = {}

with open("en-ru.txt", "r", encoding='utf-8') as f:
    for line in f:
        line = line.strip()

        parts = line.split(" - ")
        english = parts[0]
        russian_words = parts[1]

        words = russian_words.split(", ")

        for russian in words:
            if russian not in ru_en:
                ru_en[russian] = []
            ru_en[russian].append(english)

with open("ru-en.txt", "w", encoding='utf-8') as f:
    for russian in sorted(ru_en.keys()):
        english_list = sorted(ru_en[russian])
        f.write(russian + " - " + ", ".join(english_list) + "\n")

print("Словарь создан. Файл ru-en.txt готов.")