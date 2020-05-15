Простая библиотека с API для получения расписания с ruz.fa.ru

## Установка с pip
```
pip3 install git+https://github.com/GeorgiyDemo/fa_api.git
```

## Примеры 
### Пример работы с группами

```python
from fa_api import FaAPI

#Создаем объект расписания
fa = FaAPI()

#Получаем информацию о группе ПИ19-5
group = fa.search_group("ПИ19-5")
#Получаем инфо о расписании группы ПИ19-5 на сегодня
timetable = fa.timetable_group(group[0]["id"])

#Получаем информацию о группе ПИ19-3
group = fa.search_group("ПИ19-3")
#Получаем инфо о расписании группы ПИ19-3 с 01.05.2020 по 06.05.2020
timetable = fa.timetable_group(group[0]["id"], "2020.05.01", "2020.05.06")

print(timetable)
```
### Пример работы с преподавателями

```python
from fa_api import FaAPI

#Создаем объект расписания
fa = FaAPI()
#Получаем информацию о преподавателе
teacher = fa.search_teacher("Милованов")
#Получаем расписание преподавателя за апрель
timetable = fa.timetable_teacher(teacher[0]["id"],"2020.04.01","2020.04.30")
print(timetable)
```