from datetime import datetime

import requests
from fake_headers import Headers


class FaAPI:
    def __init__(self):

        self.base_url = "https://ruz.fa.ru"
        self.header_generator()

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
        self.headers = headers

    def __date_now(self):
        return datetime.now().strftime("%Y.%m.%d")

    def __request(self, sub_url):
        """Запрос к РУЗ"""
        r = requests.get(self.base_url + sub_url, headers=self.headers)
        if r.status_code == 200:
            return r.json()
        raise requests.exceptions.BaseHTTPError(
            "[Ошибка] RUZ отдал код {}!\nURL: '{}'".format(r.status_code, self.base_url + sub_url))

    def search_group(self, group_name: str) -> list:
        """Поиск группы по ее названию"""
        r = self.__request("/api/search?term={}&type=group".format(group_name))
        return r

    def timetable_group(self, group_id: str, date_begin=None, date_end=None) -> list:
        """Отдает расписание группы по её id"""

        if date_begin is None or date_end is None:
            date_begin = self.__date_now()
            date_end = date_begin

        r = self.__request("/api/schedule/group/{}?start={}&finish={}&lng=1".format(group_id, date_begin, date_end))
        return r

    def search_teacher(self, teacher_name: str) -> list:
        """Поиск преподавателя по его ФИО"""
        r = self.__request("/api/search?term={}&type=person".format(teacher_name))
        return r

    def timetable_teacher(self, teacher_id: str, date_begin=None, date_end=None) -> list:
        """Отдает расписание преподавателя по его id"""

        if date_begin is None or date_end is None:
            date_begin = self.__date_now()
            date_end = date_begin

        r = self.__request("/api/schedule/person/{}?start={}&finish={}&lng=1".format(teacher_id, date_begin, date_end))
        return r

    def search_auditorium(self, auditorium_name: str) -> list:
        """Поиск аудитории по её названию"""
        r = self.__request("/api/search?term={}&type=auditorium".format(auditorium_name))
        return r

    def timetable_auditorium(self, auditorium_id: str, date_begin=None, date_end=None) -> list:
        """Отдает расписание преподавателя по его id"""

        if date_begin is None or date_end is None:
            date_begin = self.__date_now()
            date_end = date_begin

        r = self.__request(
            "/api/schedule/auditorium/{}?start={}&finish={}&lng=1".format(auditorium_id, date_begin, date_end))
        return r

    def search_building(self, building_name: str) -> list:
        """Поиск здания по его названию"""
        r = self.__request("/api/search?term={}&type=building".format(building_name))
        return r

    def timetable_building(self, building_id: str, date_begin=None, date_end=None) -> list:
        """Отдает расписание здания по его id"""

        if date_begin is None or date_end is None:
            date_begin = self.__date_now()
            date_end = date_begin

        r = self.__request(
            "/api/schedule/building/{}?start={}&finish={}&lng=1".format(building_id, date_begin, date_end))
        return r
