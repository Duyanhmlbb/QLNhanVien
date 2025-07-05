import json
# Định nghĩa lớp NhanVien để lưu trữ thông tin của từng nhân viên
class NhanVien:
    def __init__(self, ma, ten, phong_ban, luong):
        # Khởi tạo thuộc tính cho nhân viên
        self.ma = ma
        self.ten = ten
        self.phong_ban = phong_ban
        self.luong = luong
    # Chuyển đổi thông tin nhân viên sang dạng từ điển (để lưu file JSON)
    def to_dict(self):
        return {
            "ma": self.ma,
            "ten": self.ten,
            "phong_ban": self.phong_ban,
            "luong": self.luong
        }
    # Phương thức tĩnh: Chuyển từ dữ liệu file JSON thành đối tượng NhanVien
    @staticmethod
    def from_dict(data):
        return NhanVien(data["ma"], data["ten"], data["phong_ban"], data["luong"])
# Định nghĩa lớp QuanLyNhanVien để quản lý danh sách nhân viên và các chức năng liên quan
class QuanLyNhanVien:
    def __init__(self):
        # Khởi tạo danh sách nhân viên rỗng
        self.ds = []
    # Chức năng 1: Khởi tạo danh sách nhân viên (xóa toàn bộ danh sách cũ)
    def khoi_tao(self):
        self.ds = []
        print("Danh sách đã được khởi tạo.")
    # Chức năng 2: Kiểm tra danh sách có rỗng hay không
    def danh_sach_rong(self):
        return len(self.ds) == 0
    # Kiểm tra mã nhân viên có bị trùng không
    def kiem_tra_trung_ma(self, ma):
        return any(nv.ma == ma for nv in self.ds)
    # Kiểm tra toàn bộ thông tin nhân viên có bị trùng không
    def kiem_tra_trung_nv(self, nv_moi):
        return any(nv.ma == nv_moi.ma and nv.ten == nv_moi.ten and nv.phong_ban == nv_moi.phong_ban and nv.luong == nv_moi.luong for nv in self.ds)
    # Chức năng 3: Thêm nhân viên vào đầu danh sách
    def them_dau(self, nv):
        if self.kiem_tra_trung_nv(nv):
            print("Nhân viên này đã tồn tại trong danh sách. Không thể thêm.")
            return
        self.ds.insert(0, nv)
        print("Đã thêm nhân viên vào đầu danh sách.")
    # Chức năng 4: Thêm nhân viên vào cuối danh sách
    def them_cuoi(self, nv):
        if self.kiem_tra_trung_nv(nv):
            print("Nhân viên này đã tồn tại trong danh sách. Không thể thêm.")
            return
        self.ds.append(nv)
        print("Đã thêm nhân viên vào cuối danh sách.")
    # Chức năng 5: Hiển thị danh sách nhân viên
    def hien_thi(self):
        if not self.ds:
            print("Danh sách nhân viên trống.")
        else:
            print("\nDANH SÁCH NHÂN VIÊN:")
            for nv in self.ds:
                print(f"Mã: {nv.ma} | Tên: {nv.ten} | Phòng ban: {nv.phong_ban} | Lương: {nv.luong} VND")
    # Chức năng 6: Tìm nhân viên theo mã
    def tim_theo_ma(self, ma):
        return next((nv for nv in self.ds if nv.ma == ma), None)
    # Chức năng 7: Tìm nhân viên theo tên
    def tim_theo_ten(self, ten):
        return [nv for nv in self.ds if ten.lower() in nv.ten.lower()]
    # Chức năng 8: Tìm nhân viên theo phòng ban
    def tim_theo_phong_ban(self, pb):
        return [nv for nv in self.ds if pb.lower() in nv.phong_ban.lower()]
    # Chức năng 9: Cập nhật thông tin nhân viên theo mã
    def cap_nhat(self, ma):
        nv = self.tim_theo_ma(ma)
        if nv:
            print(f"Thông tin hiện tại: Tên: {nv.ten} | Phòng ban: {nv.phong_ban} | Lương: {nv.luong} VND")
            nv.ten = nhap_ten()
            nv.phong_ban = nhap_phong_ban()
            nv.luong = nhap_luong()
            print("Đã cập nhật thông tin nhân viên.")
        else:
            print("Không tìm thấy nhân viên với mã đã nhập.")
    # Chức năng 10: Xóa nhân viên theo mã
    def xoa_theo_ma(self, ma):
        truoc = len(self.ds)
        self.ds = [nv for nv in self.ds if nv.ma != ma]
        if len(self.ds) < truoc:
            print("Đã xóa nhân viên.")
        else:
            print("Không tìm thấy mã cần xóa.")
    # Chức năng 11: Sắp xếp danh sách theo tên nhân viên
    def sap_xep_ten(self):
        self.ds.sort(key=lambda nv: nv.ten.lower())
        print("Đã sắp xếp theo tên.")
    # Chức năng 12: Sắp xếp danh sách theo lương giảm dần
    def sap_xep_luong(self):
        self.ds.sort(key=lambda nv: nv.luong, reverse=True)
        print("Đã sắp xếp theo lương giảm dần.")
    # Chức năng 13: Đếm số lượng nhân viên
    def dem_nhan_vien(self):
        return len(self.ds)
    # Chức năng 14: Tính tổng lương của tất cả nhân viên
    def tong_luong(self):
        return sum(nv.luong for nv in self.ds)
    # Chức năng 15: Tìm nhân viên có lương cao nhất
    def nhan_vien_luong_max(self):
        return max(self.ds, key=lambda nv: nv.luong, default=None)
    # Chức năng 16: Tìm nhân viên có lương thấp nhất
    def nhan_vien_luong_min(self):
        return min(self.ds, key=lambda nv: nv.luong, default=None)
    # Chức năng 17: Thống kê số lượng nhân viên theo phòng ban
    def thong_ke_phong_ban(self):
        thong_ke = {}
        for nv in self.ds:
            thong_ke[nv.phong_ban] = thong_ke.get(nv.phong_ban, 0) + 1
        for pb, so_nv in thong_ke.items():
            print(f"Phòng ban: {pb} có {so_nv} nhân viên.")
    # Chức năng 18: Ghi danh sách nhân viên ra file
    def ghi_file(self, ten_file):
        with open(ten_file, "w", encoding="utf-8") as f:
            json.dump([nv.to_dict() for nv in self.ds], f, ensure_ascii=False, indent=2)
        print(f"Đã ghi danh sách vào file {ten_file}.")
    # Chức năng 19: Đọc danh sách nhân viên từ file
    def doc_file(self, ten_file):
        try:
            with open(ten_file, "r", encoding="utf-8") as f:
                data = json.load(f)
                self.ds = [NhanVien.from_dict(nv) for nv in data]
            print(f"Đã đọc danh sách từ file {ten_file}.")
        except FileNotFoundError:
            print("File không tồn tại.")
        except:
            print("Lỗi khi đọc file.")
    # Chức năng 20: Sao lưu dữ liệu từ file nguồn sang file đích
    def sao_luu_du_lieu(self, file_nguon, file_dich):
        try:
            with open(file_nguon, 'r', encoding='utf-8') as f1:
                data = json.load(f1)
            with open(file_dich, 'w', encoding='utf-8') as f2:
                json.dump(data, f2, ensure_ascii=False, indent=2)
            print(f"Đã sao lưu dữ liệu từ {file_nguon} sang {file_dich}.")
        except:
            print("Lỗi khi sao lưu dữ liệu.")
