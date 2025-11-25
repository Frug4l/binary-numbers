import re

class BinaryMultipleOfThree:
    def create_regex(self):
        return r'\b[01]+\b'
    
    def is_multiple_of_three(self, binary_str):
        decimal_value = int(binary_str, 2)
        return decimal_value % 3 == 0
    
    def find_binary_numbers(self, text):
        pattern = self.create_regex()
        return re.findall(pattern, text)
