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

class Node:
    def __init__(self, key, value):
        self.left = None
        self.right = None
        self.key = key  # Judul
        self.value = value  # Tahun

def insert(root, key, value):
    if root is None:
        return Node(key, value)
    if key < root.key:
        root.left = insert(root.left, key, value)
    elif key > root.key:
        root.right = insert(root.right, key, value)
    return root
root = None
for judul,tahun in data:
    root = insert(root, judul,tahun)

def binary_search(root, key):
    if root is None or root.key == key:
        return root
    if key < root.key:
        return binary_search(root.left, key)
    return binary_search(root.right, key)

# Contoh penggunaan pencarian:
cariJudul = "Horimiya"
def search_operation():
    search_result = binary_search(root, cariJudul)
    if search_result:
        print(f"{cariJudul} telah ditemukan, diterbitkan pada tahun: {search_result.value}")
    else:
        print(f"{cariJudul} tidak ditemukan.")
execution_time = timeit.timeit(search_operation, number=1000)  # Misalnya, diulang 1000 kali
print(f"Waktu eksekusi: {execution_time} detik")