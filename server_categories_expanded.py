"""
Расширенная структура серверов HPE Proliant
На основе данных с silworks.com
Включает все серии, модели и поколения (G5-G12)
"""

# ПОЛНАЯ СТРУКТУРА HPE PROLIANT
HPE_PROLIANT_STRUCTURE = {
    "DL Series": {
        "description": "Стоечные серверы (Rack-mount)",
        "generations": {
            "G5": ["DL120", "DL140", "DL145", "DL160", "DL165", "DL180", "DL185", "DL320", "DL360", "DL365", "DL380", "DL385", "DL580", "DL585"],
            "G6": ["DL120", "DL140", "DL160", "DL165", "DL170", "DL180", "DL185", "DL320", "DL360", "DL365", "DL370", "DL380", "DL385", "DL580", "DL585"],
            "G7": ["DL120", "DL140", "DL160", "DL165", "DL170", "DL180", "DL185", "DL320", "DL360", "DL365", "DL370", "DL380", "DL385", "DL580", "DL585"],
            "G8": ["DL120", "DL160", "DL320e", "DL360e", "DL360p", "DL380e", "DL380p", "DL385p", "DL560", "DL580"],
            "G9": ["DL20", "DL60", "DL80", "DL120", "DL160", "DL180", "DL320e", "DL360", "DL380", "DL388", "DL560", "DL580"],
            "G10": ["DL20", "DL60", "DL80", "DL120", "DL160", "DL180", "DL325", "DL345", "DL360", "DL365", "DL380", "DL385", "DL560", "DL580"],
            "G10+": ["DL20", "DL25", "DL110", "DL160", "DL325", "DL345", "DL360", "DL365", "DL380", "DL385", "DL560"],
            "G11": ["DL20", "DL110", "DL325", "DL345", "DL360", "DL365", "DL380", "DL385"],
            "G12": ["DL365"]
        }
    },
    
    "DX Series": {
        "description": "Серверы для объектного хранилища",
        "models": ["DX380", "DX360", "DX340", "DX320", "DX290", "DX280", "DX270", "DX190", "DX180", "DX160", "DX110"]
    },
    
    "ML Series": {
        "description": "Башенные серверы (Tower)",
        "generations": {
            "G4": ["ML150", "ML310", "ML350", "ML370"],
            "G5": ["ML110", "ML115", "ML150", "ML310", "ML350", "ML370"],
            "G6": ["ML110", "ML115", "ML150", "ML310", "ML330", "ML350", "ML370"],
            "G7": ["ML110", "ML115", "ML150", "ML310", "ML330", "ML350", "ML370"],
            "G8": ["ML110", "ML310e", "ML350e", "ML350p"],
            "G9": ["ML10", "ML30", "ML110", "ML150", "ML310e", "ML350"],
            "G10": ["ML30", "ML110", "ML350"],
            "G10+": ["ML30", "ML110", "ML350"]
        }
    },
    
    "RL Series": {
        "description": "Компактные серверы (Remote/Branch Office)",
        "models": ["RL300"]
    },
    
    "SL Series": {
        "description": "Масштабируемые серверы (Scalable)",
        "models": ["SL230s", "SL250s", "SL270s", "SL335s", "SL4540", "SL4545"]
    },
    
    "XL Series": {
        "description": "Серверы для HPC и Big Data",
        "models": ["XL170r", "XL190r", "XL230a", "XL230k", "XL250a", "XL270d", "XL450"]
    },
    
    "BL Series": {
        "description": "Блейд-серверы (Blade)",
        "models": [
            "BL20p", "BL25p", "BL35p", "BL45p",
            "BL260c", "BL280c", "BL420c", "BL460c", "BL465c", "BL480c", "BL490c", "BL660c", "BL680c",
            "BL2x220c"
        ]
    },
    
    "WS Series": {
        "description": "Рабочие станции (Workstations)",
        "models": ["WS460c"]
    },
    
    "Microserver": {
        "description": "Микросерверы",
        "models": ["MicroServer G7", "MicroServer Gen8", "MicroServer Gen10", "MicroServer Gen10+"]
    }
}


