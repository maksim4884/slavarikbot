# Словарь для хранения слов
words = {}


def load_dictionary(filename="data.txt"):
    """
    Загружает словарь из файла
    """
    global words
    try:
        with open(filename, 'r', encoding='utf-8') as f:
            for line in f:
                line = line.strip()
                if line and ':' in line:
                    word, translation = line.split(':', 1)
                    words[word.strip().lower()] = translation.strip()
        print(f"Загружено {len(words)} слов")
    except FileNotFoundError:
        print("Файл не найден, создаем новый словарь")
        save_dictionary(filename)


def save_dictionary(filename="data.txt"):
    """
    Сохраняет словарь в файл
    """
    with open(filename, 'w', encoding='utf-8') as f:
        for word, translation in words.items():
            f.write(f"{word}:{translation}\n")
    print(f"Словарь сохранен ({len(words)} слов)")


def add_word(word, translation):
    """
    Добавляет новое слово в словарь
    """
    word = word.lower().strip()
    if word in words:
        return f"Слово '{word}' уже есть в словаре"

    words[word] = translation.strip()
    save_dictionary()
    return f"Добавлено: {word} - {translation}"


def find_word(word):
    """
    Ищет перевод слова
    """
    word = word.lower().strip()
    if word in words:
        return f"{word} - {words[word]}"
    else:
        return f"Слово '{word}' не найдено"


def delete_word(word):
    """
    Удаляет слово из словаря
    """
    word = word.lower().strip()
    if word in words:
        del words[word]
        save_dictionary()
        return f"Слово '{word}' удалено"
    else:
        return f"Слово '{word}' не найдено"


def show_all_words():
    """
    Показывает все слова в словаре
    """
    if not words:
        return "Словарь пуст"

    result = "📚 ВАШ СЛОВАРЬ:\n"
    for i, (word, translation) in enumerate(words.items(), 1):
        result += f"{i}. {word} - {translation}\n"
    return result


def count_words():
    """
    Считает количество слов в словаре
    """
    return f"В словаре {len(words)} слов"


def search_by_letter(letter):
    """
    Ищет все слова на определенную букву
    """
    letter = letter.lower()
    found = []
    for word in words.keys():
        if word.startswith(letter):
            found.append(word)

    if found:
        result = f"Слова на букву '{letter}':\n"
        for i, word in enumerate(sorted(found), 1):
            result += f"{i}. {word} - {words[word]}\n"
        return result
    else:
        return f"Слов на букву '{letter}' не найдено"