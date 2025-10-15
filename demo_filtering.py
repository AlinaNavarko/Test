"""
Демонстрация фильтрации компонентов
При выборе сервера показываются только совместимые компоненты
"""

from configurator import ServerConfigurator
from sample_data_ru import create_sample_data_ru, create_compatibility_matrix_extended
from data_models import ComponentType

def print_separator():
    print("=" * 70)

def demo_hp_server():
    """Демо: выбираем HP сервер"""
    print_separator()
    print("СЦЕНАРИЙ 1: Выбираем HP ProLiant ML350 G4p (Socket 604, DDR2)")
    print_separator()
    
    configurator = ServerConfigurator()
    configurator.data = create_sample_data_ru()
    configurator.compatibility_matrix = create_compatibility_matrix_extended()
    
    # Добавляем HP сервер
    success, errors = configurator.add_component("hp_ml350g4p")
    print(f"\n✅ Добавлен: HP ProLiant ML350 G4p")
    
    # Теперь смотрим, какие процессоры доступны
    print("\n📌 ДОСТУПНЫЕ ПРОЦЕССОРЫ (только совместимые с HP):")
    available_cpus = configurator.get_available_components(ComponentType.PROCESSOR)
    if available_cpus:
        for cpu in available_cpus:
            print(f"  ✅ {cpu.name}")
            socket = next((attr.value for attr in cpu.attributes if attr.name == "Сокет"), "N/A")
            print(f"     Сокет: {socket}, Цена: {cpu.price} ₽")
    else:
        print("  ❌ Нет доступных процессоров")
    
    # Смотрим память
    print("\n📌 ДОСТУПНАЯ ПАМЯТЬ (только совместимая с HP):")
    available_memory = configurator.get_available_components(ComponentType.MEMORY)
    if available_memory:
        for mem in available_memory:
            print(f"  ✅ {mem.name}")
            mem_type = next((attr.value for attr in mem.attributes if attr.name == "Тип"), "N/A")
            print(f"     Тип: {mem_type}, Цена: {mem.price} ₽")
    
    # Смотрим блоки питания
    print("\n📌 ДОСТУПНЫЕ БЛОКИ ПИТАНИЯ:")
    available_psu = configurator.get_available_components(ComponentType.POWER_SUPPLY)
    if available_psu:
        for psu in available_psu:
            print(f"  ✅ {psu.name}")
    
    print("\n❌ НЕДОСТУПНЫЕ КОМПОНЕНТЫ:")
    print("  • Intel Xeon E5620 (Socket 1366 - несовместим с HP Socket 604)")
    print("  • Intel Xeon X5670 (Socket 1366 - несовместим с HP Socket 604)")
    print("  • Samsung 4 ГБ DDR3 (DDR3 несовместим с DDR2)")
    print("  • Crucial 8 ГБ DDR3 (DDR3 несовместим с DDR2)")
    print("  • Dell Блок питания (только для Dell серверов)")
    print("  • IBM Блок питания (только для IBM серверов)")

def demo_dell_server():
    """Демо: выбираем Dell сервер"""
    print("\n\n")
    print_separator()
    print("СЦЕНАРИЙ 2: Выбираем Dell PowerEdge R710 (Socket 1366, DDR3)")
    print_separator()
    
    configurator = ServerConfigurator()
    configurator.data = create_sample_data_ru()
    configurator.compatibility_matrix = create_compatibility_matrix_extended()
    
    # Добавляем Dell сервер
    success, errors = configurator.add_component("dell_poweredge_r710")
    print(f"\n✅ Добавлен: Dell PowerEdge R710")
    
    # Смотрим доступные процессоры
    print("\n📌 ДОСТУПНЫЕ ПРОЦЕССОРЫ (только совместимые с Dell):")
    available_cpus = configurator.get_available_components(ComponentType.PROCESSOR)
    if available_cpus:
        for cpu in available_cpus:
            print(f"  ✅ {cpu.name}")
            socket = next((attr.value for attr in cpu.attributes if attr.name == "Сокет"), "N/A")
            cores = next((attr.value for attr in cpu.attributes if attr.name == "Ядер"), "N/A")
            print(f"     Сокет: {socket}, Ядер: {cores}, Цена: {cpu.price} ₽")
    
    # Смотрим память
    print("\n📌 ДОСТУПНАЯ ПАМЯТЬ (только совместимая с Dell):")
    available_memory = configurator.get_available_components(ComponentType.MEMORY)
    if available_memory:
        for mem in available_memory:
            print(f"  ✅ {mem.name}")
            mem_type = next((attr.value for attr in mem.attributes if attr.name == "Тип"), "N/A")
            capacity = next((attr.value for attr in mem.attributes if attr.name == "Объем"), "N/A")
            print(f"     Тип: {mem_type}, Объем: {capacity} ГБ, Цена: {mem.price} ₽")
    
    # Смотрим блоки питания
    print("\n📌 ДОСТУПНЫЕ БЛОКИ ПИТАНИЯ:")
    available_psu = configurator.get_available_components(ComponentType.POWER_SUPPLY)
    if available_psu:
        for psu in available_psu:
            print(f"  ✅ {psu.name}")
    
    print("\n❌ НЕДОСТУПНЫЕ КОМПОНЕНТЫ:")
    print("  • Intel Xeon 3.0 ГГц (Socket 604 - несовместим с Dell Socket 1366)")
    print("  • Intel Xeon 3.2 ГГц (Socket 604 - несовместим с Dell Socket 1366)")
    print("  • Kingston 1 ГБ DDR2 (DDR2 несовместим с DDR3)")
    print("  • Corsair 2 ГБ DDR2 (DDR2 несовместим с DDR3)")
    print("  • HP Блок питания (только для HP серверов)")
    print("  • IBM Блок питания (только для IBM серверов)")