# Các hàm hỗ trợ nhập dữ liệu nhân viên
# Hàm nhập mã nhân viên, kiểm tra không trùng và chỉ nhập số
def nhap_ma(ds):
    while True:
        ma = input("Nhập mã nhân viên: ")
        if ma.isdigit():
            if any(nv.ma == ma for nv in ds):
                print("Mã này đã tồn tại. Vui lòng nhập lại.")
            else:
                return ma
        else:
            print("Vui lòng nhập lại (chỉ số).")
# Hàm nhập tên nhân viên, chỉ cho phép nhập chữ
def nhap_ten():
    while True:
        ten = input("Nhập tên nhân viên: ")
        if ten.replace(" ", "").isalpha():
            return ten
        else:
            print("Vui lòng nhập lại (chỉ chữ).")
# Hàm nhập phòng ban
def nhap_phong_ban():
    return input("Nhập phòng ban: ")
# Hàm nhập lương nhân viên
def nhap_luong():
    while True:
        try:
            luong = float(input("Nhập lương: "))
            return luong
        except:
            print("Vui lòng nhập lại (chỉ số).")
# Hàm nhập nhân viên
def nhap_nhan_vien(ds):
    ma = nhap_ma(ds)
    ten = nhap_ten()
    phong_ban = nhap_phong_ban()
    luong = nhap_luong()
    return NhanVien(ma, ten, phong_ban, luong)
# Hàm chuẩn hóa tên file
def dinh_dang_file(ten_file):
    ten_file = ten_file.strip()
    if not ten_file.endswith(".json"):
        ten_file += ".json"
    return ten_file
