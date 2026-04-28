# Submission_Bike-Sharing_Febri-Aulia-Najwa
# Bike Sharing Dashboard
- Oleh: Febri Aulia Najwa
- ID Dicoding: CDCC229D6X1247

# Deskripsi Proyek
Dashboard ini merupakan aplikasi analisis data interaktif yang dibuat menggunakan Python dan Streamlit. Dashboard ini digunakan untuk mengeksplorasi dan memahami pola penyewaan sepeda berdasarkan tipe pengguna, waktu (jam), serta faktor lingkungan seperti cuaca, suhu, kelembapan, dan kecepatan angin. Melalui visualisasi yang disediakan, pengguna dapat melihat bagaimana perilaku penyewaan sepeda berubah dalam berbagai kondisi, sehingga dapat memberikan insight yang berguna untuk pengambilan keputusan.

# Fitur Utama
- **Login Sederhana Pengguna**: Pengguna diminta memasukkan nama sebelum masuk ke dashboard.
- **Filter Rentang Waktu**: Data dapat difilter berdasarkan tanggal tertentu melalui sidebar.
- **Ringkasan Metrik Utama**: Menampilkan total pengguna casual, pengguna registered, dan total penyewaan sepeda.
- **Analisis Tipe Pengguna**: Perbandingan total penyewaan (bar chart) dan persentase pengguna (pie chart).
- **Analisis Faktor Cuaca**: Heatmap korelasi (temp, hum, windspeed) serta visualisasi pengaruh suhu, kelembapan, dan angin terhadap penyewaan.
- **Analisis Pola Jam**: Rata-rata penyewaan sepeda per jam (0 hingga 23) serta perbandingan weekday dan weekend.
- **Analisis Kondisi Cuaca**: Menampilkan rata-rata penyewaan berdasarkan kondisi cuaca.
- **Clustering Waktu**: Mengelompokkan waktu menjadi morning, afternoon, evening, dan night. 

# Teknologi yang Digunakan
- **Python**: Bahasa pemrograman
- **Pandas**: Manipulasi data
- **NumPy**: Komputasi numerik
- **Matplotlib**: Visualisasi dasar
- **Seaborn**: Visualisasi statistik
- **Streamlit**: Pembuatan dashboard interaktif

# Deskripsi Data
Dataset terdiri dari dua file utama yang berisi data penyewaan sepeda dari tahun 2011-2012, sebagai berikut:
- **day_all_data.csv**: Data agregat harian
- **hour_all_data.csv**: Data agregat per jam

# Kolom Utama
- `dteday`: Tanggal
- `cnt`: Total penyewaan sepeda
- `casual`: Pengguna tidak terdaftar
- `registered`: Pengguna terdaftar
- `temp`: Suhu
- `hum`: Kelembapan
- `windspeed`: Kecepatan angin
- `hr`: Jam (0 hingga 23)
- `weathersit`: Kondisi cuaca

# Cara Menjalankan Dashboard
1. Pastikan semua file berikut ada dalam satu folder
   - **dashboard.py**
   - **day_all_data.csv**
   - **hour_all_data.csv**
   - **requirements.txt**

2. **Membuat Virtual Environment**
   Untuk menghindari bentrok antar library, sebaiknya gunakan virtual environment. Buka terminal atau
   command prompt di folder proyek, selanjutnya jalankan
   *Windows*
   python -m venv venv
   venv\Script\activate

3. **Instalasi library** 
   Setelah environment aktif, install semua library yang dibutuhkan menggunakan file requirements.txt
   dengan menjalankan perintah:
   pip install -r requirements.txt
   
4. **Menjalankan aplikasi streamlit**
   Setelah semua sudah siap, jalankan perintah berikut untuk membuka dashboard di browser: https://submissionbike-sharingfebri-aulia-najwa-8rmriqgotigudfrzrt6spm.streamlit.app/
