import mysql.connector

try:
    con = mysql.connector.connect(host='159.203.44.241', port= '64306', database='acqua', user='cris', password='Acqua@cris2019')
    
    if con.is_connected():
        db_info = con.get_server_info()
        print("Conectado ao servidor MySQL versão: ", db_info)
        cursor = con.cursor()
        cursor.execute("select database();")
        linha = cursor.fetchone()
        print("Conectado ao banco de dados: ", linha)
   
except OSError as e:
    print("Erro ao acessar tabela MySQL: ", e)
