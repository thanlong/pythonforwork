# Đọc file txt
with open('file.txt', 'r', encoding='utf-8') as file:
    lines = file.readlines()

# Lọc các dòng có ít hơn 8 ký tự
filtered_lines = [line for line in lines if len(line.strip()) >= 8]

# Ghi lại vào file mới
with open('file_filtered.txt', 'w', encoding='utf-8') as file:
    file.writelines(filtered_lines)

print("Xóa các dòng có ít hơn 8 ký tự thành công. Kết quả đã lưu trong 'file_filtered.txt'.")
