# API расписания Финансового университета при Правительстве Российской Федерации
Простая библиотека для получения расписания с ruz.fa.ru. Также может быть использована для работы с ruz.hse.ru

[![PyPi](https://img.shields.io/badge/PyPi-v1.0-orange)](https://pypi.org/project/fa-api/)
[![Лицензия GPLv3](https://img.shields.io/badge/license-GPLv3-lightgrey.svg)](https://www.gnu.org/licenses/gpl-3.0.html)


## Установка
```
pip3 install fa_api
```

## Примеры 
### Пример работы с группами

```python
from fa_api import FaAPI

#Создаем объект расписания
fa = FaAPI()

#Ищем группу ПИ19-5
group = fa.search_group("ПИ19-5")
#Получаем инфо о расписании группы ПИ19-5 на сегодня
timetable = fa.timetable_group(group[0]["id"])

#Ищем группу ПИ19-3
group = fa.search_group("ПИ19-3")
#Получаем инфо о расписании группы ПИ19-3 с 01.10.2020 по 06.10.2020
timetable = fa.timetable_group(group[0]["id"], "2020.10.01", "2020.10.06")

#Выводим list с расписанием
print(timetable)
```
### Пример работы с преподавателями

```python
from fa_api import FaAPI

#Создаем объект расписания
fa = FaAPI()

#Получаем информацию о преподавателе
teacher = fa.search_teacher("Милованов")
#Получаем расписание преподавателя за сентябрь
timetable = fa.timetable_teacher(teacher[0]["id"],"2020.09.01","2020.09.30")

#Выводим list с расписанием
print(timetable)
```