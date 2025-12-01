import pymysql.cursors
from PyQt6.QtWidgets import QMessageBox
class DbHandler():
    '''
    статический класс для работы с БД
    '''
    @staticmethod
    def make_select_request(_sql):
        '''
        статический метод для запросов SELECT к БД
        '''
        try:
            conn = pymysql.connect(
                host='localhost',
                user='pk211',
                password='1234',
                database='pk211_kolbasa'
            )
            cur = conn.cursor()
            cur.execute(_sql)
            ans = cur.fetchall()
            return ans
        except pymysql.Error:
            QMessageBox.warning(
            'Ошибка.',
            'Проблема с БД'
            )
            return -1

    @staticmethod
    def make_insert_request(_sql, _args):
        '''
        статический метод для запросов INSERT к БД
        '''
        conn = pymysql.connect(
            host='localhost',
            user='pk211',
            password='1234',
            database='pk211_kolbasa'
        )
        cur = conn.cursor()
        cur.execute(_sql,_args)
        conn.commit()
