from bottle import route, run, HTTPError, request
import album
import json


def save_user(user_data):
    first_name = user_data['first_name']
    last_name = user_data['last_name']
    filepath = f'{first_name}-{last_name}.json'
    with open(filepath, 'w') as fp:
        json.dump(user_data, fp)
    return filepath


@route('/albums', method="POST")
def add_album():
    """Добавляет альбом в БД"""
    artist = request.forms.get('artist')
    year = request.forms.get('year')
    album_name = request.forms.get('album')
    genre = request.forms.get('genre')
    try:
        year = int(year)
    except ValueError:
        return HTTPError(400, 'Ошибка, введите год в формате ХХХХ')

    try:
        new_album = album.add_album(
            year=year,
            artist=artist,
            album=album_name,
            genre=genre
        )
    except AssertionError as err:
        return HTTPError(400, str(err))

    except album.AlreadyExists as err:
        return HTTPError(409, str(err))

    else:
        print('Новый альбом {} добавлен в медитеку'.format(new_album.id))
    return "Новый id = {}".format(new_album.id)


@route('/user', method='POST')
def user():
    """Сохранение данных полученных из формы"""
    user_data = {
        'first_name': request.forms.get('first_name'),
        'last_name': request.forms.get('last_name'),
        'birthday': request.forms.get('birthday')
    }
    saved_to = save_user(user_data)
    print(f'Пользоватеть сохранен в файл {saved_to}')
    return "Данные успешно сохранены"


@route('/albums/<artist>/')
def get_albums_by_artist(artist):
    """ Поиск альбомов по артисту """
    albums_list = album.find(artist)
    print(albums_list)
    if albums_list is not None:
        albums_names = [album.album for album in albums_list]

        result = f"Список альбомов артиста {artist}</br>"
        result += 'Количество: {}</br>'.format(len(albums_list))
        result += '</br>'.join(albums_names)
        return result
    else:
        message = f'Альбомов артиста {artist} в базе не найден'
        return HTTPError(400, message)


def fib(n):
    a, b = 1, 1
    for x in range(n):
        a, b = b, a + b
    return a


@route('/hello/')
def hello_world():
    return 'Hello World'


@route('/hello/<param>/')
def upper(param):
    return param.upper()


@route('/fib/<n:int>/')
def get_fib(n):
    result = fib(n)
    return str(result)


@route('/modify/<param>/<method>/')
def modify(param, method):
    if method == 'upper':
        return param.upper()
    elif method == 'lower':
        return param.lower()
    elif method == 'title':
        return param.title()
    else:
        raise HTTPError(400, 'Invalid "method" value ')


@route('/add')
def add():
    try:
        x = int(request.query.x)
        y = int(request.query.y)
    except ValueError:
        return HTTPError(400, 'Некоректные параметры')
    else:
        return "Сумма {} и {} равна {}".format(x, y, x + y)


if __name__ == '__main__':
    run(host="localhost", port=8000, debug=True)
