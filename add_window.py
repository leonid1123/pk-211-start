from PyQt6.QtWidgets import QWidget, QGridLayout, QLabel,\
QLineEdit, QPushButton, QMessageBox
from db import DbHandler

class AddKolbasaWindow(QWidget):
    """
    класс для окна для добавления записей
    """
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.setWindowTitle('Добавление колбасы')
        layout = QGridLayout()
        self.setLayout(layout)

        self.name_entry = QLineEdit()
        self.sostav_entry = QLineEdit()
        self.price_entry = QLineEdit()

        self.add_btn = QPushButton("Добавить колбасу")
        self.add_btn.clicked.connect(self.add_new_kolbasa)

        layout.addWidget(QLabel("Название"),0,0)
        layout.addWidget(self.name_entry,0,1)
        layout.addWidget(QLabel("Состав"),1,0)
        layout.addWidget(self.sostav_entry,1,1)
        layout.addWidget(QLabel("Цена"),2,0)
        layout.addWidget(self.price_entry,2,1)
        layout.addWidget(self.add_btn,3,0,1,2)
        
    def add_new_kolbasa(self):
        '''
        метод(слот) для добавления записи
        '''
        name = self.name_entry.text().strip()
        sostav = self.sostav_entry.text().strip()
        price = self.price_entry.text().strip()
        if price.isdigit():
            price = int(price)
            sql = '''INSERT INTO kolbasa(`название`,`состав`,`цена`)
            VALUES(%s,%s,%s)
            '''
            DbHandler.make_insert_request(sql,(name,sostav,price))
            self.close()
        else:
            QMessageBox.warning(
            self,
            'Ошибка.',
            'В поле ЦЕНА можно писать только цифры!'
        )
