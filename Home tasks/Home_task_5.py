# Напишите декоратор для превращения функции print в генератор html-тегов
# Декоратор должен принимать список тегов italic, bold, underline
# Результатом работы декоратора с аргументами italic, bold должно быть преобразование из строки вида "test.txt string"
# в "<i><b>test.txt string</b></i>"

def str_to_html(tags):
    def decorator(func):
        tag_base = {
            "italic": f"<i>%text%</i>",
            "bold": f"<b>%text%</b>",
            "underline": f"<u>%text%</u>",
        }

        def wrapper(text):
            clean_tags = []
            for tag in tags:
                if tag in tag_base:
                    value_tag = tag_base[tag]
                    clean_tags.extend(value_tag.split("%text%"))
            test_text = func(text)
            result = f"{clean_tags[0]}{clean_tags[2]}{test_text}{clean_tags[1]}{clean_tags[3]}"
            print(result)
        return wrapper
    return decorator


@str_to_html(["underline", "bold"])
def get_text(text):
    return text

# Напишите функцию, которая возвращает список файлов из директории.
# Напишите декоратор для этой функции, который прочитает все файлы с
# раширением .log из найденных


def log_reading(func):
    def wrapper(*args):
        files = func(*args)
        for file in files:
            if ".log" in file:
                read_file = open(file, "r")
                print(read_file.readlines())
    return wrapper


@log_reading
def get_files(directory):
    import os
    file_list = []
    for path, dirs, files in os.walk(directory):
        for file in files:
            file_list.append(file)
    return file_list
