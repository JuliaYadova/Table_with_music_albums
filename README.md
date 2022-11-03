# Table_with_music_albums
### ТЗ по выполнению тестового задания.


Приложение содержит три модели:

(a) Album с полем name, содержащим название альбома в виде строки, artist, указывающий на модель Artist, year - год выпуска альбома в виде целого числа.
Также модель должна иметь строковое представление в виде - name[year];

(b) Artist с полем name, содержащим имя автора в виде строки;

(c) Track с полем name в виде строки, и с полем album указывающим на модель
Album.
На главной странице отображается таблица с заголовками album, name,
artist@name, tracks и строкой под заголовками, с кнопками сортировки по
album_name, artist@name.
album | name [sort]| artist@name [sort]| tracks
------|----------|-----------------|--------
album1[2022] | album1 | artist_name1 | track1 track2 track3
album2[2021] | album2 | artist_name2 | track1 track2 track3

При загрузке страницы должны подгружаться данные из API, в виде списка словарей и
загружаться в таблицу.
```
[{
"album": "album1[2022]",
"name":"album1",
"artist@name":"artist_name1",
"tracks":["track1","track2","track3"]
}, ...]
```
Причём:
1. в колонке album содержится строковое представление объекта модели Album;
2. в колонке name содержится поле name объекта модели Album;
3. в колонке artist@name содержится поле name объекта модели Artist, связанной с данным объектом модели Album;
4. в колонке tracks содержатся поля name, всех объектов модели Track связанных
с данным объектом модели Album.
При нажатии на кнопку Sort происходит сортировка по данной колонке: на API отправляется запрос с параметром sorting равному названию колонки и производится сортировка по sorting, при этом должна быть осуществлена логика, по которой вложенные
поля разделяются знаком @. Отсортированные данные передаются по API и загружаются в таблицу.


---
### Cтек:

<div>
  <img src="https://github.com/devicons/devicon/blob/master/icons/python/python-original-wordmark.svg" title="Python 3" alt="Python" width="40" height="40"/>&nbsp;
  <img src="https://github.com/devicons/devicon/blob/master/icons/django/django-plain-wordmark.svg" title="Django" alt="Django" width="40" height="40"/>&nbsp;
  <img src="https://github.com/devicons/devicon/blob/master/icons/sqlite/sqlite-original-wordmark.svg" title="SQLite3" alt="SQLite3" width="40"   height="40"/>&nbsp;
</div>

---
Инструкция по запуску:
1. Скопировать репозиторий;
2. В папке проекта создать виртуальное окружение и запустить его (*Здесь и далее команды под ОС Windows*):
```
python -m venv venv
source venv/Scripts/activate
python -m pip install --upgrade pip
python -m pip install -r requirements.txt
```
4. Из папки с файлом manage.py запустить сервер:
```
python manage.py makemigrations
python manage.py migrate
python manage.py runserver
```
5. Загрузить данные для теста:
```
python manage.py from_csv

```
6. Проект готов к тестированию:
```
/index # Главная страница проекта
/?sorting=name
/?sorting=artist@name # Обрабатываемые запросы на сортировку

```

---
### Автор
Юлия Я.
