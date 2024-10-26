import datetime
time = datetime.datetime.now()

class Order:
    def __init__(self, id, name, details):
        self.id = id
        self.name = name
        self.details = details

    def display(self):
        print(f"Order ID: {self.id}")
        print(f"Nama: {self.name}")
        print(f"Detail: {self.details}")

class Delivery:
    def __init__(self, id, name, information, date, address):
        self.id = id
        self.name = name
        self.information = information
        self.date = date
        self.address = address

    def display(self):
        print(f"Delivery ID: {self.id}")
        print(f"Nama: {self.name}")
        print(f"Informasi: {self.information}")
        print(f"Tanggal: {self.date}")
        print(f"Alamat: {self.address}")

orders = []
deliveries = []

while True:
    print("===============ORDER DELIVERY================")
    print("1. Order")
    print("2. Delivery")
    print("0. Keluar")
    menu = int(input("Masukkan yang anda pilih: "))
    
    if menu == 1:
        while True:
            print("===============ORDER================")
            print("1. Tambah Order")
            print("2. Lihat Orders")
            print("0. Keluar")
            men = int(input("Masukkan yang anda pilih: "))
            
            if men == 1:
                id = int(input("Masukkan ID: "))
                nama = input("Masukkan nama: ")
                detail = input("Masukkan detail: ")
                
                # Periksa jika ID sudah ada
                if any(order.id == id for order in orders):
                    print(f"ID '{id}' sudah ada.")
                else:
                    order = Order(id, nama, detail)
                    orders.append(order)
                    print("Order telah ditambah.")
            
            elif men == 2:
                if orders:
                    for order in orders:
                        order.display()
                        print("-------------")
                else:
                    print("Tidak ada order yang tersedia.")
            
            elif men == 0:
                break
            else:
                print("Inputan yang anda pilih tidak ada.")
    
    elif menu == 2:
        while True:
            print("===============DELIVERY================")
            print("1. Tambah Delivery")
            print("2. Lihat Deliveries")
            print("0. Keluar")
            men = int(input("Masukkan yang anda pilih: "))
            
            if men == 1:
                id = int(input("Masukkan ID: "))
                nama = input("Masukkan nama: ")
                informasi = input("Masukkan informasi: ")
                waktu = time.strftime("%Y/%m/%d %H:%M:%S")
                alamat = input("Masukkan alamat: ")
                
                # Periksa jika ID sudah ada
                if any(delivery.id == id for delivery in deliveries):
                    print(f"ID '{id}' sudah ada.")
                else:
                    delivery = Delivery(id, nama, informasi, waktu, alamat)
                    deliveries.append(delivery)
                    print("Delivery telah ditambah.")
            
            elif men == 2:
                if deliveries:
                    for delivery in deliveries:
                        delivery.display()
                        print("-------------")
                else:
                    print("Tidak ada delivery yang tersedia.")
            
            elif men == 0:
                break
            else:
                print("Inputan yang anda pilih tidak ada.")
    
    elif menu == 0:
        print("Program keluar")
        break
    else:
        print("Inputan tidak ada.")
