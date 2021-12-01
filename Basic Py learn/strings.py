'''
Topic #2: Strings (chuỗi ký tự) - a sequence of characters
'''
# String: ordered(theo thứ tự), imutable(không thể thay đỏi được), text presentation

# Use singe or double qoutes

# Escaping backslash  "\" cho phép dùng cả 2 dấu nháy đơn và nháy kép trong câu lệnh print
    # Ex1: my_string = ('I\'m a "student"')
    # Ex2: my_string = (" I'm a \"student\" ")
    # print(my_string, type(my_string))

''' 
Backslash if you want to continue in the next line
(Dùng để xuống dòng cho gọn code nhưng in ra vẫn ở cùng 1 dòng)
'''
#Ex:
# my_string = "vi mot tuong lai tuoi sang \
# hay co gang hoc python"
# print(my_string)

'''
Access characters and substrings
get character by referring to index (lấy 1 ký tự)
'''
    # my_string = "Hello world"
    # char = my_string[0] # lấy chữ H
    # print(char)
    # char = my_string[6] # lấy chữ W
    # print(char)
    # char = my_string[-1] # lấy ký tự cuối là chũ d
    # print(char)
    # char = my_string[-2] # lấy ký tự kế cuối là chũ l
    # print(char)
'''
String is immutable --> cannot be changed (kiểu dl k thể thay thế)
'''
# Ex:
# my_string[0] = 'M'

'''
Substrings with slicing (tiếp cận 1 đoạn của chuỗi)
'''
# stringName[startIndex:endIndex]
# Start at index 1 and go until index 5 (not include #5) nghĩa là k bao gồm ký tự cuối cùng
# Ex
my_string = 'Hello_world'
# sub_string = my_string[1:5] # lấy ra chuổi "ello"
# print(sub_string)
# sub_string = my_string[:5] # lấy từ vị trí bắt đầu 'H' đến vị trí thứ 5 'o'
# print(sub_string)
# sub_string = my_string[6:] # lấy chuỗi ký tự từ W đến end index là 'world' 
# print(sub_string)

'''
Reverse the string (Đảo ngược lại chuỗi) 
''' 
# sub_string = my_string[::-1] # đang là "hello world" --> "dlrow olleH"
# print(sub_string)

'''
lấy 1 chuỗi theo cách cứ n ký tự thì nó sẽ lấy 1 chuỗi như sau
''' 
# my_string = 'Hello_world'
# sub_string = my_string[::3] # n=3 cứ cách n-1 = 2 ký tự thì lấy 1 ký tự của chuỗi "Hello_world"
# print(sub_string)
# sub_string = my_string[::4] # n=4 cứ cách n-1 = 3 ký tự thì lấy 1 ký tự của chuỗi "Hello_world"
# print(sub_string)
# sub_string = my_string[::5] # n=5 cứ cách n-1 = 4 ký tự thì lấy 1 ký tự của chuỗi "Hello_world"
# print(sub_string)

'''
Concatenate two or more strings 
(kết nối 2 hay nhiều chuỗi lại vs nhau)

concat string with + (kết nối 2 chuỗi)

'''
# greeting = "Hello, xin chao cac ban "
# channel = "from ThanhNam"

# setence = greeting + channel
# print(setence)


'''
 join elements of list into a string: .join() 
 nối các chuỗi trong 1 mảng lại với nhau
'''
# my_list = ['keep', 'calm', 'and', 'follow', 'the', 'rule']
# sentence = ' '.join(my_list)  # nối nhau bằng dấu " space "
# print(sentence)
# sentence = ' _ '.join(my_list) # nối nhau bằng dấu " _ "
# print(sentence)
# sentence = ' : '.join(my_list) # nối nhau bằng dấu " : "
# print(sentence)

'''
Interating (Tiếp cẫn từng ký tự một trong chuỗi)
lấy (in) từng ký tự một ra màn hình
'''
# Interating over a string by using a for in loop

# my_string = "Mot ngay vui ve"
# for char in my_string: 
#    print(char)

'''
check ký tự xem có trong chuỗi không
'''
# if "X" or "M" in my_string: 
#     print('yes')
# else:
#     print('no')


'''
.strip() hàm xóa đi những khoảng trống ở hai đầu của chuỗi
ví dụ chuỗi "   I am 21 years old   " đang có khoảng trống ở hai đầu
'''

# print("   I am 21 years old   ".strip())

# nếu cả đầu cà cuối cùng có 1 ký tự số 1 mà muốn bỏ đi thì
# print("1I really like you".strip('1')) 

'''
.split() hàm tách 1 chuỗi gồm nhiều ký tự thành 1 mảng
'''
# Ex:
# print("keep calm and follow the rule".split())

# tách 1 cụm từ theo ký tự. Ví dụ ở đây là tách theo dấu phẩy
# print("keep calm, and follow, the rule".split(",")) 

'''
Basic & Useful function 
'''
#1 Hàm replace() ví dụ thay help me --> help you là replace("me","you")
# print("help me".replace("me","you"))


#2 Hàm kiểm tra điểm đầu và điểm cuối dùng hàm startwwith() và endwith()
#Ex1:
# my_string = "Need to make a fire"
# print(my_string.startswith("Need"))
# print(my_string.endswith("Need"))


#Ex2: Dùng hàm index() tìm vị trí của ký tự trong chuỗi ví dụ kiểm tra vị trí chữ "m"
# my_string = "Need to make a fire"
# print(my_string.index("m"))


#Ex3: Dùng hàm find() tìm vị trí ký tự trong chuỗi ví dụ cũng tìm chữ "m"
# my_string = "Need to make a fire"
# print(my_string.find("m"))


#Ex4: Dùng hàm upper() chuyển đổi ký tự từ chũ thường thành chữ hoa
# my_string = "nguyen thanh nam"
# print(my_string.upper())


#Ex4: Dùng hàm lower() chuyển đổi ký tự từ chũ hoa thành chữ thường
# my_string = "NGUYEN THANH NAM"
# print(my_string.lower())


#Ex5: Dùng hàm title() để in hoa những chữ cái đầu của 1 từ 
# my_string = "nguyen thanh nam"
# print(my_string.title())


#Ex6: Dùng hàm capitalize() để in hoa ký tự đầu và chuyển hết về chữ thường các ký tự còn lại của 1 chuỗi 
# my_string = "nguyen THANH NAM"
# print(my_string.capitalize())
# my_string = "NGUYEN THANH NAM"
# print(my_string.capitalize())



#Ex7: Dùng hàm count() đếm lần lặp hay số lượng của 1 ký tự trong chuỗi ví dụ đếm xem bn chữ "e"

print("keep calm and follow the rule".count("e")) 
# Đếm chữ "A"
my_string = "NGUYEN THANH NAM"
print(my_string.count("A"))



'''
đang xem ở  
https://www.youtube.com/watch?v=H68p4-lCXVM&list=PLJcWUrckOCKK7tXpLTJJsl1MD98bQHHOg&index=6
phút 28

'''



