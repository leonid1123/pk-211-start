#шаблон https://www.pythontutorial.net
#https://github.com/leonid1123/pk-211-start
# повторить подключение и работу с БД
# создать модуль для бд
# создать модуль для интерфейса
import sys
from pathlib import Path
from PyQt6.QtWidgets import QApplication, QWidget, QGridLayout, QListWidget,\
QPushButton, QLineEdit, QLabel
import pymysql.cursors

class MainWindow(QWidget):
    """
    Основной класс программы
    """
    def __init__(self, *args, **kwargs):
        """
        Конструктор класса
        """
        super().__init__(*args, **kwargs)
        self.setWindowTitle('КОЛБАСА!!!!')
        self.showMaximized()
        layout = QGridLayout()
        self.setLayout(layout)

        self.kolbasa_view = QListWidget()
        self.show_all_btn = QPushButton("Показать")
        self.show_all_btn.clicked.connect(self.get_all)
        self.clear_all_btn = QPushButton("Очистить список")
        self.clear_all_btn.clicked.connect(self.clear_view)

        layout.addWidget(QLabel('Список колбасы'),0,0,1,2)
        layout.addWidget(self.kolbasa_view,1,0,1,2)
        layout.addWidget(self.show_all_btn,2,0)
        layout.addWidget(self.clear_all_btn,2,1)
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
        self.conn = pymysql.connect(
            host='localhost',
            user='pk211',
            password='1234',
            database='pk211_kolbasa'
        )
        self.cur = self.conn.cursor()
        self.cur.execute('SELECT * FROM kolbasa')
        ans = self.cur.fetchone()
        self.kolbasa_view.clear()
        while ans is not None:
            self.kolbasa_view.addItem(f"{ans[1]} {ans[2]} {ans[3]}")
            ans = self.cur.fetchone()
        

if __name__ == '__main__':
    app = QApplication(sys.argv)
    app.setStyleSheet(Path('style.qss').read_text())
    window = MainWindow()
    sys.exit(app.exec())
    
