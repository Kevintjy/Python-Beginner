class App_list:
    def __init__(self):
        self.app = {}

    def add_app(self, name, genre):
        self.app[name] = genre


    def get_apps_by_genre(self, gerne):
        genre_list = []
        for i in self.app:
            if self.app[i] == gerne:
                genre_list.append(i)
        genre_list.sort()
        return genre_list

    def get_app_in_alphabetical_order(self):
        a = [self.app.keys()]
        return sorted(a)

    def __str__(self):
        result = {}
        for i in self.app:
            genre = self.app[i]
            if genre not in result:
                result[genre] = [i]
            else:
                result[genre].append(i)
        apps = []
        for keys in result:
            game = ','.join(result[keys])
            apps.append('{}:{}'.format(keys, game))
        return '\n'.join(apps)


if __name__ == "__main__":
    a = App_list()
    a.add_app('word', 'Work')
    a.add_app("ppt","Work")
    a.add_app("excel", "Work")
    a.add_app("fall in love", 'Romantic')
    print(a)