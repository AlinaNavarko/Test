"""
Полная структура категорий серверов
На основе silworks.com
"""

from data_models import Component, ComponentType, ComponentAttribute

# СТРУКТУРА КАТЕГОРИЙ СЕРВЕРОВ

SERVER_CATEGORIES = {
    "HPE Proliant": {
        "description": "Стоечные и башенные серверы HPE",
        "series": [
            "ML Series",      # Башенные серверы (Tower)
            "DL Series",      # Стоечные серверы (Rack)
            "BL Series",      # Блейд-серверы
            "SL Series",      # Масштабируемые серверы
            "Gen8 Series",
            "Gen9 Series",
            "Gen10 Series",
            "Gen10 Plus"
        ]
    },
    
    "HPE StorageWorks": {
        "description": "Системы хранения данных HPE",
        "series": [
            "MSA Series",     # Modular Smart Array
            "StoreEasy",      # NAS хранилища
            "D-Series",       # Дисковые полки
            "StoreOnce",      # Дедупликация
            "3PAR"            # Высокопроизводительные СХД
        ]
    },
    
    "HPE Apollo": {
        "description": "Высокопроизводительные вычисления",
        "series": [
            "Apollo 2000",
            "Apollo 4000",
            "Apollo 6000",
            "Apollo 8000"
        ]
    },
    
    "Dell PowerEdge": {
        "description": "Серверы Dell",
        "series": [
            "T Series",       # Башенные серверы
            "R Series",       # Стоечные серверы
            "C Series",       # Облачные серверы
            "M Series",       # Модульные серверы
            "FC Series",      # Blade серверы
            "MX Series",      # Модульная инфраструктура
            "XE Series"       # Экстремальные вычисления
        ]
    },
    
    "Dell PowerVault": {
        "description": "Системы хранения Dell",
        "series": [
            "MD Series",      # Модульные дисковые массивы
            "ME Series",      # Entry-level хранилища
            "NX Series",      # NAS решения
            "TL Series"       # Ленточные библиотеки
        ]
    },
    
    "Dell EqualLogic": {
        "description": "iSCSI SAN массивы Dell",
        "series": [
            "PS Series",      # Performance Storage
            "FS Series"       # Файловые системы
        ]
    },
    
    "EMC CX VNX": {
        "description": "Системы хранения EMC",
        "series": [
            "VNX Series",
            "VNXe Series",
            "CX3 Series",
            "CX4 Series"
        ]
    },
    
    "IBM SystemX": {
        "description": "Серверы IBM x86",
        "series": [
            "x3000 Series",   # Башенные серверы
            "x3500 Series",   # Стоечные серверы среднего уровня
            "x3600 Series",   # Стоечные серверы высокого уровня
            "x3850 Series",   # Масштабируемые серверы
            "Flex System",    # Модульная инфраструктура
            "BladeCenter"     # Блейд-серверы
        ]
    }
}


# ПРИМЕРЫ СЕРВЕРОВ ДЛЯ КАЖДОЙ КАТЕГОРИИ

