from datetime import datetime
from typing import List, Dict
from datetime import date

import requests
from fake_headers import Headers


class MetaHeaders(type):
    def __init__(cls, name, bases, dct):
        cls.headers = header_generator()

    def header_generator(self):
        """Генерация header'ов"""
        
        header = Headers()
        headers = header.generate()
        headers["Accept-Language"] = "ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7"
        headers["Accept"] = "application/json, text/plain, */*"
        headers["Accept-Encoding"] = "gzip, deflate, br"
        headers["Referer"] = "https://ruz.fa.ru/ruz/main"
        headers["Sec-Fetch-Site"] = "same-origin"
        headers["Sec-Fetch-Mode"] = "cors"
        headers["Sec-Fetch-Dest"] = "empty"
        return headers


class FaAPI(metaclass=MetaHeaders):

    HOST = "https://ruz.fa.ru"

    def __init__(self):
        self.header_generator()

    def __date_now(self) -> str:
        return datetime.now().strftime("%Y.%m.%d")

    def __request(self, path: str, data: Dict[str, str]):
        """Запрос к РУЗ"""

        r = requests.get(self.HOST + path, headers=self.headers, data=data)
        if r.status_code == 200:
            return r.json()
        raise requests.exceptions.BaseHTTPError(
            "[Ошибка] RUZ отдал код {}!\nURL: '{}'".format(r.status_code, self.HOST + path))

    def search_group(self, group_name: str) -> List:
        """Поиск группы по ее названию"""

        r = self.__request(
            "/api/search",
            data={
                'term': group_name,
                'type': 'group'
            })
        return r

    def timetable_group(self, group_id: str, date_begin: date = None, date_end: date = None) -> List:
        """Отдает расписание группы по её id"""

        if date_begin is None or date_end is None:
            date_begin = self.__date_now()
            date_end = date_begin

        r = self.__request(
            f"/api/schedule/group/{group_id}",
            data={
                'start': date_begin,
                'finish': date_end,
                'lng': 1
            })
        return r

    def search_teacher(self, teacher_name: str) -> List:
        """Поиск преподавателя по его ФИО"""

        r = self.__request(
            "/api/search",
            data={
                'term': teacher_name,
                'type': 'person'
            })
        return r

    def timetable_teacher(self, teacher_id: str, date_begin: date = None, date_end: date = None) -> List:
        """Отдает расписание преподавателя по его id"""

        if date_begin is None or date_end is None:
            date_begin = self.__date_now()
            date_end = date_begin

        r = self.__request(
            f"/api/schedule/person/{teacher_id}",
            data={
                'start': date_begin,
                'finish': date_end,
                'lng': 1
            })
        return r

    def search_auditorium(self, auditorium_name: str) -> List:
        """Поиск аудитории по её названию"""

        r = self.__request(
            "/api/search",
            data={
                'term': auditorium_name,
                'type': 'auditorium'
            })
        return r

    def timetable_auditorium(self, auditorium_id: str, date_begin: date = None, date_end: date = None) -> List:
        """Отдает расписание преподавателя по его id"""

        if date_begin is None or date_end is None:
            date_begin = self.__date_now()
            date_end = date_begin

        r = self.__request(
            f"/api/schedule/auditorium/{auditorium_id}",
            data={
                'start': date_begin,
                'finish': date_end,
                'lng': 1
            })
        return r

    def search_building(self, building_name: str) -> List:
        """Поиск здания по его названию"""

        r = self.__request(
            "/api/search",
            data={
                'term': building_name,
                'type': 'building'
            })
        return r

    def timetable_building(self, building_id: str, date_begin: date = None, date_end: date = None) -> List:
        """Отдает расписание здания по его id"""

        if date_begin is None or date_end is None:
            date_begin = self.__date_now()
            date_end = date_begin

        r = self.__request(
            f"/api/schedule/building/{building_id}",
            data={
                'start': date_begin,
                'finish': date_end,
                'lng': 1
            })
        return r
