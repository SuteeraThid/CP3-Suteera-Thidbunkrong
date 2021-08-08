name = input("enter your name: ")
password = input("enter your password: ")

if name == "Sutee" and password == "1912":
    print("-------------------------- สวัสดีค่ะ คุณ", name, "---------------------------")
    print("PALI Shop มีสินค้า Collection Spring สุดพิเศษให้คุณเลือกตามรายการข้างล่างนี้เลยค่ะ")
    print("********โดยคุณ", name, "สามารถเลือกสินค้าได้เพียง 1 ชนิดเท่านั้น แต่สามารถเลือกจำนวนเท่าไหร่ก็ได้")
    print()
    print("1. Shirt Dress     ")
    print("2. Wide Leg Pants  ")
    print("3. Wide Shot Pants ")
    print("4. Crop Blouse     ")
    print()
    numberProduct = int(input("โปรดใส่เบอร์สินค้าที่คุณต้องการ >> "))
    if numberProduct == 1:
        shirtDress = 470
        numberProducts = int(input("โปรดใส่จำนวนสินค้าที่คุณต้องการ >> "))
        print("ยอดรวมของคุณคือ ", shirtDress*numberProducts, "฿")
    elif numberProduct == 2:
        wideLegPants = 70
        numberProducts = int(input("โปรดใส่จำนวนสินค้าที่คุณต้องการ >> "))
        print("ยอดรวมของคุณคือ ", wideLegPants*numberProducts, "฿")
    elif numberProduct == 3:
        wideShotPants = 520
        numberProducts = int(input("โปรดใส่จำนวนสินค้าที่คุณต้องการ >> "))
        print("ยอดรวมของคุณคือ ", wideShotPants*numberProducts, "฿")
    elif numberProduct == 4:
        cropBlouse = 220
        numberProducts = int(input("โปรดใส่จำนวนสินค้าที่คุณต้องการ >> "))
        print("ยอดรวมของคุณคือ ", cropBlouse*numberProducts, "฿")
else:
    print("Collection Spring ของ PALI Shop สำหรับผู้เป็นสมาชิกเท่านั้น")
    print("หากคุณสนใจจะสมัครสมาชิก กรุณาติดต่อได้ที่เคาท์เตอร์ของ PALI Shop ทุกสาขา")
print("---------------------------------------------------------------------")
print("--------------------PALI Shop ขอขอบคุณที่ใช้บริการค่ะ------------------------")