def create_hpe_proliant_servers():
    """HPE Proliant серверы"""
    return [
        # ML Series (Tower)
        Component(
            id="hpe_ml110_gen10",
            name="HPE ProLiant ML110 Gen10",
            component_type=ComponentType.SERVER,
            manufacturer="HPE",
            model="ML110 Gen10",
            attributes=[
                ComponentAttribute("Категория", "HPE Proliant"),
                ComponentAttribute("Серия", "ML Series"),
                ComponentAttribute("Форм-фактор", "Башенный (Tower)"),
                ComponentAttribute("Макс. процессоров", "1"),
                ComponentAttribute("Сокет", "Socket 3647"),
                ComponentAttribute("Слотов памяти", "4"),
                ComponentAttribute("Макс. памяти", "64", "ГБ"),
                ComponentAttribute("Тип памяти", "DDR4"),
                ComponentAttribute("Отсеков 3.5\"", "4")
            ],
            description="Начальный башенный сервер для малого бизнеса"
        ),
        Component(
            id="hpe_ml350_gen10",
            name="HPE ProLiant ML350 Gen10",
            component_type=ComponentType.SERVER,
            manufacturer="HPE",
            model="ML350 Gen10",
            attributes=[
                ComponentAttribute("Категория", "HPE Proliant"),
                ComponentAttribute("Серия", "ML Series"),
                ComponentAttribute("Форм-фактор", "Башенный (Tower)"),
                ComponentAttribute("Макс. процессоров", "2"),
                ComponentAttribute("Сокет", "Socket 3647"),
                ComponentAttribute("Слотов памяти", "24"),
                ComponentAttribute("Макс. памяти", "3", "ТБ"),
                ComponentAttribute("Тип памяти", "DDR4"),
                ComponentAttribute("Отсеков 3.5\"", "8")
            ],
            description="Универсальный башенный сервер с двумя процессорами"
        ),
        
        # DL Series (Rack)
        Component(
            id="hpe_dl20_gen10",
            name="HPE ProLiant DL20 Gen10",
            component_type=ComponentType.SERVER,
            manufacturer="HPE",
            model="DL20 Gen10",
            attributes=[
                ComponentAttribute("Категория", "HPE Proliant"),
                ComponentAttribute("Серия", "DL Series"),
                ComponentAttribute("Форм-фактор", "1U Стоечный"),
                ComponentAttribute("Макс. процессоров", "1"),
                ComponentAttribute("Сокет", "Socket 1151"),
                ComponentAttribute("Слотов памяти", "4"),
                ComponentAttribute("Макс. памяти", "64", "ГБ"),
                ComponentAttribute("Тип памяти", "DDR4"),
                ComponentAttribute("Отсеков 2.5\"", "4")
            ],
            description="Компактный стоечный сервер 1U"
        ),
        Component(
            id="hpe_dl360_gen10",
            name="HPE ProLiant DL360 Gen10",
            component_type=ComponentType.SERVER,
            manufacturer="HPE",
            model="DL360 Gen10",
            attributes=[
                ComponentAttribute("Категория", "HPE Proliant"),
                ComponentAttribute("Серия", "DL Series"),
                ComponentAttribute("Форм-фактор", "1U Стоечный"),
                ComponentAttribute("Макс. процессоров", "2"),
                ComponentAttribute("Сокет", "Socket 3647"),
                ComponentAttribute("Слотов памяти", "24"),
                ComponentAttribute("Макс. памяти", "3", "ТБ"),
                ComponentAttribute("Тип памяти", "DDR4"),
                ComponentAttribute("Отсеков 2.5\"", "10")
            ],
            description="Популярный стоечный сервер 1U для ЦОД"
        ),
        Component(
            id="hpe_dl380_gen10",
            name="HPE ProLiant DL380 Gen10",
            component_type=ComponentType.SERVER,
            manufacturer="HPE",
            model="DL380 Gen10",
            attributes=[
                ComponentAttribute("Категория", "HPE Proliant"),
                ComponentAttribute("Серия", "DL Series"),
                ComponentAttribute("Форм-фактор", "2U Стоечный"),
                ComponentAttribute("Макс. процессоров", "2"),
                ComponentAttribute("Сокет", "Socket 3647"),
                ComponentAttribute("Слотов памяти", "24"),
                ComponentAttribute("Макс. памяти", "3", "ТБ"),
                ComponentAttribute("Тип памяти", "DDR4"),
                ComponentAttribute("Отсеков 2.5\"", "12")
            ],
            description="Универсальный стоечный сервер 2U"
        ),
        Component(
            id="hpe_dl580_gen10",
            name="HPE ProLiant DL580 Gen10",
            component_type=ComponentType.SERVER,
            manufacturer="HPE",
            model="DL580 Gen10",
            attributes=[
                ComponentAttribute("Категория", "HPE Proliant"),
                ComponentAttribute("Серия", "DL Series"),
                ComponentAttribute("Форм-фактор", "4U Стоечный"),
                ComponentAttribute("Макс. процессоров", "4"),
                ComponentAttribute("Сокет", "Socket 3647"),
                ComponentAttribute("Слотов памяти", "48"),
                ComponentAttribute("Макс. памяти", "6", "ТБ"),
                ComponentAttribute("Тип памяти", "DDR4"),
                ComponentAttribute("Отсеков 2.5\"", "16")
            ],
            description="Высокопроизводительный масштабируемый сервер 4U"
        )
    ]


