def XOR(word, code, repeats):
    bin_word = word.split()
    after_XOR = []
    for symbol in bin_word:
        fin_stroka = ''
        
        # Бит 0
        result = int(symbol[0]) ^ int(code[0])
        for _ in range(repeats - 1):  
            result = result ^ int(code[0])
        fin_stroka += str(result)

        # Бит 1
        result = int(symbol[1]) ^ int(code[1])
        for _ in range(repeats - 1):
            result = result ^ int(code[1])
        fin_stroka += str(result)

        # Бит 2
        result = int(symbol[2]) ^ int(code[2])
        for _ in range(repeats - 1):
            result = result ^ int(code[2])
        fin_stroka += str(result)

        # Бит 3
        result = int(symbol[3]) ^ int(code[3])
        for _ in range(repeats - 1):
            result = result ^ int(code[3])
        fin_stroka += str(result)

        # Бит 4
        result = int(symbol[4]) ^ int(code[4])
        for _ in range(repeats - 1):
            result = result ^ int(code[4])
        fin_stroka += str(result)

        # Бит 5
        result = int(symbol[5]) ^ int(code[5])
        for _ in range(repeats - 1):
            result = result ^ int(code[5])
        fin_stroka += str(result)

        # Бит 6
        result = int(symbol[6]) ^ int(code[6])
        for _ in range(repeats - 1):
            result = result ^ int(code[6])
        fin_stroka += str(result)

        # Бит 7
        result = int(symbol[7]) ^ int(code[7])
        for _ in range(repeats - 1):
            result = result ^ int(code[7])
        fin_stroka += str(result)

        after_XOR.append(fin_stroka)

    return after_XOR
        


def AND(word, code, repeats):
    bin_word = word.split()
    after_AND = []
    for symbol in bin_word:
        fin_stroka = ''

        # Бит 0
        result = int(symbol[0]) & int(code[0])
        for _ in range(repeats - 1):
            result = result & int(code[0])
        fin_stroka += str(result)

        # Бит 1
        result = int(symbol[1]) & int(code[1])
        for _ in range(repeats - 1):
            result = result & int(code[1])
        fin_stroka += str(result)

        # Бит 2
        result = int(symbol[2]) & int(code[2])
        for _ in range(repeats - 1):
            result = result & int(code[2])
        fin_stroka += str(result)

        # Бит 3
        result = int(symbol[3]) & int(code[3])
        for _ in range(repeats - 1):
            result = result & int(code[3])
        fin_stroka += str(result)

        # Бит 4
        result = int(symbol[4]) & int(code[4])
        for _ in range(repeats - 1):
            result = result & int(code[4])
        fin_stroka += str(result)

        # Бит 5
        result = int(symbol[5]) & int(code[5])
        for _ in range(repeats - 1):
            result = result & int(code[5])
        fin_stroka += str(result)

        # Бит 6
        result = int(symbol[6]) & int(code[6])
        for _ in range(repeats - 1):
            result = result & int(code[6])
        fin_stroka += str(result)

        # Бит 7
        result = int(symbol[7]) & int(code[7])
        for _ in range(repeats - 1):
            result = result & int(code[7])
        fin_stroka += str(result)

        after_AND.append(fin_stroka)

    return after_AND



def shifrator(text, code, funct, repeats):
    binary_text = ' '.join(format(ord(char), '08b') for char in text)
    binary_code = ' '.join(format(ord(char), '08b') for char in str(code))
    temp = binary_text.split()
    after_shifr = []

    if funct == 1:
        after_shifr = XOR(binary_text, binary_code, repeats)
    elif funct == 2:
        after_shifr = AND(binary_text, binary_code, repeats)
    else:
        return "От 1 до 2"

    after_shifr_str = ''
    for symbol in after_shifr:
        after_shifr_str += symbol + ' '

    return after_shifr_str



text = input("Введите текст для шифровки: ")
code = input("Введите код для шифровки: ")

while len(str(code)) != 1:
    code = input("Кодовое слово должно быть односимвольное! Введите еще раз:")

function_activate = int(input("Введите номер функции активации. and - 1; AND - 2:"))
while function_activate != 1 and function_activate != 2:
    function_activate = int(input("Выберите от 1 до 2!. OR - 1; AND - 2:"))

repeats = int(input("Введите глубину кодировки(1+):"))
while repeats < 0:
    repeats = int(input("Введите глубину кодировки(1+):"))


print(shifrator(text, code, function_activate, repeats))

