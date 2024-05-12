import streamlit as st
from streamlit_option_menu import option_menu

st.set_page_config(
    page_title="kelompoksebelas_lpk",
    page_icon="🤪",
)

st.image('welcomebg.jpg')
st.write ('''
"hallo users, selamat datang di aplikasi web project kelompok 11!! \n
Web ini dibuat untuk memudahkan kamu dalam mendapatkan informasi terkait indeks massa tubuh kamu sehingga kamu bisa mengetahui informasi mengenai kondisi tubuh saat ini, resiko yang mungkin terjadi dan kamu akan mendapatkan saran untuk mengatasi resikonya. Web ini juga dibuat untuk memudahkan kamu dalam mendapatkan informasi mengenai kadar gula darah kamu saat ini. 
SELAMAT MENCOBA <3.
''')
navbar = option_menu(menu_title=None, options=['Home', 'Kalkulator IMT', 'Cek Kadar Gula Darah',], icons=['0','0','0'])

if navbar == 'Home' :
    st.title('Kalkulator IMT dan Cek Kadar Gula Darah')
    st.subheader('Kelompok 11')
    st.write('''
    Harissa Hurulaini (2360138) \n
    Jalaludin Muhamad Akbar (2360150) \n
    Kayla Pramudewi Yudha (2360155) \n
    Nadya Aprilya Nurwita Putri (22360198)\n
    Novita Nurmayanti (2360216) ''')     

if navbar == 'Kalkulator IMT' :
    st.title('KALKULATOR INDEKS MASSA TUBUH')
    col1, col2, col3 = st.columns(3)
    with col2 :
        st.image('rumusimt.jpg', width=500)
    jenis_kelamin = st.selectbox('Pilih Jenis Kelamin', options=['Laki Laki', 'Perempuan'])
    nama = st.text_input('Masukkan nama anda')
    usia = st.number_input('Masukkan usia anda')
    tinggi = st.number_input('Masukkan tinggi anda (cm)')
    berat = st.number_input('Masukkan berat badan anda (kg)')
    column1, column2, column3 = st.columns(3)
    with column2 :
        st.image('tabelimt.jpg', width=500)
    if st.button('Hitung') :
        IMT = (berat)/((tinggi**2)/10000)
        if IMT <= 18.4 :
            st.warning(f'Anda Kekurangan Bobot\n IMT {nama} adalah {IMT}')
            st.write('''  Resiko : Berdasarkan hasil penelitian, ketika berat badan anda cukup rendah dari berat ideal, Anda juga memiliki resiko \n penyakit tertentu akibat kekursangan nutrisi dan sistem kekebalan tubuh yang lemah.
Hal ini akan mengakibatkan resiko kesehatan seperti berikut ini : \n
-Malnutrisi. \n
-Anemia. \n
-Siklus menstruasi yang tidak teratur. \n
-Resiko tulang rapuh. ''')
            st.write(''' Saran : Anda bisa mengkonsumsi asupan kalori yang lebih banyak daripada asupan kalori biasanya. Anda juga bisa rutin berolahraga agar otot di tubuh anda semakin optimal. Menghindari makanan rendah kalori atau makanan ringan yang tidak bergizi. ''')
        elif IMT <= 22.9 :
            st.success(f'hasil IMT {nama} Sehat,\nIMT {nama} adalah {IMT}')
            st.write('''
            Resiko : Orang dengan IMT normal masih tetap bisa mmeiliki resiko kesehatan tergantung pada faktor faktor lain seperti tingkat kebugaran fisik, pola makan, kebiasaan merokok dan juga riwayat keluarga. Orang dengan IMT normal juga harus tetap menjaga gaya hidup sehat untuk mengurangi resiko penyakit seperti diabetes, jantung dan tekanan darah tinggi. \n
            ''')
            st.write(''' Saran : Anda perlu aktif rutin berolahraga, makan makanan yang kaya akan nutrisi, dan pastikan untuk menjaga keseimbangan antara pekerjaan dan istirahat. ''')
        elif IMT <= 24.9 :
            st.warning(f'Hasil IMT {nama} Kelebihan Bobot, \nIMT {nama} adalah {IMT}')
            st.write('''
            Resiko : Orang yang memiliki kelebihan berat badan memiliki resiko yang lebih tinggi untuk berbagai kondisi kesehatan serius, termasuk diabetes tipe 2, penyakit jantung, tekanan darah tinggi, stroke, penyakit hati, gangguan pernapasan, dan beberapa masalah kesehatan. ''')
            st.write(''' Saran : Bagi orang yang memiliki kelebihan bobot penting untuk menagdopsi gaya hidup sehat seperti fokus pada makan makanan yang kaya akan serat, dan hindari makanan olahan tinggi gula sera lemak jenuh. Jangan lupa untuk berolahraga secara teratur, Minum air putih yang cukup, serta anda juga bisa langsung berkonsultasi pada dokter atau ahli gizi. ''')
        elif IMT <= 29.9 : 
            st.error(f'Anda obesitas tingkat 1, \nIMT {nama} adalah {IMT}')
            st.write('''
            Resiko : Obesitas membawa efek bagi tubuh, meningkatkan resiko kematian, serta mengembangkan kondisi kesehatan tertentu, seperti :\n
            -Diabetes tipe 2.\n
            -Kolestrol LDL Tinggi, Kolestrol HDL rendah, atau kadar lipid darah yang tidak sehat.\n
            -Stroke.\n
            -Penyakit Jantung Empedu.\n
            -Sleepanea dan masalah pernapasan.\n
            -Kanker.\n
            -Peradangan Kronis dan dan masalah peningkatan stres oksidatif. ''')
            st.write(''' Saran : Jika ingin menurunkan berat badan, ketahui dulu berapa banyak kalori yang anda butuhkan per hari untuk menjalankan fungsi dasar tubuh dan aktivitas sehari hari. Penting juga untuk mengetahui bagaimana kondisi kesehatan anda saat ini, karena hal ini memengaruhi perhitungan kalori harian.
Selanjutnya, lihat label informasi nilai gizi pada produk, catat berapa kalori yang akan dikonsumsi. Sesuaikan dengan jumlah kalori yang sudah di kurangi sebelumnya dari total kebutuhan kalori harian. Konsumsi makanan dan minuman dengan kandungan kalori yang lebih sedikit dari kebutuhan harian.
Misalnya, jika kebutuhan asupan kalori anda 2.100 kkal per hari, usahakan untuk mengurangi jumlahnya sekitar 300-500 kkal. Biasanya anda akan di anjurkan untuk mengurangi kalori harian sebsanyak 5-15% dari kebutuhan sebelumnya. Hal ini tergantung kondisi kesehatan dan kemmapuan tubuh anda.
Program menurunkan berat badan ini harus dilakukkan bertahap dengan kondisi tubuh. ''')
        elif IMT > 29.9 :
            st.error(f'Anda obesitas tingkat 2, \nIMT {nama} adalah {IMT}')
            st.write(''' Resiko : Orang dengan obesitas tingkat 2 akan memgalami beberapa resiko penyakit seperti : \n
            -Penyakit jantung dan pembuluh darah. \n
            -Diabetes tipe 2. \n
            -Tekanan darah tinggi (hipertensi). \n
            -Gangguan pernapasan. \n
            -Kanker. ''')
            st.write(''' Saran : Konsultasikan dengan dokter atau ahli gizi mengenai jumlah kalori dan nutrisi yang dibutuhkan, Mulailah dengan mengubah pola hidup dan juga pola makan agar lebih teratur, Mulailah beraktivtas fisik sesuai dengan kemampuan anda, Jangan lupa juga untuk meminta dukungan kepada orang sekitar seperti dari keluarga, teman atau bakan sebuah kelompok dukungan agar anda tetap termotivasi dan bertanggung jawab atas gaya hidup anda. ''')

