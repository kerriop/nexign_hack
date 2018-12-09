import osmapi
import csv


class Osm_reader():
    def __init__(self, min_lon, min_lat, max_lon, max_lat):
        self.__api = osmapi.OsmApi()
        self.__tmp = self.__api.Map(min_lon, min_lat, max_lon, max_lat)
        self.__ret = []

        for e in self.__tmp:
            try:
                try:
                    try:
                        type_ = e['type']
                        timestamp = e['data']['timestamp']
                        id = e['data']['id']
                        lat = e['data']['lat']
                        lon = e['data']['lon']
                        uid = e['data']['uid']
                        user = str(e['data']['user'])
                        tag = e['data']['tag']
                        delta_days = (osmapi.datetime.today() - timestamp).days

                        if type_ == 'node':
                            self.__ret.append([id, lat, lon, uid, timestamp, user])
                            print(e)
                            # print('type:', type_)
                            # print('timestamp:', timestamp)
                            # print(self.__ret[-1])
                            # print('------------------------------------')
                    except KeyError:
                        pass
                except IndexError:
                    pass
            except UnicodeEncodeError as err:
                print(err, str(e) + '\n')

    # def __str__(self):
    #     for e in self.__ret:
    #         print(e)

    def create_file(self):
        with open('dump.csv', "w", newline='', encoding='utf-8') as csv_file:
            writer = csv.writer(csv_file, delimiter=',')
            # writer.writerow(['id', 'lat', 'lon', 'uid', 'timestamp'])
            for line in self.__ret:
                writer.writerow(line)

    def get_values(self):
        return self.__ret


if __name__ == '__main__':
    a = Osm_reader(30.3060, 59.9352, 30.3308, 59.9440)
    result = a.get_values()
    a.create_file()
    # for e in result:
    #     print(str(e))