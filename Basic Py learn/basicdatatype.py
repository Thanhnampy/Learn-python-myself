'''
Các kiểu dữ liệu cơ bản trong Python: 
https://www.youtube.com/watch?v=FBfayv31Doo&list=PLJcWUrckOCKK7tXpLTJJsl1MD98bQHHOg&index=5

    Bool    kiểu dữ liệu True or False
    None    kiểu dữ liệu empty
    int     kiểu dữ liệu số nguyên
    float   kiểu dữ liệu số thực
    str     kiểu dữ liệu chuỗi

'''

'''
Topic #0: bool & None
'''
# [x] bool: True & False
# var_bool = True

# [x] type(): Dynamically typed
# print(type(var_bool))

# Numerically, they are evaluated as int with value 1 (True), 0 (False)
# Ex:
a = 1 + True
print(f"{a}")

# b = False
# if b == 0:
#     print("b is 0")


'''
None: Phần tử không
'''
# var_none = None
# print(type(var_none))



'''
None is often used as a placeholder for optional or missing value
It evaluetes as False in conditionals

'''

# email_address = None #False
# email_address = "namnt3102@gmail.com"

# if email_address:
#     print(f"Email address is {email_address}")
# else:
#     print(f"Email address is empty or {email_address}")

'''
Topic #1: Number (int & float)

'''
#int
# print(type(1)) 
# print(type(0))
# print(type(-10))

#Float
# print(type(1.5)) 
# print(type(0.33))
# print(type(4E2), 4E2) # 4*10(^2)

'''
[] Arithmetic: Các phép toán: + - * / ** / // %

'''
# print(10+3)
# print(10-3)
# print(10*3)
# print(10**3) #10^3=10*10*10
# print(10/3)  # chia lấy phần thập phân = 3.333333
# print(10//3) # Chia lấy phần nguyên = 3
# print(10%3)  # chia lấy dư = 1


'''
[] Basic function (hàm cơ bản)

'''

# print(pow(10,3))           #10**3
# print(abs(-6.9))           #lấy trị tuyệt đối = 6.9
# print(round(6.65))         #làm tròn số
# print(round(5.468, 2))     #làm tròn số thập phân thứ 2 = 5.47
# print(bin(256))            # chuyển từ hệ 10 sang hệ 2
# print(hex(256))            # chuyển từ hệ 10 sang hệ 16

