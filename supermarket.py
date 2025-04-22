
import sqlite3

class Product():

    def __init__(self,product_id,product_name,product_exp):
        self.product_id = product_id
        self.product_name = product_name
        self.product_exp = product_exp
    
    def __str__(self):
        
        return "ID : {}\nName : {}\nExpiration Date : {}\n".format(self.product_id,self.product_name,self.product_exp)

class Supermarketdb():
    
    def __init__(self):
        self.create_connection()
    
    def create_connection(self):
        self.conncetion = sqlite3.connect("Supermarket.db")
        self.cursor = self.conncetion.cursor()
        query = "CREATE TABLE IF NOT EXISTS Supermarket (id INT,name TEXT,exp INT)"
        self.cursor.execute(query)
        self.conncetion.commit()
    
    def disconnect(self):
        self.conncetion.close()
    
    def view_products(self):

        query = "SELECT * FROM Supermarket"
        self.cursor.execute(query)

        products = self.cursor.fetchall()

        if (len(products) == 0 ):
            print("There isn't any product in stock")
        else:
            for i in products:
                product = Product(i[0],i[1],i[2])
                print(product)
    
    def product_query(self,name):
        
        query = "SELECT * FROM Supermarket where name = ?"

        self.cursor.execute(query,(name,))

        products = self.cursor.fetchall()

        if (len(products) == 0 ):
            print("There isn't any product in stock")
        else:
            product = Product(products[0][0],products[0][1],products[0][2])
            print(product)
    
    def add_product(self, product):
        query = "INSERT INTO Supermarket VALUES (?,?,?)"
        self.cursor.execute(query, (product.product_id, product.product_name, product.product_exp)) 
        self.conncetion.commit()

    def del_product(self, name):
        query = "DELETE FROM Supermarket WHERE name = ?"
        self.cursor.execute(query, (name,))
        
        if self.cursor.rowcount == 0:
            print("There isn't any product in stock")
        
        self.conncetion.commit()
    
    
