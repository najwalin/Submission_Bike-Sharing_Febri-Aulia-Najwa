import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.ticker as ticker
import seaborn as sns
import streamlit as st

# Konfigurasi Dashboard
st.set_page_config(page_title="Bike Sharing Dashboard", layout="wide")
sns.set(style='dark')

# Session Login User
if"user_name" not in st.session_state:
    st.session_state.user_name= "" 

# Halaman Login User
if st.session_state.user_name == "":
    st.title("👋🚲 Selamat Datang di Dashboard Bike Sharing")

    name = st.text_input("Masukkan Nama Anda")

    if st.button("Masuk Dashboard"):
        if name.strip() != "":
            st.session_state.user_name = name
            st.experimental_rerun()
        else:
            st.warning("Nama harus diisi, tidak boleh kosong!")
    st.stop()

# Load Data
def load_data():
    day_df = pd.read_csv("day_all_data.csv")
    hour_df = pd.read_csv("hour_all_data.csv")

    day_df['dteday'] = pd.to_datetime(day_df['dteday'])
    hour_df['dteday'] = pd.to_datetime(hour_df['dteday'])

    return day_df, hour_df

day_df, hour_df = load_data()

# SideBar Menu
with st.sidebar:
    st.success(f"Halo, {st.session_state.user_name} 👋")

    menu = st.radio(
        "Pilih Menu Analisis",
        ["Home", "Faktor Cuaca", "Analisis Jam", "Kondisi Cuaca", "Clustering"]  
    )

    if st.button("Ganti User"):
        st.session_state.user_name = "" 
        st.experimental_rerun()

# Rentang Waktu
min_date = day_df['dteday'].min().date()
max_date = day_df['dteday'].max().date()

start_date, end_date = st.sidebar.date_input(
    "Pilih Rentang Tanggal",
    [min_date, max_date]
)

main_day_df = day_df[(day_df["dteday"] >= pd.to_datetime(start_date)) &
                    (day_df['dteday'] <= pd.to_datetime(end_date))]  
main_hour_df = hour_df[(hour_df["dteday"] >= pd.to_datetime(start_date)) &
                      (hour_df["dteday"] <= pd.to_datetime(end_date))]

# Halaman Home
if menu == "Home":
    st.title("🚵 Bike Sharing Dashboard")

    col1, col2, col3 = st.columns(3)

    col1.metric("Total Casual", f"{main_day_df['casual'].sum():,}")
    col2.metric("Total Registered", f"{main_day_df['registered'].sum():,}")
    col3.metric("Total Penyewaan Sepeda", f"{main_day_df['cnt'].sum():,}")

    st.info("📌 Secara keseluruhan, pengguna registered jauh lebih sering menggunakan layanan dibandingkan dengan pengguna casual.")

# Faktor Cuaca
elif menu == "Faktor Cuaca":

    st.header("📊 Analisis Pengaruh Faktor Cuaca terhadap Penyewaan Sepeda")

    # Menampilkan perbandingan total penyewaan sepeda berdasarkan tipe pengguna
    fig, ax = plt.subplots(1,2, figsize=(12,5))    

    sns.barplot(
        x=['Casual', 'Registered'],
        y=[main_day_df['casual'].sum(), main_day_df['registered'].sum()],
        palette=['#60A5FA', '#F87171'],
        ax=ax[0]
    )

    ax[0].set_xlabel("Tipe Pengguna")
    ax[0].set_ylabel("Jumlah Penyewaan Sepeda")
    ax[0].set_title("Perbandingan Total Penyewaan Sepeda")
    ax[0].yaxis.set_major_formatter(ticker.StrMethodFormatter('{x:,.0f}'))

    ax[1].pie(
        [main_day_df['casual'].sum(), main_day_df['registered'].sum()],
        labels=['Casual', 'Registered'],
        autopct='%1.1f%%',
        colors=['#60A5FA', '#F87171']
    )
    ax[1].set_title("Persentase Pengguna Sepeda")

    st.pyplot(fig)

    st.info("📌 Jika dilihat dari totalnya, pengguna registered menyumbang sebagian besar penyewaan sepeda dibandingkan dengan pengguna casual.")

    # Menampilkan heatmap korelasi variabel cuaca terhadap penyewaan sepeda
    corr = main_day_df[['temp','hum','windspeed','cnt']].corr()

    fig, ax = plt.subplots(figsize=(8,6))
    sns.heatmap(corr, annot=True, cmap='coolwarm', fmt='.2f')
    ax.set_title("Heatmap Korelasi Variabel Cuaca dan Penyewaan Sepeda")

    st.pyplot(fig)

    st.info("📌 Dari korelasi yang terlihat, suhu memiliki hubungan paling kuat dengan jumlah penyewaan sepeda.")

    # Menampilkan visualisasi pengaruh suhu, kelembapan, dan kecepatan angin terhadap tipe pengguna
    st.subheader("📈 Pengaruh Detail Faktor Cuaca")

    fig, ax = plt.subplots(2,3, figsize=(15,8))
    
    sns.regplot(x='temp', y='casual', data=main_day_df, ax=ax[0,0], color='#3B82F6')
    ax[0,0].set_title('Pengaruh Suhu terhadap\n Penyewaan Sepeda (Casual)')

    sns.regplot(x='hum', y='casual', data=main_day_df, ax=ax[0,1], color='#10B981')
    ax[0,1].set_title('Pengaruh Kelembapan terhadap\n Penyewaan Sepeda (Casual)')

    sns.regplot(x='windspeed', y='casual', data=main_day_df, ax=ax[0,2], color='#F5930B')
    ax[0,2].set_title('Pengaruh Kecepatan Angin terhadap\n Penyewaan Sepeda (Casual)')

    sns.regplot(x='temp', y='registered', data=main_day_df, ax=ax[1,0], color='#3B82F6')
    ax[1,0].set_title('Pengaruh Suhu terhadap\n Penyewaan Sepeda (Registered)')

    sns.regplot(x='hum', y='registered', data=main_day_df, ax=ax[1,1], color='#10B981')
    ax[1,1].set_title('Pengaruh Kelembapan terhadap\n Penyewaan Sepeda (Registered)')

    sns.regplot(x='windspeed', y='registered', data=main_day_df, ax=ax[1,2], color='#F5930B')
    ax[1,1].set_title('Pengaruh Kecepatan Angin terhadap\n Penyewaan Sepeda (Registered)')

    plt.tight_layout()
    st.pyplot(fig)

    st.info("📌 Penyewaan cenderung meningkat saat suhu lebih hangat, sementara kelembapan tinggi dan angin kencang justru berkaitan dengan penurunan jumlah penyewaan sepeda.")

