__author__ = 'afox'

# Imports
import pymssql as sql
import _mssql as sql2


def _post_login():
    conn = sql2.connect(
        server=r'sunflower.arvixe.com',
        user=r'hacknash',
        password=r'hacknash',
        database=r'hacknash'
    )

    query = "exec ryan.Hack_insert_client  @Username='test', @password='test' , @companyname='test' , @address='test' , @MajorInterest='test' , @address2='test' , @city='test' , @state='test' , @zip='37211'"

    conn.execute_query(query)

    return


def test():
    return


if "__main__" == __name__:
    _post_login()
    pass