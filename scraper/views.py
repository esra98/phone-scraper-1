from django.shortcuts import render
from .webscrapers import product_finder
from django.core.mail import send_mail



def home_page(request):
   return render(request, 'home_page.html')


def search(request):
   if request.method == 'POST':
      list = request.POST.getlist('brands')
      code_list = []
      if 'alcatel' in list:
          code_list.append(5)
      if 'Apple' in list:
          code_list.append(48)
      if 'Asus' in list:
          code_list.append(46)
      if 'BlackBerry' in list:
          code_list.append(36)
      if 'Honor' in list:
          code_list.append(121)

      if 'HTC' in list:
          code_list.append(45)
      if 'Huawei' in list:
          code_list.append(58)
      if 'Lenovo' in list:
          code_list.append(73)
      if 'LG' in list:
          code_list.append(20)
      if 'Nokia' in list:
          code_list.append(1)
      if 'OnePlus' in list:
          code_list.append(95)
      if 'Oppo' in list:
          code_list.append(82)
      if 'Samsung' in list:
          code_list.append(9)
      if 'Sony' in list:
          code_list.append(7)
      if 'Xiomi' in list:
          code_list.append(80)
      list1 = request.POST.getlist('memory')
      code_memory = []
      if '64MB' in list1:
          code_memory.append(64)
      if '128MB' in list1:
          code_memory.append(128)
      if '256MB' in list1:
          code_memory.append(256)
      if '512MB' in list1:
          code_memory.append(512)
      if '1GB' in list1:
          code_memory.append(1000)
      if '2GB' in list1:
          code_memory.append(2000)
      if '4GB' in list1:
          code_memory.append(4000)
      if '8GB' in list1:
          code_memory.append(8000)
      if '16GB' in list1:
          code_memory.append(16000)
      if '32GB' in list1:
          code_memory.append(32000)
      if '64GB' in list1:
          code_memory.append(64000)
      if '128GB' in list1:
          code_memory.append(128000)
      if '256GB' in list1:
          code_memory.append(256000)
      if '512GB' in list1:
          code_memory.append(512000)
      list2 = request.POST.getlist('ram')
      code_ram = []
      if '16MB' in list2:
          code_ram.append(16)
      if '32MB' in list2:
          code_ram.append(32)
      if '64MB' in list2:
          code_ram.append(64)
      if '128MB' in list2:
          code_ram.append(128)
      if '256MB' in list2:
          code_ram.append(256)
      if '512MB' in list2:
          code_ram.append(512)
      if '768MB' in list2:
          code_ram.append(768)
      if '1GB' in list2:
          code_ram.append(1000)
      if '1.5GB' in list2:
          code_ram.append(1500)
      if '2GB' in list2:
          code_ram.append(2000)
      if '3GB' in list2:
          code_ram.append(3000)
      if '4GB' in list2:
          code_ram.append(4000)
      if '6GB' in list2:
          code_ram.append(6000)
      if '8GB' in list2:
          code_ram.append(8000)
      if '10GB' in list2:
          code_ram.append(10000)
      list3 = request.POST.getlist('camera')
      code_camera = []
      if '1MP' in list3:
          code_camera.append(1)
      if '2MP' in list3:
          code_camera.append(2)
      if '3MP' in list3:
          code_camera.append(3)
      if '4MP' in list3:
          code_camera.append(4)
      if '5MP' in list3:
          code_camera.append(5)
      if '8MP' in list3:
          code_camera.append(8)
      if '10MP' in list3:
          code_camera.append(10)
      if '12MP' in list3:
          code_camera.append(12)
      if '13MP' in list3:
          code_camera.append(13)
      if '16MP' in list3:
          code_camera.append(16)

      list4 = request.POST.getlist('sim')
      code_sim = []
      if 'double' in list4:
          code_sim.append("DOUBLE")

      list5 = request.POST.getlist('screen_size')
      screen_size = []
      if '5.5' in list5:
          screen_size.append(5.5)
      if '5.6' in list5:
          screen_size.append(5.6)
      if '5.7' in list5:
          screen_size.append(5.7)
      if '5.8' in list5:
          screen_size.append(5.8)
      if '5.9' in list5:
          screen_size.append(5.9)
      if '6' in list5:
          screen_size.append(6)
      if '6.1' in list5:
          screen_size.append(6.1)
      if '6.2' in list5:
          screen_size.append(6.2)
      if '6.3' in list5:
          screen_size.append(6.3)
      if '6.4' in list5:
          screen_size.append(6.4)
      if '6.5' in list5:
          screen_size.append(6.5)
      if 'max' in list5:
          screen_size.append("max")

   product_list=product_finder(code_list, code_memory, code_ram, code_camera, code_sim, screen_size)
   return render(request, 'result_page.html', {"list": product_list})


def mail_the_products(request):
    if request.method == "POST":
        mail_adress = request.POST.get("mailaddress")
        selected_products = request.POST.getlist('mail_list')
        str_list = ""
        for product in selected_products:
            str_list = str_list + str(product) + " \n"

        string = "merhaba, \nlistenizdeki ürünler aşağıdadır: \n" + str_list
        send_mail(
            'ürün listesi',
            string ,
            'web_project@hushmail.com',
            [mail_adress],
            fail_silently=False
    )
    return render(request, 'send_success.html')
