def XOR(word, code):
    bin_word = word.split()
    after_XOR = []
    for symbol in bin_word:
        stroka = ''
        stroka += str(int(symbol[0]) or int(code[0]))
        stroka += str(int(symbol[1]) or int(code[1]))
        stroka += str(int(symbol[2]) or int(code[2]))
        stroka += str(int(symbol[3]) or int(code[3]))
        stroka += str(int(symbol[4]) or int(code[4]))
        stroka += str(int(symbol[5]) or int(code[5]))
        stroka += str(int(symbol[6]) or int(code[6]))
        stroka += str(int(symbol[7]) or int(code[7]))
        after_XOR.append(stroka)
    return after_XOR



def AND(word, code):
    bin_word = word.split()
    after_AND = []
    for symbol in bin_word:
        stroka = ''
        stroka += str(int(symbol[0]) and int(code[0]))
        stroka += str(int(symbol[1]) and int(code[1]))
        stroka += str(int(symbol[2]) and int(code[2]))
        stroka += str(int(symbol[3]) and int(code[3]))
        stroka += str(int(symbol[4]) and int(code[4]))
        stroka += str(int(symbol[5]) and int(code[5]))
        stroka += str(int(symbol[6]) and int(code[6]))
        stroka += str(int(symbol[7]) and int(code[7]))
        after_AND.append(stroka)
    return after_AND



def shifrator(text, code, funct):
    binary_text = ' '.join(format(ord(char), '08b') for char in text)
    binary_code = ' '.join(format(ord(char), '08b') for char in str(code))
    temp = binary_text.split()
    after_shifr = []

    if funct == 1:
        after_shifr = XOR(binary_text, binary_code)
    elif funct == 2:
        after_shifr = AND(binary_text, binary_code)
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

function_activate = int(input("Введите номер функции активации. OR - 1; AND - 2:"))
while function_activate != 1 and function_activate != 2:
    function_activate = int(input("Выберите от 1 до 2!. OR - 1; AND - 2:"))

print(shifrator(text, code, function_activate))



