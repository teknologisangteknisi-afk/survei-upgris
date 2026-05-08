import streamlit as st
import time

# Konfigurasi Halaman
st.set_page_config(page_title="Survei Mahasiswa UPGRIS", page_icon="🎓", layout="centered")

# --- CUSTOM CSS UNTUK TAMPILAN RAPI & PROFESIONAL ---
st.markdown("""
    <style>
    /* Mengubah warna latar belakang aplikasi (opsional, warna terang/bersih) */
    .stApp {
        background-color: #f8f9fa;
    }
    /* Mempercantik tombol Submit */
    div.stButton > button:first-child {
        background-color: #0056b3;
        color: white;
        border-radius: 8px;
        width: 100%;
        font-weight: bold;
        border: none;
        padding: 10px;
    }
    div.stButton > button:first-child:hover {
        background-color: #004494;
        border: none;
    }
    /* Styling Judul */
    .main-header {
        font-size: 28px;
        font-weight: 900;
        color: #1e3a8a;
        text-align: center;
        margin-bottom: 5px;
    }
    .sub-text {
        text-align: center;
        color: #64748b;
        font-size: 15px;
        margin-bottom: 25px;
    }
    /* Styling Card/Box untuk Form */
    div[data-testid="stForm"] {
        background-color: #ffffff;
        padding: 25px;
        border-radius: 15px;
        box-shadow: 0px 4px 10px rgba(0, 0, 0, 0.05);
        border: 1px solid #e2e8f0;
    }
    </style>
""", unsafe_allow_html=True)

# Judul dan Deskripsi
st.markdown('<div class="main-header">🎓 Survei Dinamika Mahasiswa </div>', unsafe_allow_html=True)
st.markdown('<div class="sub-text">Bantu kami memetakan tingkat stres dan kebahagiaan mahasiswa di pertengahan semester ini.</div>', unsafe_allow_html=True)

# Membuat Form Survei
with st.form("kampus_form"):
    st.write("📝 **Part 1: Realita Akademik**")
    
    # Pertanyaan Normal
    semester = st.selectbox("1. Kamu sekarang angkatan / semester berapa?", 
                            ["Pilih Semester...", "Semester 2", "Semester 4", "Semester 6", "Semester 8 / Pejuang Skripsi"])
    
    # Pertanyaan Normal dengan 1 Jebakan Halus
    keluhan = st.radio("2. Apa keluhan terbesarmu di kampus minggu ini?", 
                       ("Tugas / Jurnal / Laporan praktikum numpuk 📚", 
                        "Bimbingan dosen yang menguras energi 🤯", 
                        "Cuaca Semarang yang lagi panas-panasnya ☀️", 
                        "Nungguin notif chat dari 'seseorang' yang nggak kunjung datang 📱")) # Jebakan
                        
    st.write("---")
    st.write("☕ **Part 2: Healing & Social Life**")
    
    # Pertanyaan Jebakan (Menyindir kelakuannya dan kelakuan Mas Yudha)
    healing = st.radio("3. Kalau lagi sumpek urusan kampus, pelariannya biasanya ke mana?",
                       ("Maraton film di kos / nonton bioskop bareng teman 🍿", # Menyindir Mas Yudha
                        "Nongkrong di cafe / ngopi santai ☕", # Menyindir Mas Yudha
                        "Jalan-jalan random tengah malam / cari jajan manis 🛵🍦", # Menyindir Ninis banget
                        "Scroll sosmed doang sampai ketiduran 😴"))
                        
    # Pertanyaan PDKT Halus
    inisial = st.text_input("4. Jujur, ada nggak inisial nama seseorang di UPGRIS yang lagi jadi penyemangat (atau malah bikin overthinking) kamu saat ini? (Tulis inisial/kosongkan)")
    
    # Tombol Submit
    submit = st.form_submit_button("Kirim Survei 🚀")

# Logika setelah tombol ditekan
if submit:
    with st.spinner("Menyimpan data secara anonim ke server kampus (bohongan)... 📡"):
        time.sleep(2)
    st.success("Terima kasih sudah berpartisipasi! Data kamu aman. Semangat terus kuliah dan bimbingannya! ✨")
    
    # Pesan Pop-up Iseng
    if "Nungguin notif" in keluhan or inisial != "":
        st.info("Pesan Admin: Kurang-kurangin gengsinya ya, kalau kangen mending chat duluan aja! 🏃‍♂️💨")