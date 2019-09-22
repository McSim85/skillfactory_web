"""
требования к приложению:
1. Веб-сервер принимает GET-запросы по адресу /albums/<artist> и выводит на экран сообщение с количеством альбомов
    исполнителя artist и списком названий этих альбомов.
2. Веб-сервер принимает POST-запросы по адресу /albums/ и сохраняет переданные пользователем данные об альбоме.
    Данные передаются в формате веб-формы. Если пользователь пытается передать данные об альбоме, который уже есть в
    базе данных, обработчик запроса отвечает HTTP-ошибкой 409 и выводит соответствующее сообщение.
Чтобы сформировать POST-запрос к серверу можно воспользоваться уже знакомой нам утилитой http.
    Допустим, мы запустили сервер по адресу http://localhost:8080. Тогда запросы будут выглядеть так:
    http -f POST http://localhost:8080/albums artist="New Artist" genre="Rock" album="Super"
    Дополните список передаваемых параметров, если потребуется.
3. Набор полей в передаваемых данных полностью соответствует схеме таблицы album базы данных.
4. В качестве исходной базы данных использовать файл albums.sqlite3.
5. До попытки сохранить переданные пользователем данные, нужно провалидировать их. Проверить, например, что в поле "год выпуска" передан действительно год.

Выложите код в репозиторий и приложите ссылку. Если считаете нужным, оставьте комментарии о способах запуска и
    проверки кода. Если в модулях есть сложные на ваш взгляд места, прокомментируйте их.
"""
from bottle import route
from bottle import run
from bottle import HTTPError
from bottle import HTTPResponse
from bottle import request

import album

def make_russian(num):
    """
    Определение окончания "\а\ов" в зависимости от кол-ва найденых альбомов
    """
    strRez = ""
    if (str(num)[-1] in "567890") or (11 <= num <= 14):
        strRez += "ов"
    elif str(num)[-1] in "234":
        strRez += "а"
    return strRez

@route("/albums/<artist>")
def albums(artist):
    albums_list = album.find(artist)
    if not albums_list:
        message = "Альбомов {} не найдено".format(artist)
        result = HTTPError(404, message)
    else:
        album_names = [album.album for album in albums_list]
        result = "База данных содержит {} альбом{} {}:<br>".format(len(albums_list), make_russian(len(albums_list)), artist)
        result += "<br>".join(album_names)
    return result

def valid_album(album_data):
    message = ""
    result = HTTPResponse(status=200, body=message)
    EmptyFields = list(filter(lambda x: album_data[x] == "" or album_data[x] is None , album_data.keys()))
    if EmptyFields :
        message += "Необходимо заполнить поля: %s <br>" % " ".join(EmptyFields)
        result = HTTPError(400, message)
    try:
        album_data["year"] = int(album_data["year"])
    except ValueError :
        message += "Год выпуска альбома не число, данные - не сохранены "
        result = HTTPError(400, message)
    return (result, album_data)

@route("/albums", method="POST")
def album_insert():
    album_data = {
        "year": request.forms.get("year"),
        "artist": request.forms.get("artist"),
        "genre": request.forms.get("genre"),
        "album": request.forms.get("album")
    }
    result, album_data = valid_album(album_data)
    if not isinstance(result, HTTPError):
        result = album.insert(album_data)
    return result

if __name__ == '__main__':
    run(host="localhost", port=8080, debug=True)