import unittest
from vniencoder import VniEncoder

class TestVniEncoder(unittest.TestCase):
    def setUp(self):
        self.encoder = VniEncoder()

    # Test cases cho hàm encode
    def test_encode_no_special_chars(self):
        """Kiểm tra encode với chuỗi không có ký tự đặc biệt"""
        self.assertEqual(self.encoder.encode("bí chị cửa"), "bi1 chi5 cua73")

    def test_encode_special_chars_at_end(self):
        """Kiểm tra encode với ký tự đặc biệt ở cuối"""
        self.assertEqual(self.encoder.encode("bí chị cửa!!"), "bi1 chi5 cua73!!")

    def test_encode_special_chars_in_middle(self):
        """Kiểm tra encode với ký tự đặc biệt ở giữa"""
        self.assertEqual(self.encoder.encode("bí, chị cửa"), "bi1, chi5 cua73")

    def test_encode_multiple_special_chars(self):
        """Kiểm tra encode với nhiều ký tự đặc biệt"""
        self.assertEqual(self.encoder.encode("bí!!! chị... cửa???"), "bi1!!! chi5... cua73???")

    def test_encode_numbers(self):
        """Kiểm tra encode với số trong chuỗi"""
        self.assertEqual(self.encoder.encode("bí 123 chị 456 cửa"), "bi1 123 chi5 456 cua73")

    def test_encode_non_vietnamese(self):
        """Kiểm tra encode với chuỗi không phải tiếng Việt"""
        self.assertEqual(self.encoder.encode("hello world"), "hello world")

    def test_encode_mixed_vietnamese_non_vietnamese(self):
        """Kiểm tra encode với chuỗi pha trộn tiếng Việt và không tiếng Việt"""
        self.assertEqual(self.encoder.encode("hello bí chị"), "hello bi1 chi5")

    def test_encode_tone_and_no_tone(self):
        """Kiểm tra encode với từ có dấu và không dấu"""
        self.assertEqual(self.encoder.encode("bí bi"), "bi1 bi")

    def test_encode_multiple_tones(self):
        """Kiểm tra encode với nhiều dấu trong cùng một từ"""
        self.assertEqual(self.encoder.encode("cửa quả"), "cua73 qua3")

    def test_encode_special_char_with_word(self):
        """Kiểm tra encode với từ có ký tự đặc biệt liền kề"""
        self.assertEqual(self.encoder.encode("đi!!"), "di9!!")

    # Test cases cho hàm decode
    def test_decode_basic(self):
        """Kiểm tra decode với chuỗi VNI cơ bản"""
        self.assertEqual(self.encoder.decode("bi1 chi5 cua73"), "bí chị cửa")

    def test_decode_with_special_chars(self):
        """Kiểm tra decode với chuỗi VNI có ký tự đặc biệt"""
        self.assertEqual(self.encoder.decode("bi1 chi5 cua73!!"), "bí chị cửa!!")

    def test_decode_mixed_text(self):
        """Kiểm tra decode với chuỗi VNI pha trộn tiếng Việt và không tiếng Việt"""
        self.assertEqual(self.encoder.decode("hello bi1 chi5"), "hello bí chị")

if __name__ == '__main__':
    unittest.main()