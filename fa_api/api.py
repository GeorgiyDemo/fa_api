from datetime import date
from datetime import datetime
from typing import List

import requests
import urllib3

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)


class FaAPI:
    HOST = "https://ruz.fa.ru"

    def __date_now(self) -> str:
        return datetime.now().strftime("%Y.%m.%d")

    def __request(self, sub_url: str):
        """Запрос к РУЗ"""

        r = requests.get(self.HOST + sub_url, verify=False)
        if r.status_code == 200:
            return r.json()
        raise requests.exceptions.BaseHTTPError(
            "[Ошибка] RUZ отдал код {}!\nURL: '{}'".format(
                r.status_code, self.base_url + sub_url
            )
        )

    def search_group(self, group_name: str) -> List:
        """Поиск группы по ее названию"""

        r = self.__request("/api/search?term={}&type=group".format(group_name))
        return r

    def timetable_group(
        self, group_id: str, date_begin: date = None, date_end: date = None
    ) -> List:
        """Отдает расписание группы по её id"""

        if date_begin is None or date_end is None:
            date_begin = self.__date_now()
            date_end = date_begin

        r = self.__request(
            "/api/schedule/group/{}?start={}&finish={}&lng=1".format(
                group_id, date_begin, date_end
            )
        )
        return r

    def search_teacher(self, teacher_name: str) -> List:
        """Поиск преподавателя по его ФИО"""

        r = self.__request("/api/search?term={}&type=person".format(teacher_name))
        return r

    def timetable_teacher(
        self, teacher_id: str, date_begin: date = None, date_end: date = None
    ) -> List:
        """Отдает расписание преподавателя по его id"""

        if date_begin is None or date_end is None:
            date_begin = self.__date_now()
            date_end = date_begin

        r = self.__request(
            "/api/schedule/person/{}?start={}&finish={}&lng=1".format(
                teacher_id, date_begin, date_end
            )
        )
        return r

    def search_auditorium(self, auditorium_name: str) -> List:
        """Поиск аудитории по её названию"""

        r = self.__request(
            "/api/search?term={}&type=auditorium".format(auditorium_name)
        )
        return r

    def timetable_auditorium(
        self, auditorium_id: str, date_begin: date = None, date_end: date = None
    ) -> List:
        """Отдает расписание преподавателя по его id"""

        if date_begin is None or date_end is None:
            date_begin = self.__date_now()
            date_end = date_begin

        r = self.__request(
            "/api/schedule/auditorium/{}?start={}&finish={}&lng=1".format(
                auditorium_id, date_begin, date_end
            )
        )
        return r

    def search_building(self, building_name: str) -> List:
        """Поиск здания по его названию"""

        r = self.__request("/api/search?term={}&type=building".format(building_name))
        return r

    def timetable_building(
        self, building_id: str, date_begin: date = None, date_end: date = None
    ) -> List:
        """Отдает расписание здания по его id"""

        if date_begin is None or date_end is None:
            date_begin = self.__date_now()
            date_end = date_begin

        r = self.__request(
            "/api/schedule/building/{}?start={}&finish={}&lng=1".format(
                building_id, date_begin, date_end
            )
        )
        return r
