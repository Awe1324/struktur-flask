# Flask PostgreSQL CRUD Mahasiswa

Project sederhana berbasis Flask untuk mengelola data mahasiswa menggunakan PostgreSQL sebagai database dan Postman.  
Fitur yang tersedia meliputi:
- Menambahkan data mahasiswa (POST)
- Menampilkan semua data (GET)
- Menampilkan detail mahasiswa berdasarkan NIM (GET by NIM)
- Menghapus data mahasiswa (DELETE)

# Teknologi yang Digunakan
- Python 3.10.11
- Flask  
- psycopg2  
- PostgreSQL  
- Postman

# Cara Menjalankan
 - buat venv, dan masuk venv dengan tekan tombol CTRL+SHIFT+P-select interpreter-aktifkan python venv
 - install library yang diperlukan
 - buat database di PG admin/postgresql
    CREATE DATABASE mahasiswa;
        CREATE TABLE data_mahasiswa (
            nim VARCHAR(20) PRIMARY KEY,
            nama VARCHAR(100),
            alamat VARCHAR(150),
            tanggal_lahir DATE,
            tanggal_masuk DATE
            );
 - jalankan program flask (python main.py) diterminal Vscode

# Endpoint yang tersedia
- pastikan data sudah ada, jika belum buat di pgadmin/postman

   | Metode | URL | Keterangan |
   |---------|-----|------------|
   | GET | /mahasiswa | Menampilkan semua data |
   | GET | /mahasiswa/<nim> | Menampilkan data berdasarkan NIM |

- gunakan postman untuk mengelola data seperti menambah,dan menghapus data
