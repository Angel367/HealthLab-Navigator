
### dump data from the file
```bash
python -Xutf8 manage.py dumpdata -o db.json
```
### load data from the file
```bash
python manage.py loaddata current_good_db.json
```
### run server
```bash
python manage.py makemigrations HealthLab_Navigator_api 
python manage.py migrate 
python manage.py runserver localhost:8000 
#python HealthLab_Navigator_api/test_data.py
```


