# Поддержка русского языка

## Обзор

Конфигуратор серверов полностью поддерживает русский язык для всех компонентов, интерфейса и сообщений.

## Использование русских данных

### Вариант 1: Использовать русские названия компонентов

```python
from configurator import ServerConfigurator
from sample_data_ru import create_sample_data_ru, create_compatibility_matrix_extended

# Создать конфигуратор с русскими данными
configurator = ServerConfigurator()
configurator.data = create_sample_data_ru()
configurator.compatibility_matrix = create_compatibility_matrix_extended()

# Теперь все компоненты имеют русские названия и описания
success, errors = configurator.add_component("hp_ml350g4p")
component = configurator.get_component_details("hp_ml350g4p")
print(component.name)  # "HP ProLiant ML350 G4p"
print(component.description)  # "Начальный серверный стоечный сервер..."
```

### Вариант 2: Использовать систему переводов

```python
from translations import t, set_language

# Установить русский язык (по умолчанию)
set_language("ru")

# Использовать переводы
print(t("component_type_server"))      # "Сервер"
print(t("component_type_processor"))   # "Процессор"
print(t("component_type_memory"))      # "Оперативная память"
print(t("total_price"))                # "Общая стоимость"
print(t("valid"))                      # "Действительна"
```

## Доступные компоненты с русскими названиями

### Серверы
- **HP ProLiant ML350 G4p** - Начальный серверный стоечный сервер с поддержкой двух процессоров
- **Dell PowerEdge R710** - Серверный стоечный сервер среднего уровня с большой емкостью памяти
- **IBM System x3650 M3** - Высокопроизводительный стоечный сервер для критичных нагрузок

### Процессоры
- **Intel Xeon 3.0 ГГц** - Одноядерный процессор для серверов начального уровня
- **Intel Xeon 3.2 ГГц** - Одноядерный процессор с повышенной частотой
- **Intel Xeon E5620** - Четырехядерный процессор для высокопроизводительных задач
- **Intel Xeon X5670** - Шестиядерный процессор топового уровня

### Оперативная память
- **Kingston 1 ГБ DDR2-400** - Модуль памяти DDR2 начального уровня
- **Corsair 2 ГБ DDR2-533** - Модуль памяти DDR2 повышенной емкости
- **Samsung 4 ГБ DDR3-1333** - Современный модуль памяти DDR3
- **Crucial 8 ГБ DDR3-1600** - Высокоемкий модуль памяти DDR3 с высокой частотой

### Накопители
- **Seagate 500 ГБ SATA** - Надежный жесткий диск для базовых задач
- **Western Digital 1 ТБ SATA** - Емкий жесткий диск для хранения данных
- **Intel SSD 240 ГБ SATA** - Быстрый твердотельный накопитель

### Блоки питания
- **HP Блок питания 460 Вт** - Блок питания для серверов HP
- **Dell Блок питания 750 Вт** - Энергоэффективный блок питания для серверов Dell
- **IBM Блок питания 835 Вт** - Высокоэффективный блок питания для серверов IBM

## Атрибуты компонентов на русском

Все атрибуты компонентов имеют русские названия:

```python
component.attributes = [
    ComponentAttribute("Форм-фактор", "4U Стойка"),
    ComponentAttribute("Макс. процессоров", "2"),
    ComponentAttribute("Слотов памяти", "8"),
    ComponentAttribute("Макс. памяти", "32", "ГБ"),
    ComponentAttribute("Частота", "3.0", "ГГц"),
    ComponentAttribute("Ядер", "4"),
    ComponentAttribute("Объем", "500", "ГБ"),
    ComponentAttribute("Мощность", "460", "Вт")
]
```

## Веб-интерфейс на русском языке

Пример веб-интерфейса с русским языком находится в файле `web_ui_example.html`.

### Основные элементы интерфейса:
- Заголовок: "Конфигуратор серверов"
- Разделы: "Доступные компоненты", "Ваша конфигурация"
- Категории: "Серверы", "Процессоры", "Оперативная память", "Накопители", "Блоки питания"
- Кнопки: "Добавить", "Удалить", "Очистить", "Сохранить конфигурацию", "Экспорт в PDF"
- Итоговая стоимость: "Итоговая стоимость: XXX ₽"

