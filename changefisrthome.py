# Đọc file txt
with open('file.txt', 'r', encoding='utf-8') as file:
    data = file.read()

# Thay đổi đầu số từ 0120 thành 070
updated_data = data.replace('0120', '070')

# Ghi lại vào file txt
with open('file_updated.txt', 'w', encoding='utf-8') as file:
    file.write(updated_data)

print("Chuyển đổi hoàn tất. Nội dung mới đã được lưu trong 'file_updated.txt'.")
