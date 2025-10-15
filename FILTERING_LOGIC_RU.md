# Логика фильтрации компонентов

## Схема работы

```
ШАГИ ПОЛЬЗОВАТЕЛЯ                    ЧТО ПРОИСХОДИТ В СИСТЕМЕ

1. Открыл сайт                       Показать ВСЕ серверы
   |
   v
2. Выбрал HP ML350 G4p               Добавить в конфигурацию
   |                                 Запомнить: Socket 604, DDR2
   v
3. Открыл раздел "Процессоры"        get_available_components(PROCESSOR)
   |                                 |
   |                                 v
   |                                 Проверить КАЖДЫЙ процессор:
   |                                 - Intel Xeon 3.0 (604) ✅ Совместим
   |                                 - Intel Xeon 3.2 (604) ✅ Совместим  
   |                                 - Intel Xeon E5620 (1366) ❌ Не совместим
   |                                 - Intel Xeon X5670 (1366) ❌ Не совместим
   v
   Видит ТОЛЬКО:                     Вернуть только ✅ компоненты
   • Intel Xeon 3.0 ГГц
   • Intel Xeon 3.2 ГГц
   |
   v
4. Выбрал Intel Xeon 3.0             Добавить в конфигурацию
   |
   v
5. Открыл раздел "Память"            get_available_components(MEMORY)
   |                                 |
   |                                 v
   |                                 Проверить КАЖДУЮ память:
   |                                 - Kingston 1GB DDR2 ✅ Совместима
   |                                 - Corsair 2GB DDR2 ✅ Совместима
   |                                 - Samsung 4GB DDR3 ❌ Не совместима
   |                                 - Crucial 8GB DDR3 ❌ Не совместима
   v
   Видит ТОЛЬКО:                     Вернуть только ✅ компоненты
   • Kingston 1 ГБ DDR2-400
   • Corsair 2 ГБ DDR2-533
```

## Примеры матрицы совместимости

### Для HP ML350 G4p

```python
"hp_ml350g4p": [
    "intel_xeon_3_0_604",      # ✅ Socket 604
    "intel_xeon_3_2_604",      # ✅ Socket 604
    "kingston_1gb_ddr2_400",   # ✅ DDR2
    "corsair_2gb_ddr2_533",    # ✅ DDR2
    "hp_460w_psu",             # ✅ HP БП
    # НЕТ процессоров Socket 1366
    # НЕТ памяти DDR3
    # НЕТ Dell/IBM блоков питания
]
```

### Для Dell R710

```python
"dell_poweredge_r710": [
    "intel_xeon_e5620",        # ✅ Socket 1366
    "intel_xeon_x5670",        # ✅ Socket 1366
    "samsung_4gb_ddr3_1333",   # ✅ DDR3
    "crucial_8gb_ddr3_1600",   # ✅ DDR3
    "dell_750w_psu",           # ✅ Dell БП
    # НЕТ процессоров Socket 604
    # НЕТ памяти DDR2
    # НЕТ HP/IBM блоков питания
]
```

## Код проверки совместимости

```python
def get_available_components(self, component_type: ComponentType) -> List[Component]:
    """
    Возвращает только те компоненты, которые совместимы 
    с текущей конфигурацией
    """
    # Получить все компоненты данного типа
    all_components = self.data.get_components_by_type(component_type)
    available = []
    
    # Проверить каждый компонент
    for component in all_components:
        # Проверить совместимость с текущей конфигурацией
        errors = self._check_compatibility(component)
        
        # Если ошибок нет - компонент совместим
        if not errors:
            available.append(component)
    
    return available
```

## Пример использования в веб-интерфейсе

### Backend API (Flask/FastAPI)

```python
@app.get("/api/components/{component_type}")
def get_components(component_type: str):
    """
    Возвращает доступные компоненты с учетом текущей конфигурации
    """
    # Получить текущую конфигурацию пользователя
    configurator = get_user_configurator(session_id)
    
    # Получить только совместимые компоненты
    available = configurator.get_available_components(
        ComponentType[component_type.upper()]
    )
    
    # Вернуть в формате JSON
    return {
        "available": [
            {
                "id": comp.id,
                "name": comp.name,
                "price": comp.price,
                "attributes": [
                    {"name": attr.name, "value": attr.value, "unit": attr.unit}
                    for attr in comp.attributes
                ]
            }
            for comp in available
        ]
    }
```

### Frontend (JavaScript)

