# Realtime Face Detection API

## Deskripsi

Proyek ini merupakan implementasi sistem Realtime Face Detection berbasis Web menggunakan Flask dan OpenCV.

Aplikasi mampu:

- Mengakses webcam secara realtime
- Mendeteksi wajah menggunakan Haar Cascade Classifier
- Menampilkan bounding box pada wajah
- Menampilkan posisi wajah (Kiri, Kanan, Atas, Bawah, Tengah)
- Berjalan melalui browser menggunakan Flask

---

## Teknologi yang Digunakan

- Python 3.x
- Flask
- OpenCV
- NumPy
- HTML
- CSS
- JavaScript

---

## Struktur Folder

```text
FACEDETECTIONAPI/
│
├── dataset/
│   ├── train/
│   │   ├── messi/
│   │   └── ronaldo/
│   │
│   └── test/
│       ├── messi/
│       └── ronaldo/
│
├── model/
│   └── haarcascade_frontalface_default.xml
│
├── static/
│   ├── script.js
│   └── style.css
│
├── templates/
│   └── index.html
│
├── app.py
├── requirements.txt
├── README.md
└── .gitignore
```

---

## Dataset

Dataset yang digunakan terdiri dari citra wajah pemain sepak bola:

### Training Dataset

| Kelas | Jumlah |
|---------|---------|
| Lionel Messi | 228 |
| Cristiano Ronaldo | 231 |
| Total | 459 |

### Testing Dataset

| Kelas | Jumlah |
|---------|---------|
| Lionel Messi | Sesuai folder test |
| Cristiano Ronaldo | Sesuai folder test |

Dataset digunakan sebagai dokumentasi proyek dan pengujian model deteksi wajah.

---

## Model

Model deteksi wajah menggunakan:

- Haar Cascade Classifier
- File:
  `haarcascade_frontalface_default.xml`

Sumber:

https://github.com/opencv/opencv/tree/master/data/haarcascades

---

## Cara Instalasi

Clone repository:

```bash
git clone https://github.com/USERNAME/Realtime-Face-Detection.git
```

Masuk ke folder project:

```bash
cd Realtime-Face-Detection
```

Install dependency:

```bash
pip install -r requirements.txt
```

---

## Menjalankan Program

```bash
python app.py
```

Buka browser:

```text
http://localhost:5000
```

---

## Fitur

- Realtime Webcam Detection
- Face Detection
- Face Position Detection
- Responsive Interface
- Flask API Integration

---

## Hasil Implementasi

Sistem berhasil:

- Mengakses webcam secara realtime
- Mendeteksi wajah pengguna
- Menampilkan jumlah wajah yang terdeteksi
- Menampilkan posisi wajah

Contoh posisi:

- Posisi Kiri
- Posisi Kanan
- Posisi Atas
- Posisi Bawah
- Posisi Tengah

---

## Author

Nama : Dendy Iqbal

Program Studi : Teknik Informatika

Universitas : (Isi Kampusmu)

Tahun : 2025