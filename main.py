from flask import Flask, request, jsonify
import psycopg2

app = Flask(__name__)

# Konfigurasi koneksi ke PostgreSQL
conn = psycopg2.connect(
    host="localhost",
    database="mahasiswa",
    user="postgres",
    password="1324"
)


# Endpoint GET - ambil semua data
@app.route('/mahasiswa', methods=['GET'])
def get_all():
    cur = conn.cursor()
    cur.execute("SELECT * FROM data_mahasiswa ORDER BY nim;")
    rows = cur.fetchall()
    cur.close()

    data = []
    for r in rows:
        data.append({
            'nim': r[0],
            'nama': r[1],
            'alamat': r[2],
            'tanggal_lahir': str(r[3]),
            'tanggal_masuk': str(r[4])
        })
    return jsonify(data)

# Endpoint GET DETAIL - ambil 1 data berdasarkan NIM
@app.route('/mahasiswa/<nim>', methods=['GET'])
def get_detail(nim):
    cur = conn.cursor()
    cur.execute("SELECT * FROM data_mahasiswa WHERE nim = %s;", (nim,))
    row = cur.fetchone()
    cur.close()

    if row:
        return jsonify({
            'nim': row[0],
            'nama': row[1],
            'alamat': row[2],
            'tanggal_lahir': str(row[3]),
            'tanggal_masuk': str(row[4])
        })
    else:
        return jsonify({'message': 'Data tidak ditemukan'}), 404

#Endpoint POST - tambah data baru
@app.route('/mahasiswa', methods=['POST'])
def add_data():
    data = request.get_json()
    cur = conn.cursor()
    cur.execute("""
        INSERT INTO data_mahasiswa (nim, nama, alamat, tanggal_lahir, tanggal_masuk)
        VALUES (%s, %s, %s, %s, %s);
    """, (data['nim'], data['nama'], data['alamat'], data['tanggal_lahir'], data['tanggal_masuk']))
    conn.commit()
    cur.close()
    return jsonify({'message': 'Data berhasil ditambahkan'}), 201

# Endpoint DELETE - hapus data berdasarkan NIM
@app.route('/mahasiswa/<nim>', methods=['DELETE'])
def delete_data(nim):
    cur = conn.cursor()
    cur.execute("DELETE FROM data_mahasiswa WHERE nim = %s;", (nim,))
    conn.commit()
    cur.close()
    return jsonify({'message': f'Data dengan NIM {nim} berhasil dihapus'})

if __name__ == '__main__':
    app.run(debug=True)
