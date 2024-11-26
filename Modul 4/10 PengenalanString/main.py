# string adalah kumpulan dari karakter

data = "ini adalah string"
print(data)
print("panjang karakter: ", len(data))
print("tipe data : ", type(data))

#1. cara membuat string

"""
   1. dengan menggunakan single quote '---'
   2. dengan menggunakan double quote "---"
"""

data = 'menggunakan single quote'
print(data)

data = "menggunakan double quote"
print(data)

print("ini adalah hari jum'at")
print("nama saya ma'ruf")

# 2. kekuatan tanda \

# membuat ' menjadi string
print('mari sholat jum\'at')
print('Saya Ma\'ruf')

# double backslash
print('C:\\user\\adam')

# tab (\t)
print("MU\t\tJuara")

# backspace (\b)
print("MU\bJuara")

# newline (enter)
print("baris satu.\nbaris dua.") # LF -> lide feed # macOS
print("baris satu.\n\rbaris dua.") # CRLF -> windows

# raw string
print(r'C:\user\adam')