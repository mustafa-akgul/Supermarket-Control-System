from supermarket import Supermarketdb,Product


import time

print("""***************************************************
      

Welcome to Supermarket Warehouse Control System


***************************************************
1- View products in warehouse
2- Find product
3- Add product
4- Delete product      
5- Press 'q' to exit
      
***************************************
""")

supermarket1 = Supermarketdb()
while True:
    query = input("Which action would you like to take : ")
    if (query == 'q'):
        print("Check out...")
        time.sleep(2)
        break
    elif(query == '1'):
        supermarket1.view_products()
        
    elif(query == '2'):
        name = input("Enter the name of the product you want to search : ")
        supermarket1.product_query(name)
    elif(query == '3'):
        id = input("Enter id of new product : ")
        name = input("Enter name of new product : ")
        exp = input("Enter exp of new product : ")
        product = Product(id,name,exp)
        supermarket1.add_product(product)
        
    elif(query == '4'):
        name = input("Enter the name of the product you want to delete : ")
        print("Product is being deleted..")
        time.sleep(2)
        supermarket1.del_product(name)
    
    else:
        print("Incorrect entry")
        time.sleep(2)