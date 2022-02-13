# Register-API-Test

## Description
測試註冊的 API

參考網站：https://reqres.in/

## Test Case

| ID  | 題目 | 預期結果  | 實際結果 | 
| --- | --- | --- | --- |
| 1  | 使用者同時輸入 email 和 password 是否成功註冊 | 成功註冊，回傳200 | Pass | 
| 2  | 使用者只輸入 email 是否成功註冊  | 不能註冊，回傳400 | Pass | 
| 3  | 使用者只輸入 password 是否成功註冊  | 不能註冊，回傳400 | Pass | 
| 4  | 使用者輸入 database 沒有的 email, 是否成功註冊 | 不能註冊，回傳400 | Pass | 
| 5  | Password 符合長度範圍  | 成功註冊，回傳200 |  | 
| 6  | Password 不符合長度範圍  | 不能註冊，回傳400 |  | 
| 7  | Password 符合小寫，大寫，數字格式  | 成功註冊，回傳200 |  | 
| 8  | Password 不符合小寫，大寫，數字格式  | 不能註冊，回傳400 |  | 
| 9  | 輸入 email 和 password 後等待的時間  | 符合預期標準 |  | 
| 10  | 後端是否接收到 email 和 password  | 已儲存在 database|  | 

## Result

```
~ Result of Test 1 ~ 

Input: george.bluth@reqres.in
Status: 200
Response: {'id': 1, 'token': 'QpwL5tke4Pnpja7X1'}

Input: janet.weaver@reqres.in
Status: 200
Response: {'id': 2, 'token': 'QpwL5tke4Pnpja7X2'}

Input: emma.wong@reqres.in
Status: 200
Response: {'id': 3, 'token': 'QpwL5tke4Pnpja7X3'}

Input: eve.holt@reqres.in
Status: 200
Response: {'id': 4, 'token': 'QpwL5tke4Pnpja7X4'}

Input: charles.morris@reqres.in
Status: 200
Response: {'id': 5, 'token': 'QpwL5tke4Pnpja7X5'}

Input: tracey.ramos@reqres.in
Status: 200
Response: {'id': 6, 'token': 'QpwL5tke4Pnpja7X6'}

~ Result of Test 2 ~ 

Input: george.bluth@reqres.in
Status: 400
Response: {'error': 'Missing password'}

Input: janet.weaver@reqres.in
Status: 400
Response: {'error': 'Missing password'}

Input: emma.wong@reqres.in
Status: 400
Response: {'error': 'Missing password'}

Input: eve.holt@reqres.in
Status: 400
Response: {'error': 'Missing password'}

Input: charles.morris@reqres.in
Status: 400
Response: {'error': 'Missing password'}

Input: tracey.ramos@reqres.in
Status: 400
Response: {'error': 'Missing password'}

~ Result of Test 3 ~ 

Status: 400
Response: {'error': 'Missing email or username'}

~ Result of Test 4 ~ 

Status: 400
Response: {'error': 'Note: Only defined users succeed registration'}
```
