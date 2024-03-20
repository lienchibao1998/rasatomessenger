import sqlite3

def create_table():
    # Kết nối đến cơ sở dữ liệu SQLite (nếu chưa tồn tại sẽ tự động tạo mới)
    conn = sqlite3.connect('actions/data_dalat.db')
    cursor = conn.cursor()

    # Tạo bảng places nếu chưa tồn tại
    cursor.execute('''CREATE TABLE IF NOT EXISTS places
                    (title TEXT, subtitle TEXT, image_url TEXT, url TEXT)''')

    # Lưu và đóng kết nối đến cơ sở dữ liệu
    conn.commit()
    conn.close()

def insert_data():
    places_data = [
        ("Chợ đêm Đà Lạt", "Khu Vực Ăn Uống Về Đêm...", "https://cdn3.ivivu.com/2023/10/du-l%E1%BB%8Bch-da-lat-ivivu.jpg", "https://vinpearl.com/vi/cho-dem-da-lat"),
        ("Hồ Xuân Hương", "Hồ Hồ Xuân Hương được đánh giá là một trong số các hồ nước đẹp nhất của Việt Nam...", "https://cdn3.ivivu.com/2023/10/du-lich-da-lat-ivivu-3.jpg", "https://vinpearl.com/vi/ho-xuan-huong-da-lat"),
        ("DINH BẢO ĐẠI", "Dinh thự vị vua cuối cùng của Việt Nam...", "https://cdn3.ivivu.com/2023/10/du-l%E1%BB%8Bch-da-lat-ivivu1.jpg", "https://www.traveloka.com/vi-vn/explore/destination/dinh-bao-dai/250796"),
        ("GA ĐÀ LẠT", "Gắn liền với lịch sử hình thành và phát triển đô thị “xứ ngàn thông”. Được coi là nhà ga xe lửa cổ đẹp nhất Việt Nam và Đông Dương...", "https://cdn3.ivivu.com/2023/10/du-lich-da-lat-ivivu4.jpg", "https://vietnamtourism.gov.vn/post/34856")
    ]

    # Kết nối đến cơ sở dữ liệu SQLite
    conn = sqlite3.connect('actions/data_dalat.db')
    cursor = conn.cursor()

    # Thêm dữ liệu vào bảng places
    cursor.executemany("INSERT INTO places VALUES (?, ?, ?, ?)", places_data)

    # Lưu và đóng kết nối đến cơ sở dữ liệu
    conn.commit()
    conn.close()

def print_data():
    # Kết nối đến cơ sở dữ liệu SQLite
    conn = sqlite3.connect('actions/data_dalat.db')
    cursor = conn.cursor()

    # Truy vấn dữ liệu từ bảng places
    cursor.execute("SELECT * FROM places")
    rows = cursor.fetchall()

    # Hiển thị kết quả
    for row in rows:
        print(row)

    # Đóng kết nối đến cơ sở dữ liệu
    cursor.close()
    conn.close()

# Tạo bảng và thêm dữ liệu vào cơ sở dữ liệu
create_table()
insert_data()

# In dữ liệu từ cơ sở dữ liệu
print("Dữ liệu từ cơ sở dữ liệu:")
print_data()
