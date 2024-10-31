import base64
import pickle

def base64_encode(text):
    textBytes = text.encode('utf-8')
    base64_bytes = base64.b64encode(textBytes)
    return base64_bytes.decode('utf-8')

text = input("sifrenizi olusturun: ")
passText = base64_encode(text)
# print(passText)
print("sifreniz olusturulmustur.")

with open("log.txt", "a") as file:
    file.write(f"\n{text} : {passText}")

with open('data.pkl', 'wb') as file:
    pickle.dump(passText, file)