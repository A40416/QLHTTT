from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

# định nghĩa class để mapping với bảng nhanvien trong CSDL
class NhanVien(db.Model):
    ma = db.Column(db.Integer, primary_key=True)
    # khai báo nullable=False để cột bắt buộc phải nhập
    hoten = db.Column(db.String(50), nullable=False)
    tuoi = db.Column(db.Integer)
    diachi = db.Column(db.String(50))

    def __repr__(self):
        # Method này cho phép hiển thị thông tin chi tiết về đối tượng
        return f'Task {self.ma} : {self.hoten} : {self.tuoi} : {self.diachi}'
