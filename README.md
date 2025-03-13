# VniEncoder

Tác giả: Trịnh Huỳnh Thịnh Khang

Giới thiệu: Thư viện Python này giúp mã hóa và giải mã văn bản tiếng Việt theo phương pháp VNI.

## Cài đặt

```bash
pip install vniencoder
```

## Cách dùng

```python
VniEncoder = VniEncoder()  # Tạo đối tượng

result = VniEncoder.encode("bí chị cửa!!")  # Gọi hàm encode
print(result)  # Kết quả: "bi1 chi5 cua73"

decoded_text = VniEncoder.decode("bi1 chi5 cua73!!")
print(decoded_text)  # Kết quả: "bí chị cửa"
```

## Thông tin liên hệ:

Gmail: trinhhuynhthinhkhang.work@gmail.com

Page Facebook: Nhật ký học tập của Khang 