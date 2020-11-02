def validate_password(password):
    """
    Функция принимает пароль строкой и выполняет валидацию с помощью трёх
    вспомогательных функций:
    1. Содержит только a−z, A−Z, 0−9
    2. Содержит четное количество букв
    3. Содержит нечетное количество цифр
    Основная функция возвращает True, если пароль валидный.
    Если пароль не валидный, возвращает лист стрингов, в которых перечислены
    причины неуспешной проверки. Например: ["содержит запрещенные символы"]
    """
    error_message = []
    if not _validate_symbols(password):
        error_message.append("Password contains restricted symbols")
    if not _validate_letters_even(password):
        error_message.append("Password letters are not even")
    if not _validate_numbers_odd(password):
        error_message.append("Password numbers are not odd")
        return error_message
    if not error_message:
        pass
    else:
        print(error_message)
    return True


def _validate_symbols(input_str):
  """
  Проверяет строку на наличие запрещенных символов
  Подсказка: у строк есть метод, проверяющий наличие только був и цифр
  Возвращает True\False
  """
  check = input_str.isalnum()
  if not check:
      return False
  return True


def _validate_letters_even(input_str):
  """
  Проверяет строку на четное количество букв
  Возвращает True\False
  """
  char_list = []
  for char in input_str:
      if char.isalpha():
          char_list.append(char)
  if not len(char_list) % 2 == 0:
      return False
  return True


def _validate_numbers_odd(input_str):
  """
  Проверяет строку на нечетное количество цифр
  Возвращает True\False
  """
  digit_list =[]
  for char in input_str:
      if char.isdigit():
          digit_list.append(char)
  if not len(digit_list) % 2 != 0:
      return False
  return True
