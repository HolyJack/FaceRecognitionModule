from api import *
from matplotlib import pyplot

img = pyplot.imread("./data-samples/dzh.jpg")
img2 =  pyplot.imread("./data-samples/jackwhite.jpg")
img3 =  pyplot.imread("./data-samples/jackwhite2.jpg")
img4 =  pyplot.imread("./data-samples/Jack_White_Ottawa.jpg")
img5 = pyplot.imread("./data-samples/dzhigurda.jpg")
img6 = pyplot.imread("./data-samples/potter.jpg")
img7 = pyplot.imread("./data-samples/potter3.jpg")
img8 = pyplot.imread("./data-samples/potter1.jpg")
img9 = pyplot.imread("./data-samples/dzhigurda2.jpg")
img10 = pyplot.imread("./data-samples/dzhigurda3.jpg")
img11 =  pyplot.imread("./data-samples/Jack-White.jpg")
img12 = pyplot.imread("./data-samples/potter4.jpg")
class1_image = pyplot.imread("./data-samples/dzhigurda1.jpg")
class2_image = pyplot.imread("./data-samples/potter2.jpg")
class3_image = pyplot.imread("./data-samples/jackwhite3.jpg")

login1 = 'gjiga'
login2 = 'potter'
login3 = 'jackwhite'


register_user(login1, img)
update_user_info(login1, class1_image)
register_user(login2, class2_image)
register_user(login3, class3_image)

print("________")
print("djiga:", detect_user(img))
print("djiga:", detect_user(img5))
print("djiga:", detect_user(img9))
print("djiga:", detect_user(img10))
print("jack:", detect_user(img2))
print("jack:", detect_user(img3))
print("jack:", detect_user(img4))
print("jack:", detect_user(img11))
print("potter:", detect_user(img6))
print("potter:", detect_user(img7))
print("potter:", detect_user(img8))
print("potter:", detect_user(img12))
print("________")
print(detect_user(class1_image))
print(detect_user(class2_image))
print(detect_user(class3_image))
print("________")

print(compare_users(class1_image, img))
print(compare_users(class1_image, class2_image))
print("________")
print(database_stats())
delete_user_data(login1)
print(database_stats())
database_clear()
print(database_stats())