import re
import bogo

class VniEncoder:
    def __init__(self):
        # Bản đồ ký tự VNI
        self.vni_char_map = {
            'á': '1', 'à': '2', 'ả': '3', 'ã': '4', 'ạ': '5',
            'â': '6', 'ấ': '61', 'ầ': '62', 'ẩ': '63', 'ẫ': '64', 'ậ': '65',
            'ă': '8', 'ắ': '81', 'ằ': '82', 'ẳ': '83', 'ẵ': '84', 'ặ': '85',
            'é': '1', 'è': '2', 'ẻ': '3', 'ẽ': '4', 'ẹ': '5',
            'ê': '6', 'ế': '61', 'ề': '62', 'ể': '63', 'ễ': '64', 'ệ': '65',
            'í': '1', 'ì': '2', 'ỉ': '3', 'ĩ': '4', 'ị': '5',
            'ó': '1', 'ò': '2', 'ỏ': '3', 'õ': '4', 'ọ': '5',
            'ô': '6', 'ố': '61', 'ồ': '62', 'ổ': '63', 'ỗ': '64', 'ộ': '65',
            'ơ': '7', 'ớ': '71', 'ờ': '72', 'ở': '73', 'ỡ': '74', 'ợ': '75',
            'ú': '1', 'ù': '2', 'ủ': '3', 'ũ': '4', 'ụ': '5',
            'ư': '7', 'ứ': '71', 'ừ': '72', 'ử': '73', 'ữ': '74', 'ự': '75',
            'ý': '1', 'ỳ': '2', 'ỷ': '3', 'ỹ': '4', 'ỵ': '5',
            'đ': '9',
        }
        # Bản đồ ký tự gốc
        self.base_char_map = {
            'á': 'a', 'à': 'a', 'ả': 'a', 'ã': 'a', 'ạ': 'a',
            'â': 'a', 'ấ': 'a', 'ầ': 'a', 'ẩ': 'a', 'ẫ': 'a', 'ậ': 'a',
            'ă': 'a', 'ắ': 'a', 'ằ': 'a', 'ẳ': 'a', 'ẵ': 'a', 'ặ': 'a',
            'é': 'e', 'è': 'e', 'ẻ': 'e', 'ẽ': 'e', 'ẹ': 'e',
            'ê': 'e', 'ế': 'e', 'ề': 'e', 'ể': 'e', 'ễ': 'e', 'ệ': 'e',
            'í': 'i', 'ì': 'i', 'ỉ': 'i', 'ĩ': 'i', 'ị': 'i',
            'ó': 'o', 'ò': 'o', 'ỏ': 'o', 'õ': 'o', 'ọ': 'o',
            'ô': 'o', 'ố': 'o', 'ồ': 'o', 'ổ': 'o', 'ỗ': 'o', 'ộ': 'o',
            'ơ': 'o', 'ớ': 'o', 'ờ': 'o', 'ở': 'o', 'ỡ': 'o', 'ợ': 'o',
            'ú': 'u', 'ù': 'u', 'ủ': 'u', 'ũ': 'u', 'ụ': 'u',
            'ư': 'u', 'ứ': 'u', 'ừ': 'u', 'ử': 'u', 'ữ': 'u', 'ự': 'u',
            'ý': 'y', 'ỳ': 'y', 'ỷ': 'y', 'ỹ': 'y', 'ỵ': 'y',
            'đ': 'd',
        }
        # Thứ tự ưu tiên các số
        self.priority_order = ['9', '8', '6', '7', '5', '4', '3', '2', '1']

    def _word_to_vni(self, word):
        word = word.lower()
        queue = []
        base_word = ''
        for char in word:
            if char in self.vni_char_map:
                base_char = self.base_char_map[char]
                base_word += base_char
                numbers = self.vni_char_map[char]
                for number in numbers:
                    if number not in queue:
                        queue.append(number)
            else:
                base_word += char
        queue = sorted(queue, key=lambda x: self.priority_order.index(x))
        return base_word + ''.join(queue)

    def encode(self, input_text):
        parts = re.findall(r'\w+|\W+', input_text)
        encoded_parts = []
        for part in parts:
            if re.search(r'\w', part):
                encoded_parts.append(self._word_to_vni(part))
            else:
                encoded_parts.append(part)
        return ''.join(encoded_parts)

    def decode(self, vni_text):
        words = vni_text.split()
        decoded_words = []
        for word in words:
            decoded_word = bogo.process_sequence(word, rules=bogo.get_vni_definition())
            decoded_words.append(decoded_word)
        return ' '.join(decoded_words)