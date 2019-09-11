from bs4 import BeautifulSoup
import requests,re

def product_finder():
    product_list1=["Apple iPhone 11 Pro Max"]
    list2=[]


    for product in product_list1:
        url= "https://www.cimri.com/cep-telefonlari?page=1&q="+ str(product)
        r = requests.get(url)
        source = BeautifulSoup(r.content, "lxml")
        available_product_div = source.find("div", attrs={"id": "cimri-product"})
        available_product= available_product_div.find("h3", attrs={"class": "product-title"})

        if available_product_div.find("div", attrs={"class": "coming-soon"}) == None:
            if available_product != None:
                counter = 0
                product_word_by_word = product.split()
                length = len(product_word_by_word)
                for word in product_word_by_word:
                    if word.upper() in available_product.text.upper():
                        counter += 1
                if length == counter:
                    list2.append(product)
                else:
                    print("cimride bulunamayan ürün" + product)
            else:
                print("none type" + product)
        else:
            print(product +" cimride satışta değil")
        print(list2)

product_finder()