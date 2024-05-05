
def test_function(func, test_cases):
    results = []
    for args, expected_result in test_cases:
        try:
            result = func(*args)
            if result == expected_result:
                results.append(True)
            else:
                results.append(False)
                # print(f"Тест провален для аргументов {args}. "
                #       f"Ожидаемый результат: {expected_result}. "
                #       f"Получено: {result}")
        except Exception:
            results.append(False)
            # print(f"Тест провален для аргументов {args}. "
            #       f"Ошибка: {e}")
    return results


def create_function_from_text(func_text):
    try:
        # Создаем пустой словарь для глобальных переменных
        global_vars = {}
        # Исполняем текст функции в контексте этого словаря
        exec(func_text, global_vars)
        # Найдем определение функции в созданном контексте
        for name in global_vars:
            obj = global_vars[name]
            if callable(obj):
                # Если найден объект функции, возвращаем его
                if hasattr(obj, '__code__'):
                    return obj
                else:
                    return None

    except Exception as e:
        return f"Ошибка при создании функции из кода: {e}"


