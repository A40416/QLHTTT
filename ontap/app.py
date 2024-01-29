from flask import Flask
from flask_restful import Api
from models import db
import config
from services import NhanVienManager

# Khởi tạo Flask application và Flask-RESTful API manager
app = Flask(__name__)
app.config.from_object(config)
# Khởi tạo đối tượng Flask-SQLALchemy
db.init_app(app)
# Tạo đối tượng Flask-RESTful API manager
api = Api(app)
# Tạo endponints
api.add_resource(NhanVienManager, '/nhanvien')

if __name__ == '__main__':
    # Tạo database tables.
    with app.app_context():
        db.create_all()
    # Start Flask development web server
    app.run(debug=True)