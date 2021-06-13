def function():
    print('Nama saya najib')
function()


def method(name = "None"):
    print("Nama saya", name)

method() #otomatis keisi default "None"


#function keyword parameter
def fungsi(nama, kelas, asal):
    print("Nama saya ", nama, "Kelas", kelas, "Asal saya ", asal)
    
fungsi("JAFAR", "TT 41 12", "Bone") #pake keyword
#bisa tidak urut kalau fungsi(kelas = "TT 41 12",nama = "JAFAR", asal = "Bone" )


#RETURN VALUE

def add(a, b):
    result = a + b
    return result
add(2, 2)

def function_value():
    
    return "saya makan"
kamu = function_value()
print(kamu)


def nama(name):
    print("Nama saya ",name)
    return
nama("Ali")
