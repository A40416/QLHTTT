from flask_restful import Resource
from flask import request
from models import NhanVien, db


# định nghĩa class cung cấp các method cho phép gọi API từ frontend
class NhanVienManager(Resource):
    def get(self):
        # lấy về tất cả nhanvien từ database
        employess = NhanVien.query.all()
        # Chuyển đổi danh sách nhân viên thành JSON và trả về response
        listemployee = [
            {
                "ma": employee.ma,
                "hoten": employee.hoten,
                "tuoi": employee.tuoi,
                "diachi": employee.diachi,
            }
            for employee in employess
        ]
        return {"listemployee": listemployee}

    def post(self):
        # Lấy JSON data từ request
        response_data = request.get_json()
        # Kiểm tra xem dữ liệu có hợp lệ hay không
        if not response_data:
            return {"message": "No input data provided"}, 400
        hoten = response_data.get("hoten")
        if not hoten:
            return {"message": "Họ tên nhân viên không được bỏ trống!"}, 400
        # Thêm nhân viên mới vào database
        new_employee = NhanVien(
            hoten=response_data.get("hoten"),
            tuoi=response_data.get("tuoi"),
            diachi=response_data.get("diachi"),
        )
        db.session.add(new_employee)
        # Ghi dữ liệu vào database
        db.session.commit()
        # Trả về một message cho người dùng.
        return {
            "message": "Đã thêm nhân viên mới",
            "nhanvien": {
                "ma": new_employee.ma,
                "hoten": new_employee.hoten,
                "tuoi": new_employee.tuoi,
                "diachi": new_employee.diachi,
            },
        }
