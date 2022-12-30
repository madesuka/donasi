import requests
import streamlit as st
from streamlit_lottie import st_lottie
from PIL import Image


# Find more emojis here: https://www.webfx.com/tools/emoji-cheat-sheet/
st.set_page_config(page_title="My Webpage", page_icon=":tada:", layout="wide")


def load_lottieurl(url):
    r = requests.get(url)
    if r.status_code != 200:
        return None
    return r.json()


# Use local CSS
def local_css(file_name):
    with open(file_name) as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)


local_css("style/style.css")

# ---- LOAD ASSETS ----
lottie_coding = load_lottieurl("https://assets5.lottiefiles.com/packages/lf20_fcfjwiyb.json")
img_contact_form = Image.open("images/situasi.jpeg")
img_lottie_animation = Image.open("images/rekkrema1.jpeg")

# ---- HEADER SECTION ----
with st.container():
    st.subheader("Ayo berdonasi secara online ! :wave:")
    st.title("Berdana Punia Bersama Yayasan Satya Dharma Utama bersama PP POLRI BALI didukung Desa Adat Banyuasri Singaraja Bali")
    st.write(
        " Donasi dapat dikirimkan kepada Nomor Rekening Bank Mandiri KCP Singaraja 145-00- 1310040-5 Panitia Pembangunan Kreamtorium dan Rumah Duka oleh Yayasan SDU"
    )
    st.write("[](https://#)")

# ---- WHAT I DO ----
with st.container():
    st.write("---")
    left_column, right_column = st.columns(2)
    with left_column:
        st.subheader("Pembangunan Krematorium dan Rumah Duka Meliputi :")
        st.write("##")
        st.write(
            """
            1. Pembangunan Rumah Duka
            2. Pembangunan Ruangan Incenerator pembakaran jenazah
            3. Pembangunan fasilitas tempat Pendeta memimpin prosesi ritual 
            4. Pembangunan Fasilitas  Upacara Militer dan Adat
            5. Pembangunan ruang gambelan
            6. Pembangunan Pagar keliling
            7. Pengadaan Instalasi listrik
            8. Pembangunan Utilitas Air Bersih , Limbah dan sampah
            9. Pembangunan Kantor Yayasan
            10.Penataan kawasan tempat parkir pengunjung
                    
            """
        )
       
    with right_column:
        st_lottie(lottie_coding, height=300, key="coding")

# ---- PROJECTS ----
with st.container():
    st.write("---")
    st.subheader(" Latar Belakang Pembangunan Rumah Duka dan Krematorium :")
    st.write("##")
    image_column, text_column = st.columns((1, 2))
    with image_column:
        st.image(img_lottie_animation)
    with text_column:
        st.subheader("Krematorium dan Rumah Duka di Desa Adat Banyuasri Buleleng Bali")
        st.write(
            """
            Bertujuan :
            1. Menyediakan fasilitas umum dalam prosesi adat masyarakat hindu atau umat lain yg melakukan proses pembakaran jenazah
            2. Memfasilitasi kebutuhan prosesi adat yg telah memenuhi syarat legal baik skala maupun niskala
            3. Membantu masyarakat menyediakan sarana untuk dapat melakukan prosesi adat secara efisien dan terukur sesuai sastra agama
            4. Mendorong kemajuan masyarakat dalam melakukan upacara adat sesuai dengan perkembangan jaman
            """
        )
        
with st.container():
    image_column, text_column = st.columns((1, 2))
    with image_column:
        st.image(img_contact_form)
    with text_column:
        st.subheader("Informasi tentang kegiatan Pembangunan Krematorium dan Rumah duka progress 80 % ")
        st.write(
            """
            1. Telah terpasang peralatan incenerator atau peralatan pembakaran jenazah
            2. Tersedia mobil ambulance jenazah
            3. Konstruksi pembangunan rumah duka dan sarana lainnya
            4. Balai tempat prosesi adat
            5. Fasiltas para pelayat dan tempat penempatan sesajen
            6. Penanggung Jawab kegiatan pembangunan kreamtorium ini adalah Ketua Yayasan Satya Dharma Utama (Yayasan SDU) Brigjen Pol (Prn) Drs. Gede Atang Wiguna, SH
            7. Sekretariat Yayasan SDU : Jln. Jenderal Sudirman No.1, Kelurahan Banyuasri, Singaraja phone sekretaris W.A : Dawika 085737057787
            """
        )
        st.markdown("[Tonton Informasi Pembangunan Krematorium](https://www.youtube.com/watch?v=Nj_ev_evLPQ)")
        
# ---- CONTACT ----
with st.container():
    st.write("---")
    st.subheader(" Para dermawan dapat mengisi form berikut ini dengan melampirkan besaran dana yg ditransfer berupa copy bukti transfer")
    st.write("##")

    # Documention: https://formsubmit.co/ !!! CHANGE EMAIL ADDRESS !!!
    contact_form = """
    <form method="POST" action="https://formsubmit.co/sukawardikamade@gmail.com" enctype="multipart/form-data">
        <input type="hidden" name="_captcha" value="false">
        <input type="text" name=" Nama" placeholder=" Nama Lengkap" required>
        <input type="email" name="Email" placeholder=" Email yang masih aktip" required>
        <input type="text" name="Telephone" placeholder=" Nomor HP" required>
        <input type="text" name=" Tanggal kirim" placeholder=" diisi tanggal bulan dan tahun kirim donasi  " required>
        <input type="text" name=" Besar Sumbangan Rp. " placeholder=" ketik besar sumbangan" required>
        <textarea name="Alamat" placeholder=" Alamat lengkap  secara jelas" required></textarea>
        <input type="file" name="attachment" accept="image/png, image/jpeg">
        <button type="submit">Kirim</button>
        
    </form>
    """
    left_column, right_column = st.columns(2)
    with left_column:
        st.markdown(contact_form, unsafe_allow_html=True)
    with right_column:
        st.empty()