# ПРИМЕРЫ КОНКРЕТНЫХ МОДЕЛЕЙ С ТЕХНИЧЕСКИМИ ХАРАКТЕРИСТИКАМИ

def create_proliant_dl_series_examples():
    """Примеры серверов DL Series разных поколений"""
    from data_models import Component, ComponentType, ComponentAttribute
    
    return [
        # DL360 - разные поколения
        Component(
            id="hpe_dl360_g5",
            name="HPE ProLiant DL360 G5",
            component_type=ComponentType.SERVER,
            manufacturer="HPE",
            model="DL360 G5",
            attributes=[
                ComponentAttribute("Категория", "HPE Proliant"),
                ComponentAttribute("Серия", "DL Series"),
                ComponentAttribute("Поколение", "G5"),
                ComponentAttribute("Форм-фактор", "1U Стоечный"),
                ComponentAttribute("Макс. процессоров", "2"),
                ComponentAttribute("Сокет", "Socket 771 (LGA771)"),
                ComponentAttribute("Процессор", "Intel Xeon 5100/5300"),
                ComponentAttribute("Слотов памяти", "8"),
                ComponentAttribute("Макс. памяти", "32", "ГБ"),
                ComponentAttribute("Тип памяти", "DDR2 FBD"),
                ComponentAttribute("Отсеков 2.5\"", "6")
            ]
        ),
        Component(
            id="hpe_dl360_g6",
            name="HPE ProLiant DL360 G6",
            component_type=ComponentType.SERVER,
            manufacturer="HPE",
            model="DL360 G6",
            attributes=[
                ComponentAttribute("Категория", "HPE Proliant"),
                ComponentAttribute("Серия", "DL Series"),
                ComponentAttribute("Поколение", "G6"),
                ComponentAttribute("Форм-фактор", "1U Стоечный"),
                ComponentAttribute("Макс. процессоров", "2"),
                ComponentAttribute("Сокет", "Socket 1366 (LGA1366)"),
                ComponentAttribute("Процессор", "Intel Xeon 5500/5600"),
                ComponentAttribute("Слотов памяти", "18"),
                ComponentAttribute("Макс. памяти", "192", "ГБ"),
                ComponentAttribute("Тип памяти", "DDR3 RDIMM"),
                ComponentAttribute("Отсеков 2.5\"", "8")
            ]
        ),
        Component(
            id="hpe_dl360_g7",
            name="HPE ProLiant DL360 G7",
            component_type=ComponentType.SERVER,
            manufacturer="HPE",
            model="DL360 G7",
            attributes=[
                ComponentAttribute("Категория", "HPE Proliant"),
                ComponentAttribute("Серия", "DL Series"),
                ComponentAttribute("Поколение", "G7"),
                ComponentAttribute("Форм-фактор", "1U Стоечный"),
                ComponentAttribute("Макс. процессоров", "2"),
                ComponentAttribute("Сокет", "Socket 1366 (LGA1366)"),
                ComponentAttribute("Процессор", "Intel Xeon 5600"),
                ComponentAttribute("Слотов памяти", "18"),
                ComponentAttribute("Макс. памяти", "192", "ГБ"),
                ComponentAttribute("Тип памяти", "DDR3 RDIMM"),
                ComponentAttribute("Отсеков 2.5\"", "8")
            ]
        ),
        Component(
            id="hpe_dl360_g8",
            name="HPE ProLiant DL360 G8",
            component_type=ComponentType.SERVER,
            manufacturer="HPE",
            model="DL360 G8",
            attributes=[
                ComponentAttribute("Категория", "HPE Proliant"),
                ComponentAttribute("Серия", "DL Series"),
                ComponentAttribute("Поколение", "G8"),
                ComponentAttribute("Форм-фактор", "1U Стоечный"),
                ComponentAttribute("Макс. процессоров", "2"),
                ComponentAttribute("Сокет", "Socket 2011 (LGA2011)"),
                ComponentAttribute("Процессор", "Intel Xeon E5-2600/E5-2600v2"),
                ComponentAttribute("Слотов памяти", "24"),
                ComponentAttribute("Макс. памяти", "768", "ГБ"),
                ComponentAttribute("Тип памяти", "DDR3 RDIMM/LRDIMM"),
                ComponentAttribute("Отсеков 2.5\"", "10")
            ]
        ),
        Component(
            id="hpe_dl360_g9",
            name="HPE ProLiant DL360 Gen9",
            component_type=ComponentType.SERVER,
            manufacturer="HPE",
            model="DL360 Gen9",
            attributes=[
                ComponentAttribute("Категория", "HPE Proliant"),
                ComponentAttribute("Серия", "DL Series"),
                ComponentAttribute("Поколение", "G9"),
                ComponentAttribute("Форм-фактор", "1U Стоечный"),
                ComponentAttribute("Макс. процессоров", "2"),
                ComponentAttribute("Сокет", "Socket 2011-3 (LGA2011-3)"),
                ComponentAttribute("Процессор", "Intel Xeon E5-2600v3/v4"),
                ComponentAttribute("Слотов памяти", "24"),
                ComponentAttribute("Макс. памяти", "3", "ТБ"),
                ComponentAttribute("Тип памяти", "DDR4 RDIMM/LRDIMM"),
                ComponentAttribute("Отсеков 2.5\"", "10")
            ]
        ),
        Component(
            id="hpe_dl360_g10",
            name="HPE ProLiant DL360 Gen10",
            component_type=ComponentType.SERVER,
            manufacturer="HPE",
            model="DL360 Gen10",
            attributes=[
                ComponentAttribute("Категория", "HPE Proliant"),
                ComponentAttribute("Серия", "DL Series"),
                ComponentAttribute("Поколение", "G10"),
                ComponentAttribute("Форм-фактор", "1U Стоечный"),
                ComponentAttribute("Макс. процессоров", "2"),
                ComponentAttribute("Сокет", "Socket 3647 (LGA3647)"),
                ComponentAttribute("Процессор", "Intel Xeon Scalable 1st/2nd Gen"),
                ComponentAttribute("Слотов памяти", "24"),
                ComponentAttribute("Макс. памяти", "3", "ТБ"),
                ComponentAttribute("Тип памяти", "DDR4 RDIMM/LRDIMM"),
                ComponentAttribute("Отсеков 2.5\"", "10")
            ]
        ),
        Component(
            id="hpe_dl360_g10_plus",
            name="HPE ProLiant DL360 Gen10 Plus",
            component_type=ComponentType.SERVER,
            manufacturer="HPE",
            model="DL360 Gen10 Plus",
            attributes=[
                ComponentAttribute("Категория", "HPE Proliant"),
                ComponentAttribute("Серия", "DL Series"),
                ComponentAttribute("Поколение", "G10+"),
                ComponentAttribute("Форм-фактор", "1U Стоечный"),
                ComponentAttribute("Макс. процессоров", "2"),
                ComponentAttribute("Сокет", "Socket 4189 (LGA4189)"),
                ComponentAttribute("Процессор", "Intel Xeon Scalable 3rd Gen"),
                ComponentAttribute("Слотов памяти", "32"),
                ComponentAttribute("Макс. памяти", "8", "ТБ"),
                ComponentAttribute("Тип памяти", "DDR4 RDIMM/LRDIMM"),
                ComponentAttribute("Отсеков 2.5\"", "12")
            ]
        ),
        Component(
            id="hpe_dl360_g11",
            name="HPE ProLiant DL360 Gen11",
            component_type=ComponentType.SERVER,
            manufacturer="HPE",
            model="DL360 Gen11",
            attributes=[
                ComponentAttribute("Категория", "HPE Proliant"),
                ComponentAttribute("Серия", "DL Series"),
                ComponentAttribute("Поколение", "G11"),
                ComponentAttribute("Форм-фактор", "1U Стоечный"),
                ComponentAttribute("Макс. процессоров", "2"),
                ComponentAttribute("Сокет", "Socket 4677 (LGA4677)"),
                ComponentAttribute("Процессор", "Intel Xeon Scalable 4th/5th Gen"),
                ComponentAttribute("Слотов памяти", "32"),
                ComponentAttribute("Макс. памяти", "8", "ТБ"),
                ComponentAttribute("Тип памяти", "DDR5 RDIMM"),
                ComponentAttribute("Отсеков 2.5\"", "12")
            ]
        ),
        
        # DL380 - популярная модель разных поколений
        Component(
            id="hpe_dl380_g5",
            name="HPE ProLiant DL380 G5",
            component_type=ComponentType.SERVER,
            manufacturer="HPE",
            model="DL380 G5",
            attributes=[
                ComponentAttribute("Категория", "HPE Proliant"),
                ComponentAttribute("Серия", "DL Series"),
                ComponentAttribute("Поколение", "G5"),
                ComponentAttribute("Форм-фактор", "2U Стоечный"),
                ComponentAttribute("Макс. процессоров", "2"),
                ComponentAttribute("Сокет", "Socket 771 (LGA771)"),
                ComponentAttribute("Процессор", "Intel Xeon 5100/5300"),
                ComponentAttribute("Слотов памяти", "8"),
                ComponentAttribute("Макс. памяти", "32", "ГБ"),
                ComponentAttribute("Тип памяти", "DDR2 FBD"),
                ComponentAttribute("Отсеков 3.5\"", "8")
            ]
        ),
        Component(
            id="hpe_dl380_g7",
            name="HPE ProLiant DL380 G7",
            component_type=ComponentType.SERVER,
            manufacturer="HPE",
            model="DL380 G7",
            attributes=[
                ComponentAttribute("Категория", "HPE Proliant"),
                ComponentAttribute("Серия", "DL Series"),
                ComponentAttribute("Поколение", "G7"),
                ComponentAttribute("Форм-фактор", "2U Стоечный"),
                ComponentAttribute("Макс. процессоров", "2"),
                ComponentAttribute("Сокет", "Socket 1366 (LGA1366)"),
                ComponentAttribute("Процессор", "Intel Xeon 5600"),
                ComponentAttribute("Слотов памяти", "18"),
                ComponentAttribute("Макс. памяти", "192", "ГБ"),
                ComponentAttribute("Тип памяти", "DDR3 RDIMM"),
                ComponentAttribute("Отсеков 3.5\"", "8")
            ]
        ),
        Component(
            id="hpe_dl380_g9",
            name="HPE ProLiant DL380 Gen9",
            component_type=ComponentType.SERVER,
            manufacturer="HPE",
            model="DL380 Gen9",
            attributes=[
                ComponentAttribute("Категория", "HPE Proliant"),
                ComponentAttribute("Серия", "DL Series"),
                ComponentAttribute("Поколение", "G9"),
                ComponentAttribute("Форм-фактор", "2U Стоечный"),
                ComponentAttribute("Макс. процессоров", "2"),
                ComponentAttribute("Сокет", "Socket 2011-3 (LGA2011-3)"),
                ComponentAttribute("Процессор", "Intel Xeon E5-2600v3/v4"),
                ComponentAttribute("Слотов памяти", "24"),
                ComponentAttribute("Макс. памяти", "3", "ТБ"),
                ComponentAttribute("Тип памяти", "DDR4 RDIMM/LRDIMM"),
                ComponentAttribute("Отсеков 3.5\"", "12")
            ]
        ),
        Component(
            id="hpe_dl380_g10",
            name="HPE ProLiant DL380 Gen10",
            component_type=ComponentType.SERVER,
            manufacturer="HPE",
            model="DL380 Gen10",
            attributes=[
                ComponentAttribute("Категория", "HPE Proliant"),
                ComponentAttribute("Серия", "DL Series"),
                ComponentAttribute("Поколение", "G10"),
                ComponentAttribute("Форм-фактор", "2U Стоечный"),
                ComponentAttribute("Макс. процессоров", "2"),
                ComponentAttribute("Сокет", "Socket 3647 (LGA3647)"),
                ComponentAttribute("Процессор", "Intel Xeon Scalable 1st/2nd Gen"),
                ComponentAttribute("Слотов памяти", "24"),
                ComponentAttribute("Макс. памяти", "3", "ТБ"),
                ComponentAttribute("Тип памяти", "DDR4 RDIMM/LRDIMM"),
                ComponentAttribute("Отсеков 3.5\"", "12")
            ]
        ),
        
        # Другие модели DL Series
        Component(
            id="hpe_dl20_g10",
            name="HPE ProLiant DL20 Gen10",
            component_type=ComponentType.SERVER,
            manufacturer="HPE",
            model="DL20 Gen10",
            attributes=[
                ComponentAttribute("Категория", "HPE Proliant"),
                ComponentAttribute("Серия", "DL Series"),
                ComponentAttribute("Поколение", "G10"),
                ComponentAttribute("Форм-фактор", "1U Стоечный"),
                ComponentAttribute("Макс. процессоров", "1"),
                ComponentAttribute("Сокет", "Socket 1151 (LGA1151)"),
                ComponentAttribute("Процессор", "Intel Xeon E-2100"),
                ComponentAttribute("Слотов памяти", "4"),
                ComponentAttribute("Макс. памяти", "64", "ГБ"),
                ComponentAttribute("Тип памяти", "DDR4 UDIMM"),
                ComponentAttribute("Отсеков 2.5\"", "4")
            ]
        ),
        Component(
            id="hpe_dl325_g10_plus",
            name="HPE ProLiant DL325 Gen10 Plus",
            component_type=ComponentType.SERVER,
            manufacturer="HPE",
            model="DL325 Gen10 Plus",
            attributes=[
                ComponentAttribute("Категория", "HPE Proliant"),
                ComponentAttribute("Серия", "DL Series"),
                ComponentAttribute("Поколение", "G10+"),
                ComponentAttribute("Форм-фактор", "1U Стоечный"),
                ComponentAttribute("Макс. процессоров", "1"),
                ComponentAttribute("Сокет", "Socket SP3"),
                ComponentAttribute("Процессор", "AMD EPYC 7002/7003"),
                ComponentAttribute("Слотов памяти", "16"),
                ComponentAttribute("Макс. памяти", "4", "ТБ"),
                ComponentAttribute("Тип памяти", "DDR4 RDIMM"),
                ComponentAttribute("Отсеков 2.5\"", "10")
            ]
        ),
        Component(
            id="hpe_dl580_g10",
            name="HPE ProLiant DL580 Gen10",
            component_type=ComponentType.SERVER,
            manufacturer="HPE",
            model="DL580 Gen10",
            attributes=[
                ComponentAttribute("Категория", "HPE Proliant"),
                ComponentAttribute("Серия", "DL Series"),
                ComponentAttribute("Поколение", "G10"),
                ComponentAttribute("Форм-фактор", "4U Стоечный"),
                ComponentAttribute("Макс. процессоров", "4"),
                ComponentAttribute("Сокет", "Socket 3647 (LGA3647)"),
                ComponentAttribute("Процессор", "Intel Xeon Scalable 1st/2nd Gen"),
                ComponentAttribute("Слотов памяти", "48"),
                ComponentAttribute("Макс. памяти", "6", "ТБ"),
                ComponentAttribute("Тип памяти", "DDR4 RDIMM/LRDIMM"),
                ComponentAttribute("Отсеков 2.5\"", "16")
            ]
        )
    ]


