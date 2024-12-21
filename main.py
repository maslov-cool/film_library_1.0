import io
import sys
import sqlite3

from PyQt6 import uic  # Импортируем uic
from PyQt6.QtWidgets import QApplication, QMainWindow, QTableWidgetItem
from PyQt6.QtGui import QColor

template1 = """<?xml version="1.0" encoding="UTF-8"?>
<ui version="4.0">
 <class>MainWindow</class>
 <widget class="QMainWindow" name="MainWindow">
  <property name="geometry">
   <rect>
    <x>0</x>
    <y>0</y>
    <width>800</width>
    <height>600</height>
   </rect>
  </property>
  <property name="minimumSize">
   <size>
    <width>800</width>
    <height>600</height>
   </size>
  </property>
  <property name="maximumSize">
   <size>
    <width>800</width>
    <height>600</height>
   </size>
  </property>
  <property name="windowTitle">
   <string>Фильмотека</string>
  </property>
  <widget class="QWidget" name="centralwidget">
   <widget class="QPushButton" name="addButton">
    <property name="geometry">
     <rect>
      <x>0</x>
      <y>0</y>
      <width>171</width>
      <height>61</height>
     </rect>
    </property>
    <property name="font">
     <font>
      <pointsize>18</pointsize>
     </font>
    </property>
    <property name="text">
     <string>Добавить</string>
    </property>
   </widget>
   <widget class="QTableWidget" name="tableWidget">
    <property name="geometry">
     <rect>
      <x>0</x>
      <y>60</y>
      <width>800</width>
      <height>500</height>
     </rect>
    </property>
   </widget>
  </widget>
  <widget class="QMenuBar" name="menubar">
   <property name="geometry">
    <rect>
     <x>0</x>
     <y>0</y>
     <width>800</width>
     <height>26</height>
    </rect>
   </property>
  </widget>
  <widget class="QStatusBar" name="statusbar"/>
 </widget>
 <resources/>
 <connections/>
</ui>
"""


class MyWidget(QMainWindow):
    def __init__(self):
        super().__init__()
        f = io.StringIO(template1)
        uic.loadUi(f, self)

        self.draw_result()
        self.addButton.clicked.connect(self.adding)
        self.add_form = AddWidget(parent=self)

    def adding(self):
        self.add_form.show()

    def draw_result(self):
        con = sqlite3.connect('films_db.sqlite')
        cursor = con.cursor()
        result = cursor.execute("SELECT films.id, films.title, films.year, genres.title, films.duration FROM films"
                                " JOIN genres ON films.genre = genres.id").fetchall()[::-1]
        self.tableWidget.setRowCount(len(result))
        self.tableWidget.setColumnCount(len(result[0]))

        # Закрашиваем шапку таблицы (горизонтальные заголовки)
        self.tableWidget.horizontalHeader().setStyleSheet(
            "QHeaderView::section { background-color: rgb(255, 170, 127);}")

        # Закрашиваем боковую шапку таблицы (вертикальные заголовки)
        self.tableWidget.verticalHeader().setStyleSheet(
            "QHeaderView::section { background-color: rgb(255, 170, 127);}")

        # Устанавливаем заголовки столбцов
        header_labels = ['ИД', 'Название', 'Год выпуска', 'Жанр', 'Продолжительность']
        self.tableWidget.setHorizontalHeaderLabels(header_labels)

        for i, elem in enumerate(result):
            for j, val in enumerate(elem):
                item = QTableWidgetItem(str(val))
                item.setBackground(QColor(85, 255, 255))
                self.tableWidget.setItem(i, j, item)

        con.close()

    def update_result(self):
        self.draw_result()