def create_dell_poweredge_servers():
    """Dell PowerEdge серверы"""
    return [
        # T Series (Tower)
        Component(
            id="dell_t140",
            name="Dell PowerEdge T140",
            component_type=ComponentType.SERVER,
            manufacturer="Dell",
            model="T140",
            attributes=[
                ComponentAttribute("Категория", "Dell PowerEdge"),
                ComponentAttribute("Серия", "T Series"),
                ComponentAttribute("Форм-фактор", "Башенный (Tower)"),
                ComponentAttribute("Макс. процессоров", "1"),
                ComponentAttribute("Сокет", "Socket 1151"),
                ComponentAttribute("Слотов памяти", "4"),
                ComponentAttribute("Макс. памяти", "64", "ГБ"),
                ComponentAttribute("Тип памяти", "DDR4"),
                ComponentAttribute("Отсеков 3.5\"", "4")
            ],
            description="Начальный башенный сервер Dell"
        ),
        Component(
            id="dell_t340",
            name="Dell PowerEdge T340",
            component_type=ComponentType.SERVER,
            manufacturer="Dell",
            model="T340",
            attributes=[
                ComponentAttribute("Категория", "Dell PowerEdge"),
                ComponentAttribute("Серия", "T Series"),
                ComponentAttribute("Форм-фактор", "Башенный (Tower)"),
                ComponentAttribute("Макс. процессоров", "1"),
                ComponentAttribute("Сокет", "Socket 1151"),
                ComponentAttribute("Слотов памяти", "4"),
                ComponentAttribute("Макс. памяти", "64", "ГБ"),
                ComponentAttribute("Тип памяти", "DDR4"),
                ComponentAttribute("Отсеков 3.5\"", "8")
            ],
            description="Башенный сервер с расширенными возможностями"
        ),
        
        # R Series (Rack)
        Component(
            id="dell_r240",
            name="Dell PowerEdge R240",
            component_type=ComponentType.SERVER,
            manufacturer="Dell",
            model="R240",
            attributes=[
                ComponentAttribute("Категория", "Dell PowerEdge"),
                ComponentAttribute("Серия", "R Series"),
                ComponentAttribute("Форм-фактор", "1U Стоечный"),
                ComponentAttribute("Макс. процессоров", "1"),
                ComponentAttribute("Сокет", "Socket 1151"),
                ComponentAttribute("Слотов памяти", "4"),
                ComponentAttribute("Макс. памяти", "64", "ГБ"),
                ComponentAttribute("Тип памяти", "DDR4"),
                ComponentAttribute("Отсеков 3.5\"", "4")
            ],
            description="Компактный стоечный сервер 1U"
        ),
        Component(
            id="dell_r440",
            name="Dell PowerEdge R440",
            component_type=ComponentType.SERVER,
            manufacturer="Dell",
            model="R440",
            attributes=[
                ComponentAttribute("Категория", "Dell PowerEdge"),
                ComponentAttribute("Серия", "R Series"),
                ComponentAttribute("Форм-фактор", "1U Стоечный"),
                ComponentAttribute("Макс. процессоров", "2"),
                ComponentAttribute("Сокет", "Socket 3647"),
                ComponentAttribute("Слотов памяти", "16"),
                ComponentAttribute("Макс. памяти", "768", "ГБ"),
                ComponentAttribute("Тип памяти", "DDR4"),
                ComponentAttribute("Отсеков 2.5\"", "10")
            ],
            description="Стоечный сервер 1U для рабочих нагрузок"
        ),
        Component(
            id="dell_r640",
            name="Dell PowerEdge R640",
            component_type=ComponentType.SERVER,
            manufacturer="Dell",
            model="R640",
            attributes=[
                ComponentAttribute("Категория", "Dell PowerEdge"),
                ComponentAttribute("Серия", "R Series"),
                ComponentAttribute("Форм-фактор", "1U Стоечный"),
                ComponentAttribute("Макс. процессоров", "2"),
                ComponentAttribute("Сокет", "Socket 3647"),
                ComponentAttribute("Слотов памяти", "24"),
                ComponentAttribute("Макс. памяти", "3", "ТБ"),
                ComponentAttribute("Тип памяти", "DDR4"),
                ComponentAttribute("Отсеков 2.5\"", "10")
            ],
            description="Универсальный стоечный сервер 1U"
        ),
        Component(
            id="dell_r740",
            name="Dell PowerEdge R740",
            component_type=ComponentType.SERVER,
            manufacturer="Dell",
            model="R740",
            attributes=[
                ComponentAttribute("Категория", "Dell PowerEdge"),
                ComponentAttribute("Серия", "R Series"),
                ComponentAttribute("Форм-фактор", "2U Стоечный"),
                ComponentAttribute("Макс. процессоров", "2"),
                ComponentAttribute("Сокет", "Socket 3647"),
                ComponentAttribute("Слотов памяти", "24"),
                ComponentAttribute("Макс. памяти", "3", "ТБ"),
                ComponentAttribute("Тип памяти", "DDR4"),
                ComponentAttribute("Отсеков 2.5\"", "16")
            ],
            description="Стоечный сервер 2U для бизнес-приложений"
        ),
        Component(
            id="dell_r940",
            name="Dell PowerEdge R940",
            component_type=ComponentType.SERVER,
            manufacturer="Dell",
            model="R940",
            attributes=[
                ComponentAttribute("Категория", "Dell PowerEdge"),
                ComponentAttribute("Серия", "R Series"),
                ComponentAttribute("Форм-фактор", "4U Стоечный"),
                ComponentAttribute("Макс. процессоров", "4"),
                ComponentAttribute("Сокет", "Socket 3647"),
                ComponentAttribute("Слотов памяти", "48"),
                ComponentAttribute("Макс. памяти", "6", "ТБ"),
                ComponentAttribute("Тип памяти", "DDR4"),
                ComponentAttribute("Отсеков 2.5\"", "24")
            ],
            description="Масштабируемый сервер 4U для критичных нагрузок"
        )
    ]