def create_proliant_ml_series_examples():
    """Примеры башенных серверов ML Series"""
    from data_models import Component, ComponentType, ComponentAttribute
    
    return [
        Component(
            id="hpe_ml110_g10",
            name="HPE ProLiant ML110 Gen10",
            component_type=ComponentType.SERVER,
            manufacturer="HPE",
            model="ML110 Gen10",
            attributes=[
                ComponentAttribute("Категория", "HPE Proliant"),
                ComponentAttribute("Серия", "ML Series"),
                ComponentAttribute("Поколение", "G10"),
                ComponentAttribute("Форм-фактор", "Башенный (Tower)"),
                ComponentAttribute("Макс. процессоров", "1"),
                ComponentAttribute("Сокет", "Socket 3647 (LGA3647)"),
                ComponentAttribute("Процессор", "Intel Xeon Bronze/Silver/Gold"),
                ComponentAttribute("Слотов памяти", "4"),
                ComponentAttribute("Макс. памяти", "64", "ГБ"),
                ComponentAttribute("Тип памяти", "DDR4 RDIMM"),
                ComponentAttribute("Отсеков 3.5\"", "4")
            ]
        ),
        Component(
            id="hpe_ml350_g5",
            name="HPE ProLiant ML350 G5",
            component_type=ComponentType.SERVER,
            manufacturer="HPE",
            model="ML350 G5",
            attributes=[
                ComponentAttribute("Категория", "HPE Proliant"),
                ComponentAttribute("Серия", "ML Series"),
                ComponentAttribute("Поколение", "G5"),
                ComponentAttribute("Форм-фактор", "Башенный (Tower)"),
                ComponentAttribute("Макс. процессоров", "2"),
                ComponentAttribute("Сокет", "Socket 771 (LGA771)"),
                ComponentAttribute("Процессор", "Intel Xeon 5100/5300"),
                ComponentAttribute("Слотов памяти", "8"),
                ComponentAttribute("Макс. памяти", "32", "ГБ"),
                ComponentAttribute("Тип памяти", "DDR2 FBD"),
                ComponentAttribute("Отсеков 3.5\"", "8")
            ]
        ),
        Component(
            id="hpe_ml350_g10",
            name="HPE ProLiant ML350 Gen10",
            component_type=ComponentType.SERVER,
            manufacturer="HPE",
            model="ML350 Gen10",
            attributes=[
                ComponentAttribute("Категория", "HPE Proliant"),
                ComponentAttribute("Серия", "ML Series"),
                ComponentAttribute("Поколение", "G10"),
                ComponentAttribute("Форм-фактор", "Башенный (Tower)"),
                ComponentAttribute("Макс. процессоров", "2"),
                ComponentAttribute("Сокет", "Socket 3647 (LGA3647)"),
                ComponentAttribute("Процессор", "Intel Xeon Scalable 1st/2nd Gen"),
                ComponentAttribute("Слотов памяти", "24"),
                ComponentAttribute("Макс. памяти", "3", "ТБ"),
                ComponentAttribute("Тип памяти", "DDR4 RDIMM/LRDIMM"),
                ComponentAttribute("Отсеков 3.5\"", "8")
            ]
        ),
        Component(
            id="hpe_ml30_g10",
            name="HPE ProLiant ML30 Gen10",
            component_type=ComponentType.SERVER,
            manufacturer="HPE",
            model="ML30 Gen10",
            attributes=[
                ComponentAttribute("Категория", "HPE Proliant"),
                ComponentAttribute("Серия", "ML Series"),
                ComponentAttribute("Поколение", "G10"),
                ComponentAttribute("Форм-фактор", "Башенный (Tower)"),
                ComponentAttribute("Макс. процессоров", "1"),
                ComponentAttribute("Сокет", "Socket 1151 (LGA1151)"),
                ComponentAttribute("Процессор", "Intel Xeon E-2100"),
                ComponentAttribute("Слотов памяти", "4"),
                ComponentAttribute("Макс. памяти", "64", "ГБ"),
                ComponentAttribute("Тип памяти", "DDR4 UDIMM"),
                ComponentAttribute("Отсеков 3.5\"", "4")
            ]
        )
    ]


