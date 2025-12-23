import qrcode

# Step 1: Define the data you want to encode
data = input("Enter a URL or text for your QR code: ").strip()

# Step 2: Generate the QR code
# Version controls the size (1-40); box_size is pixels per square; border is thickness
qr = qrcode.QRCode(version=1, box_size=10, border=4)
qr.add_data(data)
qr.make(fit=True)

# Step 3: Create and save the image

img = qr.make_image(fill_color="Red", back_color="black")
img.save("my_qrcode.png")

print("✅ Success! \n Your QR code is saved as 'my_qrcode.png'.")
