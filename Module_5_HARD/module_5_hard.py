import hashlib
import time as T
class UrTube:
    users = {}
    videos = {}
    current_user = None

    def log_in(self, nickname, password):
        password = str(password)
        password = hashlib.sha256(password.encode()).hexdigest()
        if self.users[nickname].password == password and nickname in self.users.keys():
            self.current_user = self.users[nickname]
            return self.current_user.nickname, print(f'Пользователь {self.current_user} вошёл в учётную запись.')
        elif self.users[nickname].password != password and nickname in self.users.keys():
            print(f'Не верный пароль для пользователя {nickname}')
        else:
            print(f'Пользователя {nickname} не существует')

    def register(self, nickname, password, age):
        if nickname in self.users.keys():
            print(f'Пользователь с никнеймом {nickname} уже существует')
        else:
            user = User(nickname, password, age)
            self.users[nickname] = user
            self.current_user = user.nickname
            print(f'Пользователь {self.current_user} зарегестрирован и находится на сайте.')

    def log_out(self):
        self.current_user = None

    def add(self, *args):
        for v in args:
            if v.title not in self.videos.keys():
                self.videos[v.title] = v
            elif v.title in self.videos.keys():
                continue

    def get_videos(self, key_word):
        key_word = key_word.lower()
        find_list = []
        for v in self.videos.keys():
            if key_word in v.lower():
                find_list.append(v)
        return find_list

    def watch_video(self, title):
        if self.current_user == None:
            return print('Войдите в аккаунт, чтобы смотреть видео')
        if title not in self.videos.keys():
            return print(f'Видео под названием {title} не существует')
        v_duration = self.videos[title].duration
        time_now = self.videos[title].time_now
        if self.videos[title].adult_mode:
            if self.users[self.current_user].age >= 18:
                time = 0
                print(time, end= ' ')
                for time in range(time_now, v_duration):
                    time += 1
                    self.videos[title].time_now = time
                    T.sleep(1)
                    print(time, end= ' ')
                print('Конец видео')
            else:
                print('Вам нет 18 лет, пожалуйста покиньте страницу.')
        else:
            time = 0
            print(time, end=' ')
            for time in range(time_now, v_duration):
                time += 1
                self.videos[title].time_now = time
                T.sleep(1)
                print(time, end=' ')
            print('Конец видео')


class Video:
    def __init__(self, title, duration, time_now=0, adult_mode=False):
        self.title = title
        if duration > 0:
            self.duration = duration
        else:
            print('Нельзя загрузить картинку на ВИДЕОхостинг!')
        self.time_now = time_now
        self.adult_mode = adult_mode


class User:
    def __init__(self, nickname, password, age):
        self.nickname = nickname
        password = str(password)
        self.password = hashlib.sha256(password.encode()).hexdigest()
        self.age = age



ur = UrTube()
v1 = Video('Лучший язык программирования 2024 года', 200)
v2 = Video('Для чего девушкам парень программист?', 10, adult_mode=True)

# Добавление видео
ur.add(v1, v2)

# Проверка поиска
print(ur.get_videos('лучший'))
print(ur.get_videos('ПРОГ'))

# Проверка на вход пользователя и возрастное ограничение
ur.watch_video('Для чего девушкам парень программист?')
ur.register('vasya_pupkin', 'lolkekcheburek', 13)
ur.watch_video('Для чего девушкам парень программист?')
ur.register('urban_pythonist', 'iScX4vIJClb9YQavjAgF', 25)
ur.watch_video('Для чего девушкам парень программист?')

# Проверка входа в другой аккаунт
ur.register('vasya_pupkin', 'F8098FM8fjm9jmi', 55)
print(ur.current_user)

# Попытка воспроизведения несуществующего видео
ur.watch_video('Лучший язык программирования 2024 года!')
