# HealthLab-Navigator
Репозиторий с кодом BackEnd и FrontEnd частей агрегатора медицинских лабораторий.

## Структура проекта

+74958008080:12345678 Гемотест
+74958008081:12345678 КДЛ
+74958008082:12345678 Обычный


#### Экспорт БД
```shell
python -Xutf8 manage.py dumpdata --indent=4 --exclude auth.permission --exclude contenttypes -o current_good_db.json
```
#### Импорт БД
```shell
python -Xutf8 manage.py loaddata current_good_db.json
```