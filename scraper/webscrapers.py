from bs4 import BeautifulSoup
import requests,re

def product_finder(product_list, code_memory, code_ram, code_camera, code_sim,screen_size):
    list2=[]
    list = product_list
    str1=''
    for a in list:
        str1= str1 + str(a) + ','
    str1 = str1[:-1]

    myurl_makers = "&sMakers=" + str1

    ########### dahili hafıza


    if len(code_memory)==0:
        myurl_memory=""
    else:
        list_memory_range = [code_memory[0], code_memory[-1]]
        myurl_memory = "nIntMemMin=" + str(list_memory_range[0]) + "&nIntMemMax=" + str(list_memory_range[1]) + "&"

    ############ ram


    if len(code_ram) == 0:
        myurl_ram = ""
    else:
        list_ram_range = [code_ram[0], code_ram[-1]]
        myurl_ram = "nRamMin=" + str(list_ram_range[0]) + "&nRamMax=" + str(list_ram_range[1]) + "&"

    ############ camera

    if len(code_camera) == 0:
        myurl_camera= ""
    else:
        list_camera_range = [code_camera[0], code_camera[-1]]
        myurl_camera = "nCamPrimMin=" + str(list_camera_range[0]) +"&nCamPrimMax=" + str(list_camera_range[1]) + "&"


   ########## sim
    if "DOUBLE" in code_sim:
        myurl_sim = "&sNumberSIMs=1"
    else:
        myurl_sim = ""

   ############ screen size

    if len(screen_size)==0:
        myurl_screen=""
    else:
        list_screen_range=[screen_size[0],screen_size[-1]]
        myurl_screen="fDisplayInchesMin=" +str(list_screen_range[0])+ "&fDisplayInchesMax=" + str(list_screen_range[1]) + "&"
        if 'max' in screen_size:
            myurl_screen="fDisplayInchesMin=" +str(list_screen_range[0])+ "&"

    myurl= "https://www.gsmarena.com/results.php3?" + myurl_ram+ myurl_memory +myurl_screen + myurl_camera + myurl_makers + myurl_sim
    r = requests.get(myurl)
    source = BeautifulSoup(r.content, "lxml")
    products = source.find("div",attrs={"id": "review-body"}).findAll('li')
    product_list1 = []
    for product in products:
        product_title=str(product.find('span').text)
        if product_title.startswith("alcatel"):
            product_title= re.sub(r'alcatel', r'alcatel ', product_title)
            product_list1.append(product_title)
        if product_title.startswith("Apple"):
            product_title= re.sub(r'Apple', r'Apple ', product_title)
            product_list1.append(product_title)
        if product_title.startswith("Asus"):
            product_title= re.sub(r'Asus', r'Asus ', product_title)
            product_list1.append(product_title)
        if product_title.startswith("BlackBerry"):
            product_title= re.sub(r'BlackBerry', r'BlackBerry ', product_title)
            product_list1.append(product_title)
        if product_title.startswith("Honor"):
            product_title= re.sub(r'Honor', r'Honor ', product_title)
            product_list1.append(product_title)
        if product_title.startswith("HTC"):
            product_title= re.sub(r'HTC', r'HTC ', product_title)
            product_list1.append(product_title)
        if product_title.startswith("Huawei"):
            product_title= re.sub(r'Huawei', r'Huawei ', product_title)
            product_list1.append(product_title)
        if product_title.startswith("Lenovo"):
            product_title= re.sub(r'Lenovo', r'Lenovo ', product_title)
            product_list1.append(product_title)
        if product_title.startswith("LG"):
            product_title= re.sub(r'LG', r'LG ', product_title)
            product_list1.append(product_title)
        if product_title.startswith("Nokia"):
            product_title= re.sub(r'Nokia', r'Nokia ', product_title)
            product_list1.append(product_title)
        if product_title.startswith("OnePlus"):
            product_title= re.sub(r'OnePlus', r'OnePlus ', product_title)
            product_list1.append(product_title)
        if product_title.startswith("Oppo"):
            product_title= re.sub(r'Oppo', r'Oppo ', product_title)
            product_list1.append(product_title)
        if product_title.startswith("Samsung"):
            product_title= re.sub(r'Samsung', r'Samsung ', product_title)
            product_list1.append(product_title)
        if product_title.startswith("Sony"):
            product_title= re.sub(r'Sony', r'Sony ', product_title)
            product_list1.append(product_title)
        if product_title.startswith("Xiomi"):
            product_title= re.sub(r'Xiomi', r'Xiomi ', product_title)
            product_list1.append(product_title)

    for product in product_list1:
        url = "https://www.cimri.com/cep-telefonlari?page=1&q=" + str(product)
        r = requests.get(url)
        source = BeautifulSoup(r.content, "lxml")
        available_product_div = source.find("div", attrs={"id": "cimri-product"})
        available_product = available_product_div.find("h3", attrs={"class": "product-title"})

        if available_product_div.find("div", attrs={"class": "coming-soon"}) == None:
            if available_product != None:
                counter = 0
                product_word_by_word = product.split()
                length = len(product_word_by_word)
                for word in product_word_by_word:
                    if word.upper() in available_product_div.find("h3", attrs={"class": "product-title"}).text.upper():
                        counter += 1
                if length == counter:
                    list2.append(product)

    return (list2)


