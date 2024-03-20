from typing import Dict, List, Any, Text
from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher
import sqlite3

class ActionChonLoaiNoiO(Action):
    def name(self) -> Text:
        return "action_chon_loai_noi_o"

    def run(self,
            dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        
        # Kết nối đến cơ sở dữ liệu SQLite
        conn = sqlite3.connect('actions/data_dalat.db')
        cursor = conn.cursor()

        # Truy vấn dữ liệu từ cơ sở dữ liệu
        cursor.execute("SELECT * FROM loai_noi_o")
        loai_noi_o_data = cursor.fetchall()
        # Log số lượng bản ghi
        print(f"Number of records before: {len(loai_noi_o_data)}")
        
        carousel_elements = []
        for loai_noi_o in loai_noi_o_data:
            title, subtitle, image_url = loai_noi_o
            element = {
                "title": title,
                "subtitle": subtitle,
                "image_url": image_url
            }
            carousel_elements.append(element)

        message = {
            "attachment": {
                "type": "template",
                "payload": {
                    "template_type": "generic",
                    "elements": carousel_elements
                }
            }
        }

        dispatcher.utter_message(json_message=message)
                # Đóng kết nối đến cơ sở dữ liệu
        cursor.close()
        conn.close()

        return []
    
class ActionTimDiaDiem(Action):
    def name(self) -> Text:
        return "action_tim_ds_diadiem_dldl"

    def run(self,
            dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        # Kết nối đến cơ sở dữ liệu SQLite
        conn = sqlite3.connect('actions/data_dalat.db')
        cursor = conn.cursor()

        # Truy vấn dữ liệu từ cơ sở dữ liệu
        cursor.execute("SELECT * FROM dia_diem_noi_tieng")
        dia_diem_noi_tieng_data = cursor.fetchall()
        # Log số lượng bản ghi
        print(f"Number of records before: {len(dia_diem_noi_tieng_data)}")

        # Tạo elements cho carousel từ dữ liệu truy vấn
        carousel_elements = []
        for dia_diem_noi_tieng in dia_diem_noi_tieng_data:
            title, subtitle, image_url, url = dia_diem_noi_tieng
            element = {
                "title": title,
                "subtitle": subtitle,
                "image_url": image_url,
                "buttons": [
                    {
                        "title": "Đọc thêm",
                        "type": "web_url",
                        "url": url
                    }
                ]
            }
            carousel_elements.append(element)

        message = {
            "attachment": {
                "type": "template",
                "payload": {
                    "template_type": "generic",
                    "elements": carousel_elements
                }
            }
        }

        dispatcher.utter_message(json_message=message)

        # Đóng kết nối đến cơ sở dữ liệu
        cursor.close()
        conn.close()

        return []

# bảng giá xe taxi nội ô
class ActionGiaThueXeTaxiNoiO(Action):
    def name(self) -> Text:
        return "action_gia_thue_xe_taxi_noi_o"

    def run(self,
            dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        # Kết nối đến cơ sở dữ liệu SQLite
        conn = sqlite3.connect('actions/data_dalat.db')
        cursor = conn.cursor()

        # Truy vấn dữ liệu từ bảng mới
        cursor.execute("SELECT * FROM gia_dv_oto_noi_o")
        gia_dv_oto_noi_o_data = cursor.fetchall()
        print(f"Number of records in gia_dv_oto_noi_o: {len(gia_dv_oto_noi_o_data)}")

        # Tạo elements cho carousel từ dữ liệu truy vấn
        carousel_elements = []
        for gia_dv_oto_noi_o in gia_dv_oto_noi_o_data:
            title, subtitle, image_url, url = gia_dv_oto_noi_o
            element = {
                "title": title,
                "subtitle": subtitle,
                "image_url": image_url,
                "buttons": [
                    {
                        "title": "Đọc thêm",
                        "type": "web_url",
                        "url": url
                    }
                ]
            }
            carousel_elements.append(element)

        message = {
            "attachment": {
                "type": "template",
                "payload": {
                    "template_type": "generic",
                    "elements": carousel_elements
                }
            }
        }

        dispatcher.utter_message(json_message=message)

        # Đóng kết nối đến cơ sở dữ liệu
        cursor.close()
        conn.close()

        return []

# khách sạn
class ActionHotel(Action):
    def name(self) -> Text:
        return "action_khach_san"

    def run(self,
            dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        # Kết nối đến cơ sở dữ liệu SQLite
        conn = sqlite3.connect('actions/data_dalat.db')
        cursor = conn.cursor()

        # Truy vấn dữ liệu từ bảng mới
        cursor.execute("SELECT * FROM hotel")
        hotel_data = cursor.fetchall()
        print(f"Number of records in ks: {len(hotel_data)}")

        # Tạo elements cho carousel từ dữ liệu truy vấn
        carousel_elements = []
        for hotel in hotel_data:
            title, subtitle, image_url, url = hotel
            element = {
                "title": title,
                "subtitle": subtitle,
                "image_url": image_url,
                "buttons": [
                    {
                        "title": "Đặt phòng",
                        "type": "web_url",
                        "url": url
                    }
                ]
            }
            carousel_elements.append(element)

        message = {
            "attachment": {
                "type": "template",
                "payload": {
                    "template_type": "generic",
                    "elements": carousel_elements
                }
            }
        }

        dispatcher.utter_message(json_message=message)

        # Đóng kết nối đến cơ sở dữ liệu
        cursor.close()
        conn.close()

        return []

# homestay
class ActionHomestay(Action):
    def name(self) -> Text:
        return "action_homestay"

    def run(self,
            dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        # Kết nối đến cơ sở dữ liệu SQLite
        conn = sqlite3.connect('actions/data_dalat.db')
        cursor = conn.cursor()

        # Truy vấn dữ liệu từ bảng mới
        cursor.execute("SELECT * FROM homestay")
        homestay_data = cursor.fetchall()
        print(f"Number of records in homestay: {len(homestay_data)}")

        # Tạo elements cho carousel từ dữ liệu truy vấn
        carousel_elements = []
        for homestay in homestay_data:
            title, subtitle, image_url, url = homestay
            element = {
                "title": title,
                "subtitle": subtitle,
                "image_url": image_url,
                "buttons": [
                    {
                        "title": "Đặt phòng",
                        "type": "web_url",
                        "url": url
                    }
                ]
            }
            carousel_elements.append(element)

        message = {
            "attachment": {
                "type": "template",
                "payload": {
                    "template_type": "generic",
                    "elements": carousel_elements
                }
            }
        }

        dispatcher.utter_message(json_message=message)

        # Đóng kết nối đến cơ sở dữ liệu
        cursor.close()
        conn.close()

        return []

# cf view
class ActionCoffee(Action):
    def name(self) -> Text:
        return "action_cf_view"

    def run(self,
            dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        # Kết nối đến cơ sở dữ liệu SQLite
        conn = sqlite3.connect('actions/data_dalat.db')
        cursor = conn.cursor()

        # Truy vấn dữ liệu từ bảng mới
        cursor.execute("SELECT * FROM cf_view")
        cf_view_data = cursor.fetchall()
        print(f"Number of records in ks: {len(cf_view_data)}")

        # Tạo elements cho carousel từ dữ liệu truy vấn
        carousel_elements = []
        for cf_view in cf_view_data:
            title, subtitle, image_url = cf_view
            element = {
                "title": title,
                "subtitle": subtitle,
                "image_url": image_url
            }
            carousel_elements.append(element)
            print(carousel_elements)

        message = {
            "attachment": {
                "type": "template",
                "payload": {
                    "template_type": "generic",
                    "elements": carousel_elements
                }
            }
        }

        dispatcher.utter_message(json_message=message)

        # Đóng kết nối đến cơ sở dữ liệu
        cursor.close()
        conn.close()

        return []

# đồ ăn
class Actiondo_an(Action):
    def name(self) -> Text:
        return "action_tim_do_an_ngon"

    def run(self,
            dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        # Kết nối đến cơ sở dữ liệu SQLite
        conn = sqlite3.connect('actions/data_dalat.db')
        cursor = conn.cursor()

        # Truy vấn dữ liệu từ bảng mới
        cursor.execute("SELECT * FROM do_an")
        do_an_data = cursor.fetchall()
        print(f"Number of records in ks: {len(do_an_data)}")

        # Tạo elements cho carousel từ dữ liệu truy vấn
        carousel_elements = []
        for do_an in do_an_data:
            title, subtitle, image_url = do_an
            element = {
                "title": title,
                "subtitle": subtitle,
                "image_url": image_url
            }
            carousel_elements.append(element)
            print(carousel_elements)

        message = {
            "attachment": {
                "type": "template",
                "payload": {
                    "template_type": "generic",
                    "elements": carousel_elements
                }
            }
        }

        dispatcher.utter_message(json_message=message)

        # Đóng kết nối đến cơ sở dữ liệu
        cursor.close()
        conn.close()

        return []
    
# quà kỉ niệm
class ActionGift(Action):

    def name(self) -> Text:
        return "action_mua_qua_ki_niem"

    def run(self,
            dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        # Kết nối đến cơ sở dữ liệu SQLite
        conn = sqlite3.connect('actions/data_dalat.db')
        cursor = conn.cursor()

        # Truy vấn dữ liệu từ bảng mới
        cursor.execute("SELECT * FROM gift")
        gift_data = cursor.fetchall()
        print(f"Number of records in ks: {len(gift_data)}")

        # Tạo elements cho carousel từ dữ liệu truy vấn
        carousel_elements = []
        for gift in gift_data:
            title, subtitle, image_url = gift
            element = {
                "title": title,
                "subtitle": subtitle,
                "image_url": image_url
            }
            carousel_elements.append(element)
            print(carousel_elements)

        message = {
            "attachment": {
                "type": "template",
                "payload": {
                    "template_type": "generic",
                    "elements": carousel_elements
                }
            }
        }

        dispatcher.utter_message(json_message=message)

        # Đóng kết nối đến cơ sở dữ liệu
        cursor.close()
        conn.close()

        return []
    
# Đặt vé máy bay
class ActionAirlines(Action):
    def name(self) -> Text:
        return "action_tim_may_bay"

    def run(
        self,
        dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: Dict[Text, Any]
    ) -> List[Dict[Text, Any]]:
        # Kết nối đến cơ sở dữ liệu SQLite
        conn = sqlite3.connect('actions/data_dalat.db')
        cursor = conn.cursor()

        # Truy vấn dữ liệu từ cơ sở dữ liệu
        cursor.execute("SELECT * FROM airlines_data")
        airlines_data = cursor.fetchall()
        # Log số lượng bản ghi
        print(f"Number of records before: {len(airlines_data)}")

        # Tạo elements cho carousel từ dữ liệu truy vấn
        carousel_elements = []
        for airlines in airlines_data:
            title, subtitle, image_url, phone_number, url = airlines
            element = {
                "title": title,
                "subtitle": subtitle,
                "image_url": image_url,
                "buttons": [
                    {
                        "title": f"Gọi {phone_number}",
                        "type": "phone_number",
                        "payload": phone_number
                    },
                    {
                        "title": "Truy cập web",
                        "type": "web_url",
                        "url": url
                    }
                ]
            }
            carousel_elements.append(element)

        message = {
            "attachment": {
                "type": "template",
                "payload": {
                    "template_type": "generic",
                    "elements": carousel_elements
                }
            }
        }

        dispatcher.utter_message(json_message=message)

        # Đóng kết nối đến cơ sở dữ liệu
        cursor.close()
        conn.close()

        return []

# Đặt xe khách
class ActionBus(Action):
    def name(self) -> Text:
        return "action_tim_nha_xe"

    def run(
        self,
        dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: Dict[Text, Any]
    ) -> List[Dict[Text, Any]]:
        # Kết nối đến cơ sở dữ liệu SQLite
        conn = sqlite3.connect('actions/data_dalat.db')
        cursor = conn.cursor()

        # Truy vấn dữ liệu từ cơ sở dữ liệu
        cursor.execute("SELECT * FROM nha_xe")
        nha_xe_data = cursor.fetchall()
        # Log số lượng bản ghi
        print(f"Number of records before: {len(nha_xe_data)}")

        # Tạo elements cho carousel từ dữ liệu truy vấn
        carousel_elements = []
        for nha_xe in nha_xe_data:
            title, subtitle, image_url, phone_number, url = nha_xe
            element = {
                "title": title,
                "subtitle": subtitle,
                "image_url": image_url,
                "buttons": [
                    {
                        "title": f"Gọi {phone_number}",
                        "type": "phone_number",
                        "payload": phone_number
                    },
                    {
                        "title": "Truy cập web",
                        "type": "web_url",
                        "url": url
                    }
                ]
            }
            carousel_elements.append(element)

        message = {
            "attachment": {
                "type": "template",
                "payload": {
                    "template_type": "generic",
                    "elements": carousel_elements
                }
            }
        }

        dispatcher.utter_message(json_message=message)

        # Đóng kết nối đến cơ sở dữ liệu
        cursor.close()
        conn.close()

        return []
    
# Hostel
class ActionHostel(Action):
    def name(self) -> Text:
        return "action_tim_hostel_dalat"

    def run(
        self,
        dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: Dict[Text, Any]
    ) -> List[Dict[Text, Any]]:
        # Kết nối đến cơ sở dữ liệu SQLite
        conn = sqlite3.connect('actions/data_dalat.db')
        cursor = conn.cursor()

        # Truy vấn dữ liệu từ cơ sở dữ liệu
        cursor.execute("SELECT * FROM hostel_dalat")
        hostel_dalat_data = cursor.fetchall()
        # Log số lượng bản ghi
        print(f"Number of records before: {len(hostel_dalat_data)}")

        # Tạo elements cho carousel từ dữ liệu truy vấn
        carousel_elements = []
        for hostel_dalat in hostel_dalat_data:
            title, subtitle, image_url, phone_number, url = hostel_dalat
            element = {
                "title": title,
                "subtitle": subtitle,
                "image_url": image_url,
                "buttons": [
                    {
                        "title": f"Gọi {phone_number}",
                        "type": "phone_number",
                        "payload": phone_number
                    },
                    {
                        "title": "Xem đường đi",
                        "type": "web_url",
                        "url": url
                    }
                ]
            }
            carousel_elements.append(element)

        message = {
            "attachment": {
                "type": "template",
                "payload": {
                    "template_type": "generic",
                    "elements": carousel_elements
                }
            }
        }

        dispatcher.utter_message(json_message=message)

        # Đóng kết nối đến cơ sở dữ liệu
        cursor.close()
        conn.close()

        return []

# nhà nghỉ
class ActionNhaNghi(Action):
    def name(self) -> Text:
        return "action_tim_nha_nghi_dalat"

    def run(
        self,
        dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: Dict[Text, Any]
    ) -> List[Dict[Text, Any]]:
        # Kết nối đến cơ sở dữ liệu SQLite
        conn = sqlite3.connect('actions/data_dalat.db')
        cursor = conn.cursor()

        # Truy vấn dữ liệu từ cơ sở dữ liệu
        cursor.execute("SELECT * FROM nha_nghi_dalat")
        nha_nghi_dalat_data = cursor.fetchall()
        # Log số lượng bản ghi
        print(f"Number of records before: {len(nha_nghi_dalat_data)}")

        # Tạo elements cho carousel từ dữ liệu truy vấn
        carousel_elements = []
        for nha_nghi_dalat in nha_nghi_dalat_data:
            title, subtitle, image_url, phone_number, url = nha_nghi_dalat
            element = {
                "title": title,
                "subtitle": subtitle,
                "image_url": image_url,
                "buttons": [
                    {
                        "title": f"Gọi {phone_number}",
                        "type": "phone_number",
                        "payload": phone_number
                    },
                    {
                        "title": "Đặt web",
                        "type": "web_url",
                        "url": url
                    }
                ]
            }
            carousel_elements.append(element)

        message = {
            "attachment": {
                "type": "template",
                "payload": {
                    "template_type": "generic",
                    "elements": carousel_elements
                }
            }
        }

        dispatcher.utter_message(json_message=message)

        # Đóng kết nối đến cơ sở dữ liệu
        cursor.close()
        conn.close()

        return []
    