```javascript
// Когда пользователь выбирает сервер
async function onServerSelected(serverId) {
    // Добавить сервер в конфигурацию
    await fetch('/api/configuration', {
        method: 'POST',
        body: JSON.stringify({ component_id: serverId })
    });
    
    // Обновить списки доступных компонентов
    await updateAvailableProcessors();
    await updateAvailableMemory();
    await updateAvailableStorage();
    await updateAvailablePSU();
}

// Получить доступные процессоры
async function updateAvailableProcessors() {
    const response = await fetch('/api/components/processor');
    const data = await response.json();
    
    // Показать только доступные процессоры
    renderComponents('processors-list', data.available);
    
    // Скрыть или затемнить недоступные
    disableIncompatibleComponents('processors', data.available);
}
```

### HTML с динамической фильтрацией

```html
<!-- ДО выбора сервера: показать все -->
<div class="component-card" data-id="intel_xeon_3_0_604">
    Intel Xeon 3.0 ГГц (Socket 604)
</div>
<div class="component-card" data-id="intel_xeon_e5620">
    Intel Xeon E5620 (Socket 1366)
</div>

<!-- ПОСЛЕ выбора HP сервера: затемнить несовместимые -->
<div class="component-card" data-id="intel_xeon_3_0_604">
    Intel Xeon 3.0 ГГц (Socket 604) <!-- Активен -->
</div>
<div class="component-card disabled" data-id="intel_xeon_e5620">
    Intel Xeon E5620 (Socket 1366) <!-- Затемнен -->
    <span class="incompatible-badge">Несовместим</span>
</div>
```

## Варианты отображения несовместимых компонентов

### Вариант 1: Полностью скрыть
```javascript
// Показать только совместимые
availableComponents.forEach(comp => {
    document.getElementById(comp.id).style.display = 'block';
});

// Скрыть несовместимые
incompatibleComponents.forEach(comp => {
    document.getElementById(comp.id).style.display = 'none';
});
```

**Плюсы:** Чистый интерфейс, не отвлекает  
**Минусы:** Пользователь не видит, что еще существует

### Вариант 2: Затемнить и заблокировать
```javascript
// Затемнить несовместимые
incompatibleComponents.forEach(comp => {
    const card = document.getElementById(comp.id);
    card.classList.add('disabled');
    card.title = 'Несовместимо с выбранным сервером';
});
```

**Плюсы:** Пользователь видит все опции  
**Минусы:** Может быть путаница

### Вариант 3: Показать с объяснением
```javascript
// Добавить бейдж с причиной
incompatibleComponents.forEach(comp => {
    const card = document.getElementById(comp.id);
    card.classList.add('incompatible');
    
    const badge = document.createElement('div');
    badge.className = 'incompatible-badge';
    badge.textContent = `Требуется Socket 1366 (у вас Socket 604)`;
    card.appendChild(badge);
});
```

**Плюсы:** Образовательный, помогает понять  
**Минусы:** Занимает место

## Рекомендуемый подход

**Комбинированный:**

1. **Первый экран (выбор сервера)** - показать все серверы
2. **После выбора сервера** - показать только совместимые компоненты
3. **Кнопка "Показать все"** - опционально показать несовместимые с объяснением
4. **Всплывающая подсказка** - при наведении на несовместимый компонент

```html
<div class="filters">
    <label>
        <input type="checkbox" id="show-incompatible">
        Показать несовместимые компоненты
    </label>
</div>

<div class="component-card" data-id="intel_xeon_e5620" data-compatible="false" style="display: none;">
    <span class="incompatible-icon">🚫</span>
    <div class="component-name">Intel Xeon E5620</div>
    <div class="incompatible-reason">
        Требуется Socket 1366 (ваш сервер: Socket 604)
    </div>
</div>
```

## Производительность

**Матрица совместимости обеспечивает быструю проверку:**

```python
# Проверка совместимости - O(1)
if new_component.id in compatibility_matrix[existing_component.id]:
    return True  # Совместим

# Вместо сложной логики - O(n)
if (check_socket(new, existing) and 
    check_memory_type(new, existing) and
    check_manufacturer(new, existing) and
    check_power(new, existing) and ...):
    return True
```

## Итого

✅ **При выборе сервера показываются ТОЛЬКО совместимые компоненты**  
✅ **Фильтрация происходит автоматически через `get_available_components()`**  
✅ **Матрица совместимости обеспечивает быструю проверку**  
✅ **Можно выбрать способ отображения несовместимых компонентов**  
✅ **Backend API возвращает уже отфильтрованный список**
