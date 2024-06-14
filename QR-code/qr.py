import qrcode
import image


#qr objesi oluşturma
qr = qrcode.QRCode(version = 15, box_size = 5, border = 5)

#data 
data = "Can Öztel"

#data ekleme
qr.add_data(data)

#oluştur
qr.make(fit=True)

#image oluşturma 
img= qr.make_image(fill="black", back_color= "white")

# image kaydetme 
img.save("qr.png")