# СТРУКТУРА ДЛЯ ВЕБА - РАСШИРЕННАЯ
def get_proliant_structure_for_web():
    """Полная структура HPE Proliant для веб-интерфейса"""
    
    web_structure = {
        "category": "HPE Proliant",
        "series": []
    }
    
    # DL Series
    dl_series = {
        "id": "dl_series",
        "name": "DL Series",
        "description": "Стоечные серверы (Rack-mount)",
        "generations": []
    }
    
    for gen, models in HPE_PROLIANT_STRUCTURE["DL Series"]["generations"].items():
        dl_series["generations"].append({
            "id": f"dl_{gen.lower()}",
            "name": gen,
            "models": [{"id": model.lower().replace(" ", "_"), "name": model} for model in models]
        })
    
    web_structure["series"].append(dl_series)
    
    # ML Series
    ml_series = {
        "id": "ml_series",
        "name": "ML Series",
        "description": "Башенные серверы (Tower)",
        "generations": []
    }
    
    for gen, models in HPE_PROLIANT_STRUCTURE["ML Series"]["generations"].items():
        ml_series["generations"].append({
            "id": f"ml_{gen.lower()}",
            "name": gen,
            "models": [{"id": model.lower().replace(" ", "_"), "name": model} for model in models]
        })
    
    web_structure["series"].append(ml_series)
    
    # DX Series
    web_structure["series"].append({
        "id": "dx_series",
        "name": "DX Series",
        "description": "Серверы для объектного хранилища",
        "models": [{"id": model.lower().replace(" ", "_"), "name": model} 
                  for model in HPE_PROLIANT_STRUCTURE["DX Series"]["models"]]
    })
    
    # RL Series
    web_structure["series"].append({
        "id": "rl_series",
        "name": "RL Series",
        "description": "Компактные серверы",
        "models": [{"id": model.lower().replace(" ", "_"), "name": model} 
                  for model in HPE_PROLIANT_STRUCTURE["RL Series"]["models"]]
    })
    
    # SL Series
    web_structure["series"].append({
        "id": "sl_series",
        "name": "SL Series",
        "description": "Масштабируемые серверы",
        "models": [{"id": model.lower().replace(" ", "_"), "name": model} 
                  for model in HPE_PROLIANT_STRUCTURE["SL Series"]["models"]]
    })
    
    # XL Series
    web_structure["series"].append({
        "id": "xl_series",
        "name": "XL Series",
        "description": "Серверы для HPC и Big Data",
        "models": [{"id": model.lower().replace(" ", "_"), "name": model} 
                  for model in HPE_PROLIANT_STRUCTURE["XL Series"]["models"]]
    })
    
    # BL Series
    web_structure["series"].append({
        "id": "bl_series",
        "name": "BL Series",
        "description": "Блейд-серверы",
        "models": [{"id": model.lower().replace(" ", "_"), "name": model} 
                  for model in HPE_PROLIANT_STRUCTURE["BL Series"]["models"]]
    })
    
    return web_structure


