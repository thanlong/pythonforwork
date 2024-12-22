import os

# Thư mục chứa các file txt
folder_path = 'path/to/your/folder'  # Thay đường dẫn bằng thư mục của bạn
output_file = 'merged.txt'  # Tên file xuất kết quả

# Lấy danh sách file .txt trong thư mục
txt_files = [f for f in os.listdir(folder_path) if f.endswith('.txt')]

# Gộp nội dung các file
with open(output_file, 'w', encoding='utf-8') as outfile:
    for txt_file in txt_files:
        with open(os.path.join(folder_path, txt_file), 'r', encoding='utf-8') as infile:
            outfile.write(infile.read())
            outfile.write('\n')  # Thêm dòng trống giữa các file (tùy chọn)

print(f"Đã gộp {len(txt_files)} file thành công vào '{output_file}'.")
