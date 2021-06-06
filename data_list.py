my_list = []
my_list.append(10) #Memasukkan ke dalam list
my_list.append(12)
my_list.append(20)
my_list.append("najib")
print(my_list)
print(len(my_list))

#edit data
my_list[0] = 70
print(my_list)


#menghapus
my_list.remove(20) #untuk menghapus data ke dalam list
print(my_list)


a = int(input("masukkan data ke dalam my_list :"))
my_list.append(a)
print(my_list)

