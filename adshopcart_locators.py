import datetime
from faker import Faker
fake = Faker(locale='en_CA')


# ___________________-- eCommerce App Data Parameters______________________
app = 'Advantage Shopping Cart'
Advantage_Shopping_Cart_url = 'https://advantageonlineshopping.com/#/'
Advantage_Shopping_home_page_title = 'Advantage Shopping'
product_list = ['SPEAKERS', 'TABLETS', 'HEADPHONES', 'LAPTOPS', 'MICE']

admin_username = 'sylviakaranja'
admin_password = 'Vanilla!87'

new_username = fake.user_name()
new_password = fake.password()
first_name = fake.first_name()
last_name = fake.last_name()
middle_name = fake.first_name()
full_name = f'{first_name} {last_name}'
email = fake.email()
subject = f'Today is: {datetime.datetime.now()}. '

list_of_interest = [fake.job(), fake.job(), fake.job()]

moodle_net_profile = f'https://moodle.net/{new_username}'
city = fake.city()
country = fake.current_country()
province = fake.province()[0:10]
postal_code = fake.pyint(111,999)
description = f'User added by {admin_username} via Python Selenium Automated script on {datetime.datetime.now()}' # fake.sentence(nb_words=100)
pic_desc = f'Image submitted by {full_name}'
sysid = ''

webpage = fake.url()
icq_num = fake.pyint(111111,999999)
id_skype = new_username
id_aim = f'{new_username}{fake.pyint(111,999)}'
id_yahoo = fake.user_name()
id_msn = fake.user_name()
id_idnumber = fake.pyint(1111111,9919999)

id_institution = fake.company()
id_department = fake.catch_phrase()
phonenum1 = fake.phone_number()
phonenum2 = fake.phone_number()
address = fake.address().replace("\n", " ")[0:50]


lst_opt = ['Web page', 'ICQ number', 'Skype ID', 'AIM ID', 'Yahoo ID', 'MSN ID',
           'ID number', 'Institution', 'Department', 'Phone', 'Mobile phone', 'Address']

lst_ids = ['id_url', 'id_icq', 'id_skype', 'id_aim', 'id_yahoo', 'id_msn',
           'id_idnumber', 'id_institution', 'id_department', 'id_phone1', 'id_phone2', 'id_address']

lst_val = [webpage, icq_num, id_skype, id_aim, id_yahoo, id_msn,
           id_idnumber, id_institution, id_department, phonenum1, phonenum2, address]


#_________________________________________________________________