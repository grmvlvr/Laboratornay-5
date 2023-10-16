def Cezar(text, shift):
    zashifr_text= ""
    for c in text:
# Функция isalpha() в Python возвращает True, если все символы в строке являются алфавитными.Если нет, возвращается False.
        if c.isalpha():
# Функция isupper() в Python проверяет, все ли символы в строке находятся в верхнем регистре.
            start = ord('A') if c.isupper() else ord('a')
            encrypted_c = chr((ord(c) - start + shift) % 26 + start)
            zashifr_text+= encrypted_c
        else:
            zashifr_text+= c
    return zashifr_text

def validate_shift(shift):
# Функция isdigit() в Python: возвращает True, если все символы в строке являются цифрами. Если нет, возвращается False.
    if not shift.isdigit():
        return False
    shift = int(shift)
    return shift >= 1 and shift <= 25

def caesar_decipher(text, shift):
    return Cezar(text, -shift)

def main():
    text = input("Введите текст: ")
    shift = input("Введите шаг сдвига (от 1 до 25): ")
    
    if not validate_shift(shift):
        print("!!!Неверный шаг сдвига!!!")
        return
    
    zashifr_text= Cezar(text, int(shift))
    decrypted_text = caesar_decipher(zashifr_text, int(shift))

    print("Начальный текст:", decrypted_text)
    print("Зашифрованный текст:", zashifr_text)

if __name__ == "__main__":
    main()
