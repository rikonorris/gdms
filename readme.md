
Governance Government Automatization Platform


- Django 1.11
- MariaDB 1.12

ViewFlow - http://docs.viewflow.io/  
ToDo - https://github.com/shacker/django-todo  
Form Buider - https://github.com/stephenmcd/django-forms-builder  
Report Builder - https://github.com/burke-software/django-report-builder
Groups Manager - http://django-groups-manager.readthedocs.io/

Інсталяція:
1. Зтягнути останні коміти git pull
2. Внести зміни в settings_local.py в частині БД
3. Зробити міграції - ./manage.py makemigrations
4. Закоментувати в settings.py та url.py додаток todo
5. Промігрувати схему - ./manage.py migrate
6. Розкоментувати todo
7. Змігрувати знову
8. Додати суперюзера ./manage.py createsuperuser
9. Зайти в адмінку /area51
10. Додати ПІБ юзеру через блок "Штатний розпис" -> Користувачі
11. В тому ж блоці створити декілька департаментів і штатних одиниць. Додати у департамент юзерів
12. Створити Групи авторизації, дати права і додати до них юзерів
13. Done!