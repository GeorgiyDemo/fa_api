import requests

class FaAPI:
    """Base constructor"""
    def __init__(self):
        self.base_url = "https://ruz.fa.ru"
        pass

    def request(self, sub_url):
        #TODO выставить header'ы
        r = requests.get(self.base_url+sub_url)
        if r.status_code == 200:
            return r.json()
        raise requests.exceptions.BaseHTTPError("RUZ отдал код {}! ".format(r.status_code))


    def search_group(self, group_name):
        """
        Поиск по группе
        - Принимает имя группы
        - Отдает json с id группы и всем таким
        """
        r = self.request("/api/search?term={}&type=group".format(group_name))
        return r

    def group_timetable(self, group_id):
        """"
        Отдает расписание по группе
        Принимает:
        - id гурппы 
        - Дату начала
        - Дату окончания




if __name__ == "__main__":
    obj = FaAPI()
    print(obj.search_group("ПИ19-4"))

