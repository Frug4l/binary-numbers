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
    
    def find_multiples_of_three(self, text):
        binary_numbers = self.find_binary_numbers(text)
        return [num for num in binary_numbers if self.is_multiple_of_three(num)]
    
    def analyze_text(self, text):
        all_binary = self.find_binary_numbers(text)
        multiples = self.find_multiples_of_three(text)
        print("Найдено чисел: " + str(len(all_binary)))
        return multiples

validator = BinaryMultipleOfThree()
text = input("Введите текст: ")
result = validator.analyze_text(text)
print("Результат: " + str(result))