## Пример полного использования

```python
from configurator import ServerConfigurator
from sample_data_ru import create_sample_data_ru, create_compatibility_matrix_extended
from translations import t, set_language

# Установить русский язык
set_language("ru")

# Создать конфигуратор с русскими данными
configurator = ServerConfigurator()
configurator.data = create_sample_data_ru()
configurator.compatibility_matrix = create_compatibility_matrix_extended()

# Добавить компоненты
print(f"\n{t('cli_welcome')}")
print("-" * 50)

components_to_add = [
    ("hp_ml350g4p", "HP ProLiant ML350 G4p"),
    ("intel_xeon_3_0_604", "Intel Xeon 3.0 ГГц"),
    ("kingston_1gb_ddr2_400", "Kingston 1 ГБ DDR2-400"),
    ("seagate_500gb_sata", "Seagate 500 ГБ SATA"),
    ("hp_460w_psu", "HP Блок питания 460 Вт")
]

for component_id, component_name in components_to_add:
    success, errors = configurator.add_component(component_id)
    if success:
        print(f"✅ {t('component_added')}: {component_name}")
    else:
        print(f"❌ {t('error')}: {', '.join(errors)}")

# Получить конфигурацию
config = configurator.get_current_configuration()

print(f"\n{t('configuration')}")
print("-" * 50)
print(f"{t('total_price')}: {config.total_price} ₽")
print(f"{t('valid')}: {'✅' if config.is_valid else '❌'}")

if config.validation_errors:
    print(f"\n{t('validation_errors')}:")
    for error in config.validation_errors:
        print(f"  • {error}")

# Показать выбранные компоненты
print(f"\n{t('selected_components')}:")
for comp_type, components in config.components.items():
    if components:
        print(f"\n{t(f'component_type_{comp_type.value}')}:")
        for comp in components:
            print(f"  • {comp.name} - {comp.price} ₽")
```

## Расширение переводов

Чтобы добавить новые переводы, отредактируйте файл `translations.py`:

```python
RUSSIAN = {
    # ... существующие переводы ...
    
    # Добавить новые переводы
    "new_key": "Новый перевод",
    "another_key": "Другой перевод",
}
```

## Переключение языка

```python
from translations import set_language, t

# Использовать русский язык
set_language("ru")
print(t("total_price"))  # "Общая стоимость"

# Переключиться на английский
set_language("en")
print(t("total_price"))  # "Total Price"
```

## Для веб-разработчиков

При создании веб-интерфейса используйте:

1. **HTML** - используйте `lang="ru"` в теге `<html>`
2. **Кодировка** - всегда используйте UTF-8: `<meta charset="UTF-8">`
3. **Валюта** - используйте знак рубля: `₽` (не "руб")
4. **Форматирование чисел** - используйте пробелы для тысяч: "1 500 ₽", а не "1500₽"

## Рекомендации

1. **Консистентность** - используйте одинаковые термины по всему интерфейсу
2. **Единицы измерения** - используйте русские сокращения: ГБ, МГц, ГГц, Вт
3. **Падежи** - учитывайте склонение: "1 процессор", "2 процессора", "5 процессоров"
4. **Кнопки** - используйте глаголы: "Добавить", "Удалить", а не существительные

## Типичные термины

| English | Русский |
|---------|---------|
| Server | Сервер |
| Processor | Процессор |
| Memory | Оперативная память |
| Storage | Накопитель |
| Power Supply | Блок питания |
| Form Factor | Форм-фактор |
| Socket | Сокет |
| Frequency | Частота |
| Capacity | Объем |
| Compatible | Совместим |
| Incompatible | Несовместим |
| Configuration | Конфигурация |
| Add | Добавить |
| Remove | Удалить |
| Clear | Очистить |
| Save | Сохранить |
| Export | Экспорт |