def create_ibm_systemx_servers():
    """IBM SystemX серверы"""
    return [
        Component(
            id="ibm_x3250_m6",
            name="IBM System x3250 M6",
            component_type=ComponentType.SERVER,
            manufacturer="IBM",
            model="x3250 M6",
            attributes=[
                ComponentAttribute("Категория", "IBM SystemX"),
                ComponentAttribute("Серия", "x3000 Series"),
                ComponentAttribute("Форм-фактор", "1U Стоечный"),
                ComponentAttribute("Макс. процессоров", "1"),
                ComponentAttribute("Сокет", "Socket 1150"),
                ComponentAttribute("Слотов памяти", "4"),
                ComponentAttribute("Макс. памяти", "32", "ГБ"),
                ComponentAttribute("Тип памяти", "DDR3"),
                ComponentAttribute("Отсеков 3.5\"", "4")
            ],
            description="Компактный стоечный сервер 1U"
        ),
        Component(
            id="ibm_x3550_m5",
            name="IBM System x3550 M5",
            component_type=ComponentType.SERVER,
            manufacturer="IBM",
            model="x3550 M5",
            attributes=[
                ComponentAttribute("Категория", "IBM SystemX"),
                ComponentAttribute("Серия", "x3500 Series"),
                ComponentAttribute("Форм-фактор", "1U Стоечный"),
                ComponentAttribute("Макс. процессоров", "2"),
                ComponentAttribute("Сокет", "Socket 2011-3"),
                ComponentAttribute("Слотов памяти", "24"),
                ComponentAttribute("Макс. памяти", "768", "ГБ"),
                ComponentAttribute("Тип памяти", "DDR4"),
                ComponentAttribute("Отсеков 2.5\"", "8")
            ],
            description="Стоечный сервер 1U среднего уровня"
        ),
        Component(
            id="ibm_x3650_m5",
            name="IBM System x3650 M5",
            component_type=ComponentType.SERVER,
            manufacturer="IBM",
            model="x3650 M5",
            attributes=[
                ComponentAttribute("Категория", "IBM SystemX"),
                ComponentAttribute("Серия", "x3600 Series"),
                ComponentAttribute("Форм-фактор", "2U Стоечный"),
                ComponentAttribute("Макс. процессоров", "2"),
                ComponentAttribute("Сокет", "Socket 2011-3"),
                ComponentAttribute("Слотов памяти", "24"),
                ComponentAttribute("Макс. памяти", "1.5", "ТБ"),
                ComponentAttribute("Тип памяти", "DDR4"),
                ComponentAttribute("Отсеков 2.5\"", "16")
            ],
            description="Универсальный стоечный сервер 2U"
        ),
        Component(
            id="ibm_x3850_x6",
            name="IBM System x3850 X6",
            component_type=ComponentType.SERVER,
            manufacturer="IBM",
            model="x3850 X6",
            attributes=[
                ComponentAttribute("Категория", "IBM SystemX"),
                ComponentAttribute("Серия", "x3850 Series"),
                ComponentAttribute("Форм-фактор", "4U Стоечный"),
                ComponentAttribute("Макс. процессоров", "4"),
                ComponentAttribute("Сокет", "Socket 2011-3"),
                ComponentAttribute("Слотов памяти", "96"),
                ComponentAttribute("Макс. памяти", "12", "ТБ"),
                ComponentAttribute("Тип памяти", "DDR4"),
                ComponentAttribute("Отсеков 2.5\"", "16")
            ],
            description="Масштабируемый сервер 4U для критичных приложений"
        )
    ]


