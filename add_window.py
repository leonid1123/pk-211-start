from PyQt6.QtWidgets import QWidget, QGridLayout, QLabel,\
QLineEdit, QPushButton

class AddKolbasaWindow(QWidget):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.setWindowTitle('Добавление колбасы')
        layout = QGridLayout()
        self.setLayout(layout)

        self.name_entry = QLineEdit()
        self.sostav_entry = QLineEdit()
        self.price_entry = QLineEdit()

        self.add_btn = QPushButton("Добавить колбасу")

        layout.addWidget(QLabel("Название"),0,0)
        layout.addWidget(self.name_entry,0,1)
        layout.addWidget(QLabel("Состав"),1,0)
        layout.addWidget(self.sostav_entry,1,1)
        layout.addWidget(QLabel("Цена"),2,0)
        layout.addWidget(self.price_entry,2,1)
        layout.addWidget(self.add_btn,3,0,1,2)
        


