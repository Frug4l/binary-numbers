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
        print("Все числа: " + str(all_binary))
        print("Кратные 3: " + str(multiples))
        return multiples
    
    def analyze_file(self, filename):
        try:
            with open(filename, 'r') as file:
                content = file.read()
            print("Файл загружен: " + filename)
            return self.analyze_text(content)
        except:
            print("Ошибка: файл не найден")
            return None

print("1 - ввести текст")
print("2 - загрузить файл")
choice = input("Выбор: ")

validator = BinaryMultipleOfThree()
if choice == "1":
    text = input("Введите текст: ")
    result = validator.analyze_text(text)
elif choice == "2":
    filename = input("Введите имя файла: ")
    result = validator.analyze_file(filename)
else:
    print("Неверный выбор")
