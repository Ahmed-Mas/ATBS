import PyPDF2

pdf = PyPDF2.PdfFileReader(open("C:\\Users\\ahmed\\Desktop\\test\\encryptcombinedminutes.pdf", "rb"))

passDic = open("C:\\Users\\ahmed\\Desktop\\test\\dictionary.txt")
temp = passDic.read().splitlines()

for word in temp:
    print("Checking..." + word)
    if pdf.decrypt(word) == 1:
        print("Password is...\n" + word)
        break