if __name__ == "__main__":
    print("РАСШИРЕННАЯ СТРУКТУРА HPE PROLIANT")
    print("=" * 80)
    
    for series_name, series_info in HPE_PROLIANT_STRUCTURE.items():
        print(f"\n{series_name}: {series_info['description']}")
        
        if "generations" in series_info:
            print("  Поколения:")
            for gen, models in series_info["generations"].items():
                print(f"    {gen}: {len(models)} моделей ({', '.join(models[:5])}...)")
        elif "models" in series_info:
            print(f"  Моделей: {len(series_info['models'])}")
            print(f"  {', '.join(series_info['models'][:5])}...")
    
    # СТАТИСТИКА
    print("\n" + "=" * 80)
    print("СТАТИСТИКА:")
    
    total_models = 0
    for series_name, series_info in HPE_PROLIANT_STRUCTURE.items():
        if "generations" in series_info:
            series_count = sum(len(models) for models in series_info["generations"].values())
            print(f"  {series_name}: {series_count} моделей в {len(series_info['generations'])} поколениях")
            total_models += series_count
        elif "models" in series_info:
            print(f"  {series_name}: {len(series_info['models'])} моделей")
            total_models += len(series_info['models'])
    
    print(f"\nВСЕГО МОДЕЛЕЙ: {total_models}")
    
    # ПРИМЕРЫ С ХАРАКТЕРИСТИКАМИ
    print("\n" + "=" * 80)
    print(f"ПРИМЕРОВ С ТЕХНИЧЕСКИМИ ХАРАКТЕРИСТИКАМИ:")
    dl_examples = create_proliant_dl_series_examples()
    ml_examples = create_proliant_ml_series_examples()
    print(f"  DL Series: {len(dl_examples)} моделей")
    print(f"  ML Series: {len(ml_examples)} моделей")
    print(f"  ВСЕГО: {len(dl_examples) + len(ml_examples)} моделей")

