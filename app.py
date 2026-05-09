import streamlit as st
import time
import os

# Konfigurasi Halaman
st.set_page_config(page_title="Survei Dinamika Mahasiswa", page_icon="🎓", layout="centered")

# --- CUSTOM CSS ---
st.markdown("""
    <style>
    .stApp { background-color: #f8f9fa; }
    div.stButton > button:first-child { background-color: #0056b3; color: white; border-radius: 8px; width: 100%; font-weight: bold; border: none; padding: 10px; }
    div.stButton > button:first-child:hover { background-color: #004494; }
    .main-header { font-size: 28px; font-weight: 900; color: #1e3a8a; text-align: center; margin-bottom: 5px; }
    .sub-text { text-align: center; color: #64748b; font-size: 15px; margin-bottom: 25px; }
    div[data-testid="stForm"] { background-color: #ffffff; padding: 25px; border-radius: 15px; box-shadow: 0px 4px 10px rgba(0, 0, 0, 0.05); border: 1px solid #e2e8f0; }
    </style>
""", unsafe_allow_html=True)

st.markdown('<div class="main-header">🎓 Survei Dinamika Mahasiswa </div>', unsafe_allow_html=True)
st.markdown('<div class="sub-text">Bantu kami memetakan tingkat stres dan kebahagiaan mahasiswa di pertengahan semester ini.</div>', unsafe_allow_html=True)

with st.form("kampus_form"):
    st.write("📝 **Part 1: Realita Akademik**")
    semester = st.selectbox("1. Kamu sekarang angkatan / semester berapa?", 
                            ["Pilih Semester...", "Semester 2", "Semester 4", "Semester 6", "Semester 8 / Pejuang Skripsi"])
    
    keluhan = st.radio("2. Apa keluhan terbesarmu di kampus minggu ini?", 
                       ("Tugas / Jurnal / Laporan praktikum numpuk 📚", 
                        "Bimbingan dosen yang menguras energi 🤯", 
                        "Cuaca Semarang yang lagi panas-panasnya ☀️", 
                        "Nungguin notif chat dari 'seseorang' yang nggak kunjung datang 📱"))
                        
    st.write("---")
    st.write("☕ **Part 2: Healing & Social Life**")
    
    healing = st.radio("3. Kalau lagi sumpek urusan kampus, pelariannya biasanya ke mana?",
                       ("Maraton film di kos / nonton bioskop bareng teman 🍿", 
                        "Nongkrong di cafe / ngopi santai ☕", 
                        "Jalan-jalan random tengah malam / cari jajan manis 🛵🍦", 
                        "Scroll sosmed doang sampai ketiduran 😴"))
                        
    inisial = st.text_input("4. Jujur, ada nggak inisial nama seseorang yang lagi jadi penyemangat kamu saat ini? (Tulis inisial/kosongkan)")
    
    submit = st.form_submit_button("Kirim Survei 🚀")

# LOGIKA PENYIMPANAN & JALUR BELAKANG (BACKDOOR)
if submit:
    # 🕵️‍♂️ 1. JIKA MAS YUDHA MASUKIN PASSWORD LIHAT DATA
    if inisial == "PahlawanPantura": 
        st.success("Selamat datang di Markas, Komandan! 🫡 Berikut data intelijen yang masuk:")
        if os.path.exists("data_rahasia.txt"):
            with open("data_rahasia.txt", "r") as f:
                st.code(f.read())
        else:
            st.info("Belum ada target yang mengisi survei ini.")
            
    # 🧹 2. JIKA MAS YUDHA MASUKIN PASSWORD HAPUS DATA
    elif inisial == "ResetMarkas":
        if os.path.exists("data_rahasia.txt"):
            os.remove("data_rahasia.txt")
            st.success("Data intelijen berhasil dihapus bersih tanpa sisa! 🧹✨")
        else:
            st.warning("Gudang data sudah kosong, Komandan!")

    # 👱‍♀️ 3. JIKA NINIS (ATAU ORANG LAIN) YANG NGISI
    else:
        # Simpan datanya ke file text
        with open("data_rahasia.txt", "a") as f:
            f.write(f"--- DATA BARU MASUK ---\nSemester: {semester}\nKeluhan: {keluhan}\nHealing: {healing}\nInisial Doi: {inisial}\n\n")
            
        with st.spinner("Menyimpan data secara anonim ke server kampus... 📡"):
            time.sleep(2)
        st.success("Terima kasih sudah berpartisipasi! Data kamu aman. Semangat terus kuliah dan bimbingannya! ✨")
        
        if "Nungguin notif" in keluhan or inisial != "":
            st.info("Pesan Admin: Kurang-kurangin gengsinya ya, kalau kangen mending chat duluan aja! 🏃‍♂️💨")
