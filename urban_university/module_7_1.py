import os.path

class Product:
    name=""
    weight=0.0
    category=""
    def __str__(self):
        return f"{self.name}, {self.weight}, {self.category}"
    def __init__(self,name,weight,category):
        self.name=name
        self.weight=weight
        self.category=category

class Shop:
     __file_name = "products.txt"
     __file_path=""
     __product_line=""
     __errors=["Не найден файл",
               "Работаем только с объектами Product"]

     def __init__(self):
         self.__file_path=os.path.dirname(os.path.realpath(__file__))+"\\"+self.__file_name
     def __file_exists(self):
         return os.path.exists(self.__file_path)
     def __is_product_exists(self,product):
         product_list = self.get_products().split("\n")
         finded=False
         for prod in product_list:
             if(prod.split(",")[0]==product.name):
                 finded=True
                 break
         return finded
     
     def get_products(self):
         if(not self.__file_exists()):
             print(self.__errors[0])
             return ""
         result=""
         file=open(self.__file_path,"r")
         result=file.read()
         file.close()
         return result
     def add(self, *products):
         for prod in products:
             if(not isinstance(prod,Product)):
                 print(self.__errors[1])
                 return False
             if(self.__is_product_exists(prod)):
                 #prod.weight+=
                 print(f"Продукт {prod.name} уже есть в магазине, его общий вес теперь равен {prod.weight}")
                 continue
             else:
                 #if(not self.__file_exists()):
                 #    f=open(self.__file_path,"a")
                 #    f.close()
                 with open(self.__file_path,"a") as f:
                     f.writelines(prod.__str__()+"\n")
                 f.close()

s1 = Shop()
p1 = Product('Potato', 50.5, 'Vegetables')
p2 = Product('Spaghetti', 3.4, 'Groceries')
p3 = Product('Potato', 5.5, 'Vegetables')

print(p2) # __str__

s1.add(p1, p2, p3)

print(s1.get_products())