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

def linear_search(data, judul):
    for i in range(len(data)):
        if data[i][0] == judul:
            return f"{judul} telah ditemukan, diterbitkan pada tahun: {data[i][1]}"
    return f"{judul} tidak ditemukan."

# Contoh penggunaan pencarian:
cariJudul = "Horimiya"
def search_operation():
    search_result = linear_search(data,cariJudul)
    print(search_result)
execution_time = timeit.timeit(search_operation, number=1000)  # Misalnya, diulang 1000 kali
print(f"Waktu eksekusi: {execution_time} detik")