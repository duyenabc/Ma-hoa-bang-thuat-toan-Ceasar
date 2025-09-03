def mahoaCeasar(text, k):
    kq = ""
    k = k % 26
    for char in text:
        if not (char.isalpha() or char == " "):
            return "Không hợp lệ, vui lòng nhập lại."
    for char in text:
        if char == " ":
            kq += " "
            continue
        if char.isupper():
            start = ord('A')
        else:
            start = ord('a')
        iOld = ord(char) - start
        iNew = (iOld + k) % 26
        tuNew = chr(iNew + start)
        kq += tuNew
    return kq

plaintext = "Ta Loc Duyen"
k = 29
ciphertext = mahoaCeasar(plaintext, k)
print("Plaintext :", plaintext)
print("Ciphertext:", ciphertext)