# СТРУКТУРА ДЛЯ ВЕБА
def get_server_structure_for_web():
    """Структура для отображения на веб-сайте"""
    return {
        "categories": [
            {
                "id": "hpe_proliant",
                "name": "HPE Proliant",
                "description": "Стоечные и башенные серверы HPE",
                "icon": "🖥️",
                "series": [
                    {"id": "ml_series", "name": "ML Series", "description": "Башенные серверы"},
                    {"id": "dl_series", "name": "DL Series", "description": "Стоечные серверы"},
                    {"id": "bl_series", "name": "BL Series", "description": "Блейд-серверы"}
                ]
            },
            {
                "id": "hpe_storageworks",
                "name": "HPE StorageWorks",
                "description": "Системы хранения данных HPE",
                "icon": "💾",
                "series": [
                    {"id": "msa_series", "name": "MSA Series", "description": "Modular Smart Array"},
                    {"id": "storeeasy", "name": "StoreEasy", "description": "NAS хранилища"}
                ]
            },
            {
                "id": "hpe_apollo",
                "name": "HPE Apollo",
                "description": "Высокопроизводительные вычисления",
                "icon": "⚡",
                "series": [
                    {"id": "apollo_2000", "name": "Apollo 2000"},
                    {"id": "apollo_4000", "name": "Apollo 4000"}
                ]
            },
            {
                "id": "dell_poweredge",
                "name": "Dell PowerEdge",
                "description": "Серверы Dell",
                "icon": "🖥️",
                "series": [
                    {"id": "t_series", "name": "T Series", "description": "Башенные серверы"},
                    {"id": "r_series", "name": "R Series", "description": "Стоечные серверы"},
                    {"id": "c_series", "name": "C Series", "description": "Облачные серверы"}
                ]
            },
            {
                "id": "dell_powervault",
                "name": "Dell PowerVault",
                "description": "Системы хранения Dell",
                "icon": "💾",
                "series": [
                    {"id": "md_series", "name": "MD Series"},
                    {"id": "me_series", "name": "ME Series"}
                ]
            },
            {
                "id": "dell_equallogic",
                "name": "Dell EqualLogic",
                "description": "iSCSI SAN массивы",
                "icon": "🔷",
                "series": [
                    {"id": "ps_series", "name": "PS Series"}
                ]
            },
            {
                "id": "emc_cx_vnx",
                "name": "EMC CX VNX",
                "description": "Системы хранения EMC",
                "icon": "💾",
                "series": [
                    {"id": "vnx_series", "name": "VNX Series"},
                    {"id": "vnxe_series", "name": "VNXe Series"}
                ]
            },
            {
                "id": "ibm_systemx",
                "name": "IBM SystemX",
                "description": "Серверы IBM x86",
                "icon": "🖥️",
                "series": [
                    {"id": "x3000_series", "name": "x3000 Series", "description": "Башенные"},
                    {"id": "x3500_series", "name": "x3500 Series", "description": "Стоечные средние"},
                    {"id": "x3600_series", "name": "x3600 Series", "description": "Стоечные высокие"}
                ]
            }
        ]
    }


if __name__ == "__main__":
    # Вывести структуру
    print("КАТЕГОРИИ СЕРВЕРОВ:")
    print("=" * 60)
    
    for category, info in SERVER_CATEGORIES.items():
        print(f"\n{category}")
        print(f"  {info['description']}")
        print(f"  Серии: {', '.join(info['series'])}")
    
    print("\n\n" + "=" * 60)
    print(f"Всего категорий: {len(SERVER_CATEGORIES)}")
    
    # Подсчитать серверы
    hpe_count = len(create_hpe_proliant_servers())
    dell_count = len(create_dell_poweredge_servers())
    ibm_count = len(create_ibm_systemx_servers())
    
    print(f"\nПримеры серверов:")
    print(f"  HPE Proliant: {hpe_count}")
    print(f"  Dell PowerEdge: {dell_count}")
    print(f"  IBM SystemX: {ibm_count}")
    print(f"  ВСЕГО: {hpe_count + dell_count + ibm_count}")