if navbar == 'Cek Kadar Gula Darah' :
    st.title('CEK KADAR GULA DARAH')
    search = st.text_input('  ', placeholder='cari sesuai kata kunci')
    st.image('keyword.jpg', width=500)
    if st.button('CARI') :
        if search.lower() == 'anak usia dibawah 6 tahun' :
            col1, col2 = st.columns(2)
            with col1 :
                st.subheader('Tabel Rentang Kadar Gula Darah')
                st.image('rentang1.jpg', width=300)
            with col2 :
                st.subheader('Penjelasan')
                st.write(''' Anak-anak di bawah usia 6 tahun harus memiliki kadar glukosa darah di kisaran 80-200 mg/dL setiap hari. Angka tersebut terbilang sehat dan jumlah glukosanya bisa berfluktuasi saat bangun tidur, makan, hingga sebelum tidur.''')
        if search.lower() == 'anak usia 6-12 tahun' :
            col1, col2 = st.columns(2)
            with col1 :
                st.subheader('Tabel Rentang Gula Darah')
                st.image('rentang2.jpg', width=300)
            with col2 :
                st.subheader('Penjelasan')
                st.write(''' Pada rentang usia ini, kadar gula darah normal harus di kisaran 80-180 mg/dL per hari. Kadar gula darah dapat naik setelah makan akibat tubuh perlu memecah glukosa yang akhirnya menyebar ke seluruh aliran darah.''')
        if search.lower() == 'anak usia 13-19 tahun' :
            col1, col2 = st.columns(2)
            with col1 :
                st.subheader('Tabel Rentang Gula Darah')
                st.image('rentang3.jpg', width=300)
            with col2 :
                st.subheader('Penjelasan')
                st.write(''' Kadar gula darah normal menurut usia 13-19 tahun berada di kisaran 70-150 mg/dL per hari. Remaja dengan kondisi gula darah tinggi perlu rutin memeriksa kadar gula darah, dan memperhatikan makanannya serta rutin berolahraga.''')
        if search.lower() == 'usia diatas 20 tahun' :
            col1, col2 = st.columns(2)
            with col1 :
                    st.subheader('Tabel Rentang Gula Darah')
                    st.image('rentang4.jpg', width=300)
            with col2 :
                    st.subheader('Penjelasan')
                    st.write(''' Seseorang dengan usia di atas 20 tahun memiliki kadar gula darah normal di kisaran 100-180 mg/dL per hari. Saat bangun di pagi hari, gula darah harus berada di titik terendah karena tubuh belum makan selama sekitar 8 jam. \n
Kategori kadar gula rendah adalah saat angka pemeriksaannya kurang dari 100 mg/dL. Sudah memasuki kategori berbahaya jika angkanya di bawah 70 mg/dL. ''')
        if search.lower() == 'lansia' :
            col1, col2 = st.columns(2)
            with col1 :
                st.subheader('Tabel Rentang Gula Darah')
                st.image('rentang5.jpg', width=300)
            with col2 :
                st.subheader('Penjelasan')
                st.write(''' Orang yang berusia di atas 50 tahun memiliki kadar gula darah normal yang berbeda dengan usia lain. \n
Kadar gula darah pada lansia dianggap tinggi jika mencapai level 120-180 mg/dL 4-8 jam setelah makan. Dan masuk kategori rendah jika kadarnya 60-80 mg/dL di rentang waktu yang sama. ''')