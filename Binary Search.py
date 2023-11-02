import csv
import timeit

data = []  # List untuk menyimpan data dari CSV
with open('data.csv', 'r', encoding='utf-8') as csvfile:
    csvreader = csv.reader(csvfile)
    next(csvreader)  # Lewati baris kolom
    for row in csvreader:
        judul = row[0]
        tahun = row[1]
        data.append((judul,tahun))
data.sort()
def binary_search(data, judul):
    left, right = 0, len(data) - 1
    while left <= right:
        mid = left + (right - left) // 2
        if data[mid][0] == judul:
            return mid  # Elemen ditemukan
        elif data[mid][0] < judul:
            left = mid + 1
        else:
            right = mid - 1
    return -1

# Contoh penggunaan pencarian:
cariJudul = "Zetsubou no Rakuen"
def search_operation():
    search_result = binary_search(data, cariJudul)
    if search_result:
        print(f"{cariJudul} telah ditemukan, diterbitkan pada tahun: {data[search_result][1]}")
    else:
        print(f"{cariJudul} tidak ditemukan.")
execution_time = timeit.timeit(search_operation,number=1)  # Misalnya, diulang 1000 kali
print(f"Waktu eksekusi: {execution_time} detik")