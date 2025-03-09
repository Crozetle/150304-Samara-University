import os

# Получаем список всех текстовых файлов в текущей папке
files = [f for f in os.listdir() if os.path.isfile(f) and f.endswith('.md')]
files.sort()  # Сортируем файлы по алфавиту

# Проходим по каждому файлу
for i, filename in enumerate(files):
    prev_file = files[i - 1] if i > 0 else None  # Предыдущий файл
    next_file = files[i + 1] if i < len(files) - 1 else None  # Следующий файл

    # Формируем строку с ссылками
    links = "\n---\n"
    if prev_file:
        links += f"[[{prev_file}|<< Предыдущий вопрос]] | "
    if next_file:
        links += f"[[{next_file}|Следующий вопрос >>]]"

    # Открываем файл и добавляем строку в конец
    with open(filename, 'a', encoding='utf-8') as file:
        file.write(links)

print("Ссылки добавлены во все файлы.")
