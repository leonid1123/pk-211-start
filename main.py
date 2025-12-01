#шаблон https://www.pythontutorial.net
#https://github.com/leonid1123/pk-211-start
# повторить подключение и работу с БД
# создать модуль для бд
# создать модуль для интерфейса
import sys
from pathlib import Path
from PyQt6.QtWidgets import QApplication, QWidget, QGridLayout, QListWidget,\
QPushButton, QLineEdit, QLabel, QMainWindow
import pymysql.cursors
from add_window import AddKolbasaWindow
from db import DbHandler

class MainWindow(QMainWindow):
    """
    Основной класс программы
    """
    def __init__(self, *args, **kwargs):
        """
        Конструктор класса
        """
        super().__init__(*args, **kwargs)
        self.conn = None
        self.cur = None
        self.add_kolbasa = None
        self.setWindowTitle('КОЛБАСА!!!!')
        main_widget = QWidget()
        self.setCentralWidget(main_widget)
        layout = QGridLayout()
        main_widget.setLayout(layout)

        self.kolbasa_view = QListWidget()
        self.show_all_btn = QPushButton("Показать")
        self.show_all_btn.clicked.connect(self.get_all)
        self.clear_all_btn = QPushButton("Очистить список")
        self.clear_all_btn.clicked.connect(self.clear_view)
        self.add_kolbasa_btn = QPushButton("Добавить колбасу")
        self.add_kolbasa_btn.clicked.connect(self.add_kolbasa_new_window)

        layout.addWidget(QLabel('Список колбасы'),0,0,1,2)
        layout.addWidget(self.kolbasa_view,1,0,1,2)
        layout.addWidget(self.show_all_btn,2,0)
        layout.addWidget(self.clear_all_btn,2,1)
        layout.addWidget(self.add_kolbasa_btn,3,0,1,2)
        self.show()

    def clear_view(self):
        """
        Метод для очистки списка
        """
        self.kolbasa_view.clear()

    def get_all(self):
        """
        Метод для получения всех записей из базы данных
        """
        #разобраться с обработкой ошибок
        sql = 'SELECT * FROM kolbasa'
        ans = DbHandler.make_select_request(sql)
        if ans != -1:
            self.kolbasa_view.clear()
            for item in ans:
                txt = f"{item[1]} {item[2]} {item[3]}"
                self.kolbasa_view.addItem(txt)

    def add_kolbasa_new_window(self):
        '''
        Метод создания окна для редактирования записей в БД
        '''
        self.add_kolbasa = AddKolbasaWindow()
        self.add_kolbasa.show()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    app.setStyleSheet(Path('style.qss').read_text(encoding='utf8'))
    window = MainWindow()
    sys.exit(app.exec())
