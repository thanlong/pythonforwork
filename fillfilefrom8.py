import os

# Thư mục chứa các file txt
folder_path = 'path/to/your/folder'  # Thay bằng đường dẫn đến thư mục chứa file .txt

# Duyệt qua từng file trong thư mục
for filename in os.listdir(folder_path):
    if filename.endswith('.txt'):  # Chỉ xử lý file .txt
        file_path = os.path.join(folder_path, filename)
        
        # Đọc nội dung file
        with open(file_path, 'r', encoding='utf-8') as file:
            lines = file.readlines()
        
        # Lọc các dòng có độ dài từ 8 ký tự trở lên
        filtered_lines = [line for line in lines if len(line.strip()) >= 8]
        
        # Ghi lại nội dung đã lọc vào file
        with open(file_path, 'w', encoding='utf-8') as file:
            file.writelines(filtered_lines)

print("Đã xóa các dòng ít hơn 8 ký tự trong tất cả các file .txt.")
