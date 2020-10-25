def even_int_generator():
    """
    Сгенерировать список из диапазона чисел от 0 до 100 и записать
    в результирующий список только четные числа.
    """
    test_list = [i for i in range(0, 100)]  # Generating a list of integers with list comprehension
    even_int_list = []
    for i in test_list:
        if i % 2 == 0:
            even_int_list.append(i)
    return even_int_list


def count_symbols(input_str):
    """
    Дописать функцию, которая считает сколько раз каждая из букв
    встречается в строке, разложить буквы в словарь парами
    {буква:количество упоминаний в строке}
    """
    output_dict = {char: input_str.count(char) for char in set(input_str)}
    return output_dict


def get_str_center(input_str):
    """
    Дописать функцию, которая вернет Х символов из середины строки
    (2 для четного кол-ва символов, 3 - для нечетного).
    """
    output_str = input_str[(len(input_str)-2)//2:(len(input_str)+3)//2]
    return output_str


def mix_strings(str1, str2):
    """
    Дописать функцию, которая будет принимать 2 строки и вставлять вторую
    в середину первой
    """
    position = int(len(str1)/2)
    result_str = str1[:position] + str2 + str1[position:]
    return result_str


def catalog_finder(url_list):
    """
    Дописать функцию, которая принимает список URL, а возвращает
    список только тех URL, в которых есть /catalog/
    """
    # your code here
    result_list = []
    for i in url_list:
        if "catalog" in i:
            result_list.append(i)
    return result_list