# Hàm main - menu lựa chọn chức năng
def menu():
    ql = QuanLyNhanVien()
    while True:
        print("\n--- QUẢN LÝ NHÂN VIÊN ---")
        # Hiển thị menu lựa chọn
        print("1. Khởi tạo danh sách")
        print("2. Kiểm tra danh sách có rỗng không")
        print("3. Thêm nhân viên vào đầu danh sách")
        print("4. Thêm nhân viên vào cuối danh sách")
        print("5. Hiển thị danh sách nhân viên")
        print("6. Tìm kiếm nhân viên theo mã")
        print("7. Tìm kiếm nhân viên theo tên")
        print("8. Tìm kiếm nhân viên theo phòng ban")
        print("9. Cập nhật thông tin nhân viên theo mã")
        print("10. Xóa nhân viên theo mã")
        print("11. Sắp xếp danh sách theo tên")
        print("12. Sắp xếp danh sách theo lương giảm dần")
        print("13. Đếm số lượng nhân viên")
        print("14. Tính tổng lương")
        print("15. Tìm nhân viên có lương cao nhất")
        print("16. Tìm nhân viên có lương thấp nhất")
        print("17. Thống kê số lượng nhân viên theo phòng ban")
        print("18. Ghi danh sách ra file")
        print("19. Đọc danh sách từ file")
        print("20. Sao lưu dữ liệu giữa hai file")
        print("0. Thoát chương trình")
        # Lựa chọn chức năng
        chon = input("Chọn chức năng: ")
        if chon == '1':
            ql.khoi_tao()
        elif chon == '2':
            print("Danh sách rỗng." if ql.danh_sach_rong() else "Danh sách có dữ liệu.")
        elif chon == '3':
            ql.them_dau(nhap_nhan_vien(ql.ds))
        elif chon == '4':
            ql.them_cuoi(nhap_nhan_vien(ql.ds))
        elif chon == '5':
            ql.hien_thi()
        elif chon == '6':
            ma = input("Nhập mã nhân viên: ")
            nv = ql.tim_theo_ma(ma)
            if nv:
                print(f"Mã: {nv.ma} | Tên: {nv.ten} | Phòng ban: {nv.phong_ban} | Lương: {nv.luong} VND")
            else:
                print("Không tìm thấy.")
        elif chon == '7':
            kq = ql.tim_theo_ten(nhap_ten())
            if kq:
                for nv in kq:
                    print(f"Mã: {nv.ma} | Tên: {nv.ten} | Phòng ban: {nv.phong_ban} | Lương: {nv.luong} VND")
            else:
                print("Không tìm thấy.")
        elif chon == '8':
            kq = ql.tim_theo_phong_ban(nhap_phong_ban())
            if kq:
                for nv in kq:
                    print(f"Mã: {nv.ma} | Tên: {nv.ten} | Phòng ban: {nv.phong_ban} | Lương: {nv.luong} VND")
            else:
                print("Không tìm thấy.")
        elif chon == '9':
            ql.cap_nhat(input("Nhập mã nhân viên: "))
        elif chon == '10':
            ql.xoa_theo_ma(input("Nhập mã nhân viên: "))
        elif chon == '11':
            ql.sap_xep_ten()
        elif chon == '12':
            ql.sap_xep_luong()
        elif chon == '13':
            print(f"Tổng số nhân viên: {ql.dem_nhan_vien()}")
        elif chon == '14':
            print(f"Tổng lương: {ql.tong_luong():,.2f} VND")
        elif chon == '15':
            nv = ql.nhan_vien_luong_max()
            if nv:
                print(f"Lương cao nhất: {nv.ten} - {nv.luong} VND")
            else:
                print("Không có dữ liệu.")
        elif chon == '16':
            nv = ql.nhan_vien_luong_min()
            if nv:
                print(f"Lương thấp nhất: {nv.ten} - {nv.luong} VND")
            else:
                print("Không có dữ liệu.")
        elif chon == '17':
            ql.thong_ke_phong_ban()
        elif chon == '18':
            ql.ghi_file(dinh_dang_file(input("Nhập tên file: ")))
        elif chon == '19':
            ql.doc_file(dinh_dang_file(input("Nhập tên file: ")))
        elif chon == '20':
            file_nguon = dinh_dang_file(input("Nhập file nguồn: "))
            file_dich = dinh_dang_file(input("Nhập file đích: "))
            ql.sao_luu_du_lieu(file_nguon, file_dich)
        elif chon == '0':
            print("Cảm ơn bạn đã sử dụng chương trình.")
            break
        else:
            print("Lựa chọn không hợp lệ.")
# Chạy chương trình
if __name__ == "__main__":
    menu()