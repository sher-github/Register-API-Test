import requests
import json

#Get database
database = requests.get('https://reqres.in/api/users?page=1')
# print (database.json())
database = database.json()

# print (database['data'])

#Get all email
email_list= []

for i in database['data']:
    email = i['email']
    email_list.append(email)
#print(email_list)

#Register URL
register_url = 'https://reqres.in/api/register'

#Test 1: input email and password
print('~ Result of Test 1 ~ \n')

for i in range(len(email_list)):
  input_1 = {'email': email_list[i], 'password': 'pistol'}

  result_1 = requests.post(register_url, data = input_1)

  print("Input: " + email_list[i])
  print("Status: " + str(result_1.status_code))
  print('Response: ' + str(result_1.json()) + '\n')

#Test 2: input email
print('~ Result of Test 2 ~ \n')

for i in range(len(email_list)):
  input_2 = {'email': email_list[i]}

  result_2 = requests.post(register_url, data = input_2)

  print("Input: " + email_list[i])
  print("Status: " + str(result_2.status_code))
  print('Response: ' + str(result_2.json()) + '\n')

#Test 3: input password
print('~ Result of Test 3 ~ \n')

input_3 = {'password': 'pistol'}

result_3 = requests.post(register_url, data = input_3)

print("Status: " + str(result_3.status_code))
print('Response: ' + str(result_3.json()) + '\n')

#Test 4: input the incorrect email
print('~ Result of Test 4 ~ \n')

input_4 = {'email': 'abc@reqres.in', 'password': 'pistol'}

result_4 = requests.post(register_url, data = input_4)

print("Status: " + str(result_4.status_code))
print('Response: ' + str(result_4.json()) + '\n')


