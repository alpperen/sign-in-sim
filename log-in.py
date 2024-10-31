import base64
import pickle
import os
import webbrowser

def base64_encode(text):
    text_bytes = text.encode('utf-8')
    base64_bytes = base64.b64encode(text_bytes)
    return base64_bytes.decode('utf-8')

passInput = input("giris yapmak icin sifrenizi giriniz: ")


with open('data.pkl', 'rb') as file:
    stored_pass = pickle.load(file)


encoded_input_pass = base64_encode(passInput)


if encoded_input_pass == stored_pass:
    print("Basarili")
    # os.popen(r"C:\Program Files\Google\Chrome\Application\chrome.exe")
    webbrowser.open(r"C:\Users\alperen\Desktop\SignIn\main.html")


    pkl_dosyasi = 'data.pkl'

    try:
        os.remove(pkl_dosyasi)
    except:
        pass

else:
    print("Basarisiz, sifre yanlis.")
