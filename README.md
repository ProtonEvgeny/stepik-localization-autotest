# Задание: запуск автотестов для разных языков интерфейса

### Запуск теста
`pytest --language=[ваш язык] test_items.py`

Также можно опционально запустить тест не в Chrome, а в Firefox:

`pytest --language=[ваш язык] --browser_name=firefox test_items.py`

### Библиотеки

На всякий случай добавил `requirments.txt`, чтобы воспроизвести точно такое же окружение как у меня.