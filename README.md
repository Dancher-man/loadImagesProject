
## Зависимости

Для запуска проекта установить python версии 3.7 и выше и pip

## Локальный запуск проекта

После клонирования проекта выполните команды:

### Работа  с докером

### Установите Docker, Docker-Compose

### Команда для созданья образа с нуля (понадобиться немного времени пока скачаются все образы)
```bash 
docker-compose up -d --build
```
### Затем создайте суперюзера с помощью команды
```bash
docker-compose run web python manage.py createsuperuser

```

### Команда для запуска проекта, вместо(python manage.py runserver)
```bash
docker-compose up
```
### После переходите ...

#### Просмотр всех фото 

```
http://localhost:8000/api/v1/images
```

#### Создание фото POST запросом в postman передача данных через form-data а то валидацию не пройдет на фото

```
http://localhost:8000/api/v1/images
```

#### Просмотр одного фото по id пример

```
http://localhost:8000/api/v1/images/1
```

### В админ панели добавлена возможность управления данными

### Фильтрация по дате пример
#### По дате и время только так фильтровать можно другую
```
http://localhost:8000/api/v1/images/filter?created_at=2023-01-19 04:39:40
```

### Фильтрация по геолокации пример

```
http://localhost:8000/api/v1/images/filter?geolocation=Bishkek
```

### Фильтрация по имени людей пример

```
http://localhost:8000/api/v1/images/filter?persons_names=Vasya
```

### Поиск по вхождению в имени отмеченных людей на фото пример

```
http://localhost:8000/api/v1/images/search?persons_names=Ko
```


