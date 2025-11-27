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
        print("Найдено двоичных чисел: " + str(len(all_binary)))
        print("Все двоичные числа: " + str(all_binary))
        print("Кратные 3: " + str(multiples))
        
        if multiples:
            print("\nДетальная проверка:")
            for num in multiples:
                decimal = int(num, 2)
                print(num + " (двоичное) = " + str(decimal) + " (десятичное)")
        
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
    
    def process_user_input(self):
        print("=== Поиск двоичных чисел кратных 3 ===")
        print("1 - ввести текст")
        print("2 - загрузить файл")
        
        choice = input("Выбор (1-2): ")
        
        if choice == "1":
            text = input("Введите текст: ")
            return self.analyze_text(text)
        elif choice == "2":
            filename = input("Введите имя файла: ")
            return self.analyze_file(filename)
        else:
            print("Неверный выбор!")
            return None

def main():
    validator = BinaryMultipleOfThree()
    
    while True:
        print("\n" + "="*40)
        print("Главное меню:")
        print("1 - Запустить программу")
        print("2 - Выход")
        
        choice = input("Ваш выбор (1-2): ")
        
        if choice == "1":
            result = validator.process_user_input()
        elif choice == "2":
            print("Выход из программы...")
            break
        else:
            print("Неверный выбор!")

if __name__ == "__main__":
    main()
