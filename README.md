# Blogicum

Этот проект представляет собой работу над веб-приложением **Блогикум**, в котором реализуется функционал публикаций с подключением базы данных. В рамках второго этапа проекта добавляется возможность управления публикациями с помощью базы данных, а также настройка отображения постов на страницах в зависимости от их состояния.

## Описание проекта

Приложение **Блогикум** — это блог-платформа, где пользователи могут создавать и публиковать свои записи (посты) с различными аттрибутами. В этой версии добавлена поддержка базы данных для хранения информации о постах, их категории, локации и авторе.

Для этого проекта можно указать следующий стек технологий:

### Стек технологий:

- **Backend**:
  - **Django** — основной фреймворк для создания веб-приложений на Python.
  - **SQLite** — база данных для хранения информации о публикациях, категориях, локациях и пользователях.
  - **Django ORM** — для работы с базой данных, включая создание моделей, миграции и запросы.

- **Frontend**:
  - **HTML** — для создания шаблонов страниц.
  - **CSS**, **Bootstrap** — для стилизации шаблонов.

- **Администрирование**:
  - **Django Admin** — встроенная панель администратора для управления контентом (публикациями, категориями, локациями).
    
- **Контроль версий**:
  - **Git** — система контроля версий.
  - **GitHub** — для хранения репозитория.

Этот стек позволяет организовать быстрое развертывание веб-приложения с использованием Python и Django.

### Основные особенности:
- **Публикация** — это основная единица блога, которая включает в себя заголовок, основной текст, дату публикации, статус публикации и связана с пользователем-автором.
- **Категории** — публикации можно классифицировать по категориям, каждая категория имеет название, описание и уникальный идентификатор (slug).
- **Локации** — публикации могут быть привязаны к конкретным географическим местоположениям.
- **Управление постами** — администраторы (суперпользователи) могут добавлять, редактировать и удалять публикации, а также управлять их состоянием.

## Структура проекта

Проект состоит из следующих основных частей:
- **Модели**:
  - `Post` — публикация, содержащая информацию о заголовке, тексте, дате публикации, авторе, категории и локации.
  - `Category` — категория публикации, которая помогает группировать посты по темам.
  - `Location` — географическое местоположение, с которым может быть связано пост.
- **Админ-панель** — настройка административного интерфейса для управления данными моделей.
- **Шаблоны** — HTML-шаблоны для отображения страниц, таких как главная страница, страницы категорий и страницы отдельных публикаций.
- **ORM-запросы** — использование Django ORM для получения данных из базы и отображения их на страницах.
  
## Основные фичи:

- **Главная страница**: вывод последних 5 публикаций, которые опубликованы и имеют актуальную дату.
- **Страница категории**: отображение публикаций по выбранной категории.
- **Страница публикации**: отображение конкретной публикации по ее идентификатору.
- **Админ-зона**: возможность создавать, редактировать и удалять посты, категории и локации через административный интерфейс Django.

## Модели

### Post (Публикация)

- **title** — заголовок поста (макс. 256 символов).
- **text** — основной текст поста.
- **pub_date** — дата публикации.
- **author** — автор поста, связанный с моделью `User`.
- **location** — локация, связаная с моделью `Location` (необязательное поле).
- **category** — категория, связанная с моделью `Category`.
- **is_published** — флаг опубликованности поста.
- **created_at** — дата добавления записи в базу.

### Category (Категория)

- **title** — название категории.
- **description** — описание категории.
- **slug** — уникальный идентификатор категории.
- **is_published** — флаг опубликованности категории.
- **created_at** — дата создания категории.

### Location (Локация)

- **name** — название локации.
- **is_published** — флаг опубликованности локации.
- **created_at** — дата создания локации.

## Скриншоты

### Страница "О нас":
![Страница "О нас"](screenshots/About.png)

### Лента новостей:
![Лента новостей](screenshots/Record_list.png)

### Пример публикации:
![Пример публикации](screenshots/Examp_of_record.png)

### Пример категории:
![Пример категории](screenshots/Examp_of_category.png)

### Админ панель:
![Админ панель](screenshots/Admin_panel.png)

