import hashlib
import time as T


class UrTube:
    users = {}
    videos = {}
    current_user = None

    def log_in(self, nickname, password):
        """
        Здесь производится логика входа в учётную запись, которая есть в списке юзеров.
        Входной параметр "password" хэшируется и сравнивается с хэшированным паролем из объекта,
        находящегося в словаре под ключём, который является никнеймом этого объекта.
        Если никнейм есть среди ключей словаря и пароль совпадает с паролем объекта под этим ключём,
        то производится вход в учётную запись и "current_user" принимает никнейм пользователя.
        :param nickname:
        :param password:
        :return:
        """
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
        """
        Description:
        Производится логика регистрации нового пользователя:
        Проверяется наличие пользователя в списке, если нет такого, то создаётся объект пользователя из класса
        "User" с хэшированным паролем. На каждом этапе выводится сообщение.
        :param nickname:
        :param password:
        :param age:
        :return:
        """
        if nickname in self.users.keys():
            print(f'Пользователь с никнеймом {nickname} уже существует')
        else:
            user = User(nickname, password, age)
            self.users[nickname] = user
            self.current_user = user.nickname
            print(f'Пользователь {self.current_user} зарегестрирован и находится на сайте.')

    def log_out(self):
        """
        Description:
        Выход из учётной записи
        (сбрасывание текущего пользователя)
        :return:
        """
        self.current_user = None

    def add(self, *args):
        """
        Description:
        Берётся кортеж из объедков и вносится по одному в словарь под ключём собственного параметра "title",
        то есть названия, но при условии, если в словаре нет объекта с таким ключём.
        :param args:
        :return:
        """
        for v in args:
            if v.title not in self.videos.keys():
                self.videos[v.title] = v
            elif v.title in self.videos.keys():
                continue

    def get_videos(self, key_word):
        """
        Description:
        На вход приходит строка, переводится в нижний регистр и проверяется есть ли эта строка среди ключей словаря,
        содержащего информацию о видеороликах (ключи перенимают название видеороликов в словаре). Эти ключи тоже
        переводятся в нижний регистр для исключения несовпадений из-за несовпадения по регистру.
        Все названия найденых видеороликов выводятся в виде списка.
        :param key_word:
        :return: find_list
        """
        key_word = key_word.lower()
        find_list = []
        for v in self.videos.keys():
            if key_word in v.lower():
                find_list.append(v)
        return find_list

    def watch_video(self, title):
        """
        Description:
        На вход поступает атрибут "title"
        ▼
        Проверяется условие: авторизован ли сейчас какой-либо пользователь на сайте
        Если НЕТ, то выводить сообщение о необходимости авторизации
        Если ДА, то:
        ▼
        Проверяется условие: Имеется ли видео в списке под названием "title"
        Если НЕТ, то выводить сообщение об отсутствии видео
        Если ДА, то:
        ▼
        Проверяется условие возрастного ограничения:
        ▼               ▼
        Если нет ▼      Если есть ограничение, то проверяется текущий пользователь на достижение необходимого возраста:
                 ▼      ▼
                 ▼      Если пользователь младше, то выводится сообщение о его малолетстве
                 ▼      Если проверка на возраст пройдена то:
                 ▼      ▼
                 Вовспроизводится цикл проигрывания видео с присвоением текущего времени к объекту видеоролика
                 в списке, для возможности посмотреть его потом с нужного момента (такой функции нет :-(   )
        :param title:
        :return:
        """
        if self.current_user == None:
            return print('Войдите в аккаунт, чтобы смотреть видео')
        if title not in self.videos.keys():
            return print(f'Видео под названием {title} не существует')
        v_duration = self.videos[title].duration
        time_now = self.videos[title].time_now
        if self.videos[title].adult_mode:
            if self.users[self.current_user].age >= 18:
                time = 0
                print(time, end=' ')
                for time in range(time_now, v_duration):
                    time += 1
                    self.videos[title].time_now = time
                    T.sleep(1)
                    print(time, end=' ')
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


# Здесь создаётся объект видеоролика и проверяется, что это ролик длительностью хотя бы в секунду, а не просто .jpeg
class Video:
    def __init__(self, title, duration, time_now=0, adult_mode=False):
        self.title = title
        if duration > 0:
            self.duration = duration
        else:
            print('Нельзя загрузить картинку на ВИДЕОхостинг!')
        self.time_now = time_now
        self.adult_mode = adult_mode


# Здесь создаётся объект пользователя и производится хэширование пароля при создании
class User:
    def __init__(self, nickname, password, age):
        self.nickname = nickname
        password = str(password)
        self.password = hashlib.sha256(password.encode()).hexdigest()
        self.age = age


ur = UrTube()
v1 = Video('Лучший язык программирования 2024 года', 200)
v2 = Video('Для чего девушкам парень программист?', 10, adult_mode=True)
print(UrTube().__doc__)
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
