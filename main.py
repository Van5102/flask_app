from src import create_app, socketio
from flask import Blueprint, jsonify
from src.models import Project, Task, db

app = create_app()

# import openpyxl
# from openpyxl import Workbook

# # Tạo một workbook mới và active sheet
# wb = Workbook()
# ws = wb.active

# # Đặt tên cho các cột
# columns = ["task_name", "unit", "quantity", "estimate_unit_price", "sale_description", "other_description"]
# ws.append(columns)

# # Tạo dữ liệu mẫu
# data = [
#     ["Task 1", "Unit 1", 10, 100, "Sale Desc 1", "Other Desc 1"],
#     ["Task 2", "Unit 2", 20, 200, "Sale Desc 2", "Other Desc 2"],
#     ["Task 3", "Unit 3", 30, 300, "Sale Desc 3", "Other Desc 3"],
#     ["Task 4", "Unit 4", 40, 400, "Sale Desc 4", "Other Desc 4"],
#     ["Task 5", "Unit 5", 50, 500, "Sale Desc 5", "Other Desc 5"],
#     ["Task 6", "Unit 6", 60, 600, "Sale Desc 6", "Other Desc 6"],
#     ["Task 7", "Unit 7", 70, 700, "Sale Desc 7", "Other Desc 7"],
#     ["Task 8", "Unit 8", 80, 800, "Sale Desc 8", "Other Desc 8"],
#     ["Task 9", "Unit 9", 90, 900, "Sale Desc 9", "Other Desc 9"],
#     ["Task 10", "Unit 10", 100, 1000, "Sale Desc 10", "Other Desc 10"]
# ]

# # Thêm dữ liệu vào sheet
# for row in data:
#     ws.append(row)

# # Lưu workbook vào file
# wb.save("task_data.xlsx")

if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    socketio.run(app, debug=True)