def demo_without_server():
    """Демо: без выбора сервера"""
    print("\n\n")
    print_separator()
    print("СЦЕНАРИЙ 3: Без выбора сервера (все компоненты доступны)")
    print_separator()
    
    configurator = ServerConfigurator()
    configurator.data = create_sample_data_ru()
    configurator.compatibility_matrix = create_compatibility_matrix_extended()
    
    print("\n📌 ВСЕ ДОСТУПНЫЕ ПРОЦЕССОРЫ:")
    available_cpus = configurator.get_available_components(ComponentType.PROCESSOR)
    for cpu in available_cpus:
        print(f"  • {cpu.name}")
    
    print(f"\nВсего доступно: {len(available_cpus)} процессоров")
    
    print("\n💡 После выбора сервера список автоматически отфильтруется!")

def demo_try_add_incompatible():
    """Демо: попытка добавить несовместимый компонент"""
    print("\n\n")
    print_separator()
    print("СЦЕНАРИЙ 4: Попытка добавить несовместимые компоненты")
    print_separator()
    
    configurator = ServerConfigurator()
    configurator.data = create_sample_data_ru()
    configurator.compatibility_matrix = create_compatibility_matrix_extended()
    
    # Добавляем HP сервер
    configurator.add_component("hp_ml350g4p")
    print(f"\n✅ Добавлен: HP ProLiant ML350 G4p (Socket 604, DDR2)")
    
    # Пытаемся добавить процессор для Dell (Socket 1366)
    print("\n❌ Попытка добавить Intel Xeon E5620 (Socket 1366):")
    success, errors = configurator.add_component("intel_xeon_e5620")
    if not success:
        print(f"   ОШИБКА: {errors[0]}")
    
    # Добавляем совместимый процессор
    print("\n✅ Добавляем совместимый Intel Xeon 3.0 ГГц (Socket 604):")
    success, errors = configurator.add_component("intel_xeon_3_0_604")
    if success:
        print("   Успешно добавлен!")
    
    # Пытаемся добавить DDR3 память
    print("\n❌ Попытка добавить Samsung 4 ГБ DDR3:")
    success, errors = configurator.add_component("samsung_4gb_ddr3_1333")
    if not success:
        print(f"   ОШИБКА: {errors[0]}")
    
    # Добавляем совместимую DDR2 память
    print("\n✅ Добавляем совместимую Kingston 1 ГБ DDR2:")
    success, errors = configurator.add_component("kingston_1gb_ddr2_400")
    if success:
        print("   Успешно добавлен!")
    
    # Показываем итоговую конфигурацию
    config = configurator.get_current_configuration()
    print(f"\n📊 ИТОГОВАЯ КОНФИГУРАЦИЯ:")
    print(f"   Общая стоимость: {config.total_price} ₽")
    print(f"   Валидна: {'✅' if config.is_valid else '❌'}")
    print(f"   Компонентов: {sum(len(c) for c in config.components.values())}")

if __name__ == "__main__":
    print("\n🖥️  ДЕМОНСТРАЦИЯ ФИЛЬТРАЦИИ КОМПОНЕНТОВ\n")
    
    demo_hp_server()
    demo_dell_server()
    demo_without_server()
    demo_try_add_incompatible()
    
    print("\n\n")
    print_separator()
    print("ВЫВОД:")
    print_separator()
    print("""
✅ При выборе сервера автоматически фильтруются только совместимые компоненты
✅ Попытка добавить несовместимый компонент блокируется с объяснением причины
✅ Система проверяет совместимость по сокету, типу памяти, производителю БП
✅ Матрица совместимости обеспечивает быструю фильтрацию за O(1)

💡 Для веб-интерфейса: после выбора сервера вызывайте 
   get_available_components() для каждой категории и показывайте только их!
    """)
    print_separator()

