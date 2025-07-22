# app.py
import streamlit as st
import json
import os

# Path ke data hasil crawling
DATA_PATH = "data/books.json"

st.set_page_config(page_title="Web Crawler Search", layout="wide")
st.title("🔍 Web Crawler Search App")

# Load data JSON
if os.path.exists(DATA_PATH):
    with open(DATA_PATH, "r", encoding="utf-8") as f:
        data = json.load(f)
else:
    st.warning("📂 Data belum tersedia. Jalankan crawler terlebih dahulu.")
    st.stop()

# Input pencarian
query = st.text_input("Cari judul, rating, atau harga:", "")

# Filter data berdasarkan query
if query:
    filtered = [
        item for item in data
        if query.lower() in item.get("title", "").lower()
        or query.lower() in item.get("rating", "").lower()
        or query.lower() in item.get("price", "").lower()
    ]
    st.markdown(f"### 🔎 {len(filtered)} hasil ditemukan")
else:
    filtered = data
    st.markdown(f"### 📚 Menampilkan semua hasil ({len(filtered)} total)")

# Tampilkan hasil
for item in filtered:
    st.markdown(f"### {item.get('title', '(Judul tidak tersedia)')}")
    st.write(f"💵 **Harga:** {item.get('price', '-')}")
    st.write(f"⭐ **Rating:** {item.get('rating', '-')}")
    st.write(f"📦 **Stok:** {item.get('avaibility', '-')}")
    st.markdown(f"[🔗 Lihat Buku]({item.get('link', '#')})")
    st.markdown("---")
