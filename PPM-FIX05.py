import streamlit as st

st.title('Perhitungan Nilai PPM Kesadahan Total')
    
Molaritas = st.number_input('Masukan Nilai Molaritas Titran (mmol/ml)')
Volume1 = st.number_input('Masukan Nilai Volume Titran (ml)')
Nama_BM = st.selectbox('BM (mg/mmol)', ['Pilih BM','BM CaCO3 100 mg/mmol','BM Ca 40 mg/mmol'])
Nilai_BM = st.selectbox('Silahkan Nilai BM (mg/mmol)', ['Pilih Nilai BM',100,40])
FP = st.selectbox('Silahkan Nilai FP', ['Pilih Nilai FP',1,100/50,100/25,250/50,100/10])
Volume2 = st.number_input('Masukan Nilai Volume Sampel (L)')
Hitung = st.button('Hitung Nilai PPM Kesadahan Total')
 
if Hitung:
        Nilai_PPM_Kesadahan_Total = (Molaritas*Volume1*Nilai_BM*FP)/Volume2
        st.success(f'Nilai PPM Kesadahan Total Adalah {Nilai_PPM_Kesadahan_Total} mg/L')