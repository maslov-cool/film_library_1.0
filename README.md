# film_library_1.0
Программа с графическим пользовательским интерфейсом на PyQt, которая позволяет просматривать и добавлять данные в таблицу Films базы данных films_db.sqlite.
Информацию о фильмах отобразите в табличном виде, а для жанра выведите его текстовое название (подумайте, как это можно сделать с помощью SQL запроса, вот это может помочь). Добавление данных должно быть реализовано путем заполнения данных в отдельные виджеты для каждого поля таблицы films, наиболее подходящие для этого. Виджеты для добавления записи должны располагаться на отдельной форме приложения. После добавления записи необходимо обновить таблицу с отображением данных.

Предусмотрите сообщения для ошибочного пользовательского ввода, такого как, отрицательной длины, года из будущего или отрицательной даты, отсутствие заголовка и т. д.

Руководство к решению:
Класс, реализующий окно приложения, назовите MyWidget. Класс, реализующий форму для добавления записей, назовите AddWidget.

Класс MyWidget должен содержать в себе:
- Таблица tableWidget для отображения фильмов - Кнопка addButton для открытия формы добавления записей. - Поле (переменная) add_form, в которой будет храниться экземпляр класса AddWidget. - Метод adding который и будет открывать форму для добавления записей (кнопке addButton привязывается именно этот метод).
Пример реализации этого метода:

      def adding(self):
          self.add_form = AddWidget(self)
          self.add_form.show()

Класс AddWidget должен содержать в себе:
- Поля title, year, duration реализованные с помощью QPlainTextEdit. - Поле comboBox реализованное с помощью QComboBox, и при заполнении его элементами в нем должны лежать названия жанров которые лежат в БД. - Поле (переменная) params, словарь в котором лежат названия жанров (ключ - название жанра, значение - id жанра в БД). - Кнопка pushButton для сохранения новой записи в БД (обратите внимание, что данные не должны быть сохранены при неверном пользовательском вводе, в этом случае форма должна остаться открытой). - Метод get_adding_verdict, который возвращает True если удалось сохранить новую запись, False если был неверный пользовательский ввод.

После сохранения новой записи в БД класс AddWidget должен закрыться и вызвать у класса MyWidget метод, который отвечает за обновления результата.

Вот небольшая подсказка на то как это можно сделать:

    ...
    self.con.commit()
    self.parent().update_result()
    self.close()
Но чтоб это заработало в инициализации AddWidget должно быть вот это:

  class AddWidget(QMainWindow):
      def __init__(self, parent=None):
          super().__init__(parent)
