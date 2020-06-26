# Написать класс итератора, который по каждой стране из файла countries.json ищет страницу из википедии.
# Записывает в файл пару: страна – ссылка. Ссылку формировать самостоятельно.


import wikipedia
import json

wiki_link = 'https://en.wikipedia.org/wiki/'


def get_list_from_json(given_file):
    with open(given_file, 'r', encoding='utf8') as opened_file:
        data = json.load(opened_file)
        countries_list = []
        for country in data:
            countries_list.append(country['name']['common'])
    return countries_list


get_list_from_json('countries.json')

class WikiIter:
    def __init__(self, list, file_to_write):
        self.count = 0
        self.limit = len(list)
        self.countries_list = list
        self.file_to_write = file_to_write

    def __iter__(self):
        return self

    def __next__(self):
        if self.count >= self.limit:
            raise StopIteration
        index = self.count
        self.count += 1
        with open(self.file_to_write, 'w', encoding='utf8') as file:
                file.write(f"{self.countries_list[index]}," \
                      f"has link on wiki as=> {wiki_link + self.countries_list[index]}")
        return self.countries_list[index]


lets_iter = WikiIter(get_list_from_json('countries.json'), 'result.txt')

for line in lets_iter:
    print(line)


























# class Wiki_iter:
#
#     def __init__(self, given_file, file_to_write):
#         self.count = 0
#         self.limit = len(self.given_file)
#         self.given_file = given_file
#         self.file_to_write = file_to_write
#
#     def __iter__(self):
#         return self
#
#     def __next__(self):
#         if self.count < self.limit:
#             iterated_dict = self.given_file[self.count]
#             country_name = iterated_dict['name']
#
#
# if __name__ == '__main__':
#     with open("countries.json", 'r', encoding="utf-8") as country:
#         given_file = json.load(country)
#     lets_iter = Wiki_iter(given_file, 'result.txt')
#
#

