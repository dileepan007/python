import barcode
data="karthikesh robotics"
k=barcode.get_barcode_class('code128')
r=k(data)
r.save('barcode')