template2 = """<?xml version="1.0" encoding="UTF-8"?>
<ui version="4.0">
 <class>MainWindow</class>
 <widget class="QMainWindow" name="MainWindow">
  <property name="geometry">
   <rect>
    <x>0</x>
    <y>0</y>
    <width>500</width>
    <height>350</height>
   </rect>
  </property>
  <property name="minimumSize">
   <size>
    <width>500</width>
    <height>350</height>
   </size>
  </property>
  <property name="maximumSize">
   <size>
    <width>500</width>
    <height>350</height>
   </size>
  </property>
  <property name="windowTitle">
   <string>Добавить элемент</string>
  </property>
  <widget class="QWidget" name="centralwidget">
   <widget class="QLabel" name="label">
    <property name="geometry">
     <rect>
      <x>10</x>
      <y>20</y>
      <width>141</width>
      <height>31</height>
     </rect>
    </property>
    <property name="font">
     <font>
      <pointsize>12</pointsize>
     </font>
    </property>
    <property name="text">
     <string>Название</string>
    </property>
   </widget>
   <widget class="QLabel" name="label_2">
    <property name="geometry">
     <rect>
      <x>10</x>
      <y>70</y>
      <width>141</width>
      <height>31</height>
     </rect>
    </property>
    <property name="font">
     <font>
      <pointsize>12</pointsize>
     </font>
    </property>
    <property name="text">
     <string>Год выпуска</string>
    </property>
   </widget>
   <widget class="QLabel" name="label_3">
    <property name="geometry">
     <rect>
      <x>10</x>
      <y>110</y>
      <width>141</width>
      <height>41</height>
     </rect>
    </property>
    <property name="font">
     <font>
      <pointsize>12</pointsize>
     </font>
    </property>
    <property name="text">
     <string>Жанр</string>
    </property>
   </widget>
   <widget class="QLabel" name="label_4">
    <property name="geometry">
     <rect>
      <x>10</x>
      <y>170</y>
      <width>131</width>
      <height>41</height>
     </rect>
    </property>
    <property name="font">
     <font>
      <pointsize>12</pointsize>
     </font>
    </property>
    <property name="text">
     <string>Длина</string>
    </property>
   </widget>
   <widget class="QComboBox" name="comboBox">
    <property name="geometry">
     <rect>
      <x>180</x>
      <y>130</y>
      <width>311</width>
      <height>31</height>
     </rect>
    </property>
    <property name="font">
     <font>
      <pointsize>12</pointsize>
     </font>
    </property>
   </widget>
   <widget class="QPushButton" name="pushButton">
    <property name="geometry">
     <rect>
      <x>320</x>
      <y>240</y>
      <width>151</width>
      <height>51</height>
     </rect>
    </property>
    <property name="font">
     <font>
      <pointsize>14</pointsize>
     </font>
    </property>
    <property name="text">
     <string>Добавить</string>
    </property>
   </widget>
   <widget class="QPlainTextEdit" name="title">
    <property name="geometry">
     <rect>
      <x>180</x>
      <y>20</y>
      <width>311</width>
      <height>31</height>
     </rect>
    </property>
   </widget>
   <widget class="QPlainTextEdit" name="year">
    <property name="geometry">
     <rect>
      <x>180</x>
      <y>70</y>
      <width>311</width>
      <height>31</height>
     </rect>
    </property>
   </widget>
   <widget class="QPlainTextEdit" name="duration">
    <property name="geometry">
     <rect>
      <x>180</x>
      <y>190</y>
      <width>311</width>
      <height>31</height>
     </rect>
    </property>
   </widget>
  </widget>
  <widget class="QMenuBar" name="menubar">
   <property name="geometry">
    <rect>
     <x>0</x>
     <y>0</y>
     <width>500</width>
     <height>26</height>
    </rect>
   </property>
  </widget>
  <widget class="QStatusBar" name="statusbar"/>
 </widget>
 <resources/>
 <connections/>
</ui>
"""


class AddWidget(QMainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        f = io.StringIO(template2)
        uic.loadUi(f, self)
        self.parent = parent

        # Открываем соединение с БД
        con = sqlite3.connect('films_db.sqlite')
        cursor = con.cursor()
        self.params = {j: i for i, j in cursor.execute("SELECT * FROM genres").fetchall()}

        for i in self.params.keys():
            self.comboBox.addItem(i)

        self.pushButton.clicked.connect(self.get_adding_verdict)
        con.close()

    def get_adding_verdict(self):
        try:
            title = self.title.toPlainText()
            year = self.year.toPlainText()
            duration = self.duration.toPlainText()
            genre = self.comboBox.currentText()
            if not title or not year or not duration or not int(duration) > 0 or not 0 <= int(year) < 2025:
                raise ValueError
        except ValueError:
            self.statusbar.showMessage('Неверно заполнена форма')
            return False
        con = sqlite3.connect('films_db.sqlite')
        cursor = con.cursor()
        query = '''INSERT INTO films (title, year, genre, duration) VALUES (?, ?, ?, ?)'''
        values = (title, year,
                  cursor.execute('SELECT id FROM genres WHERE title = ?', (genre,)).fetchall()[0][0], duration)
        cursor.execute(query, values)
        con.commit()
        con.close()
        self.parent.update_result()
        self.close()
        return True


def except_hook(cls, exception, traceback):
    sys.__excepthook__(cls, exception, traceback)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyWidget()
    ex.show()
    sys.excepthook = except_hook
    sys.exit(app.exec())