# Analisis Jam
elif menu == "Analisis Jam":

    st.header("⏰ Analisis Pola Penyewaan Sepeda Berdasarkan Jam")

    # Menampilkan rata-rata penyewaan sepeda per jam
    hour_avg = main_hour_df.groupby('hr')['cnt'].mean()

    fig, ax  = plt.subplots(figsize=(10,5))
    ax.plot(hour_avg.index, hour_avg.values, marker='o', color='#4F46E5')

    ax.set_xticks(range(0,24))
    ax.set_xlabel("Jam")
    ax.set_ylabel("Rata-Rata Penyewaan Sepeda")
    ax.set_title("Rata-Rata Penyewaan Sepeda per Jam")

    st.pyplot(fig)

    st.info("📌 Aktivitas penyewaan sepeda paling ramai terjadi pada jam-jam sibuk, terutama pagi dan sore hari.")

    # Menampilkan perbandingan penyewaan sepeda antara weekday dan weekend
    weekday = main_hour_df[main_hour_df['day_type']=='Weekday'].groupby('hr')['cnt'].mean()
    weekend = main_hour_df[main_hour_df['day_type']=='Weekend'].groupby('hr')['cnt'].mean()
    
    fig, ax = plt.subplots(figsize=(10,5))
    ax.plot(weekday.index, weekday.values, marker='o', label='Weekday', color='#10B981')
    ax.plot(weekend.index, weekend.values, marker='o', label='Weekend', color='#F59E0B')

    ax.set_xticks(range(0,24))
    ax.set_xlabel("Jam")
    ax.set_ylabel("Rata-Rata Penyewaan Sepeda")
    ax.set_title("Perbandingan Penyewaan Sepeda antara Weekday dan Weekend")
    ax.legend()

    st.pyplot(fig)

    st.info("📌 Pada Weekday, penyewaan lebih tinggi di jam berangkat dan pulang kerja, sedangkan weekend cenderung lebih merata.")

# Kondisi Cuaca
elif menu == "Kondisi Cuaca":

    st.header("🌦️ Analisis Penyewaan Berdasarkan Kondisi Cuaca")

    weather_avg = main_day_df.groupby('weathersit')['cnt'].mean().reset_index()

    fig, ax = plt.subplots(figsize=(10,5))
    sns.barplot(data=weather_avg, x='weathersit', y='cnt', palette='viridis')

    ax.set_xlabel("Kondisi Cuaca")
    ax.set_ylabel("Rata-Rata Jumlah Penyewaan Sepeda")
    ax.set_title("Rata-Rata Penyewaan Sepeda Berdasarkan Kondisi Cuaca")

    st.pyplot(fig)

    st.info("📌 Penyewaan sepeda tertinggi terjadi saat kondisi cuaca cerah, dan menurun ketika cuaca kurang mendukung.") 

# Clustering Waktu
elif menu == "Clustering":

    st.header("🕐 Analisis Cluestering Waktu Penyewaan Sepeda")

    def time_category(hr):
        if 5 <= hr < 10: return 'Morning'
        elif 10 <= hr < 15: return 'Afternoon'
        elif 15 <= hr < 20: return 'Evening'
        else: return 'Night'

    main_hour_df['time_cat'] = main_hour_df['hr'].apply(time_category)

    time_cluster = main_hour_df.groupby('time_cat')['cnt'].mean().reset_index()

    fig, ax = plt.subplots(figsize=(8,5))
    sns.barplot(
        data=time_cluster,
        x='time_cat',
        y='cnt',
        order=['Morning', 'Afternoon','Evening','Night']
    )

    ax.set_xlabel("Kategori Waktu")
    ax.set_ylabel("Rata-Rata Penyewaan Sepeda")
    ax.set_title("Rata-Rata Penyewaan Sepeda Berdasarkan Waktu")

    st.pyplot(fig)

    st.info("📌 Waktu sore hari (evening) merupakan periode dengan aktivitas penyewaan tertinggi dibandigkan dengan waktu lainnya.")

# Footer
st.markdown("""
<style>
.stApp{
    background-color: #F9FAFB;
}
h1, h2, h3 {
    color: #111827;
}
</style>
""", unsafe_allow_html=True)