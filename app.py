import streamlit as st
import pandas as pd
from io import BytesIO
import plotly.express as px

# Style CSS

st.markdown("""
    <style>
        .main {background-color: #f4f6f9;}
        .title-box {
            padding: 25px 20px;
            background: #1f3a5f;
            color: #ffffff;
            border-radius: 8px;
            margin-bottom: 25px;
            text-align: center;
            font-size: 26px;
            font-weight: 600;
        }
        .metric-box {
            padding: 18px;
            background: #ffffff;
            border-radius: 8px;
            border: 1px solid #e0e6ed;
            box-shadow: 0px 2px 5px rgba(0,0,0,0.05);
            text-align: center;
        }
        .metric-title {
            font-size: 15px;
            color: #4a5568;
            margin-bottom: 8px;
        }
        .metric-value {
            font-size: 28px;
            font-weight: 600;
            color: #2d3748;
        }
        .section-title {
            font-size: 20px;
            font-weight: 600;
            color: #2d3748;
            margin-top: 25px;
            margin-bottom: 10px;
        }
    </style>
""", unsafe_allow_html=True)


# PAGE TITLE

st.markdown("<div class='title-box'>Sistem Analisis Data Siswa</div>", unsafe_allow_html=True)

uploaded_file = st.file_uploader("Upload File Excel Siswa", type=["xlsx"])

if uploaded_file:
    df = pd.read_excel(uploaded_file)

    st.markdown("<div class='section-title'>Data Siswa</div>", unsafe_allow_html=True)
    st.dataframe(df, use_container_width=True)


    # ANALISIS DATA

    total = len(df)
    laki = len(df[df['Jenis_Kelamin'] == 'L'])
    perempuan = len(df[df['Jenis_Kelamin'] == 'P'])
    total_tahun = df.groupby("Tahun_Ajaran")["NIS"].count()
    kenaikan = total_tahun.sort_index().diff().fillna(0)

    # METRIC SUMMARY

    st.markdown("<div class='section-title'>Ringkasan Statistik</div>", unsafe_allow_html=True)
    col1, col2, col3 = st.columns(3)
    with col1:
        st.markdown(f"<div class='metric-box'><div class='metric-title'>Total Siswa</div><div class='metric-value'>{total}</div></div>", unsafe_allow_html=True)
    with col2:
        st.markdown(f"<div class='metric-box'><div class='metric-title'>Laki-laki</div><div class='metric-value'>{laki}</div></div>", unsafe_allow_html=True)
    with col3:
        st.markdown(f"<div class='metric-box'><div class='metric-title'>Perempuan</div><div class='metric-value'>{perempuan}</div></div>", unsafe_allow_html=True)

    # TABEL ANALISIS

    st.markdown("<div class='section-title'>Total Siswa per Tahun Ajaran</div>", unsafe_allow_html=True)
    st.table(total_tahun)

    st.markdown("<div class='section-title'>Kenaikan Jumlah Siswa</div>", unsafe_allow_html=True)
    st.table(kenaikan)


    # GRAFIK ANALISIS

    st.markdown("<div class='section-title'>Grafik Analisis Siswa</div>", unsafe_allow_html=True)

    fig1 = px.bar(total_tahun.reset_index(), x="Tahun_Ajaran", y="NIS",
                  labels={"NIS":"Jumlah Siswa", "Tahun_Ajaran":"Tahun Ajaran"},
                  title="Jumlah Siswa per Tahun Ajaran",
                  text_auto=True)
    st.plotly_chart(fig1, use_container_width=True)

    fig2 = px.line(kenaikan.reset_index(), x="Tahun_Ajaran", y="NIS",
                   labels={"NIS":"Kenaikan Siswa", "Tahun_Ajaran":"Tahun Ajaran"},
                   title="Kenaikan Jumlah Siswa per Tahun Ajaran",
                   markers=True)
    st.plotly_chart(fig2, use_container_width=True)

    gender_counts = df["Jenis_Kelamin"].value_counts().reset_index()
    gender_counts.columns = ["Jenis_Kelamin", "Jumlah"]
    fig3 = px.pie(gender_counts, names="Jenis_Kelamin", values="Jumlah",
                  title="Perbandingan Laki-laki dan Perempuan")
    st.plotly_chart(fig3, use_container_width=True)

    # TAB KESIMPULAN
  
    st.markdown("<div class='section-title'>Kesimpulan</div>", unsafe_allow_html=True)
    tab1, tab2, tab3 = st.tabs(["Ringkasan Umum", "Tren Tahunan", "Analisis Gender"])

    with tab1:
        st.write(f"- Total siswa: **{total}** (Laki-laki: {laki}, Perempuan: {perempuan})")
        st.write("- Secara keseluruhan, jumlah siswa menunjukkan data yang konsisten untuk setiap tahun ajaran.")
    
    with tab2:
        for i in range(len(total_tahun)):
            tahun = total_tahun.index[i]
            naik = kenaikan.iloc[i]
            if naik > 0:
                st.write(f"Jumlah siswa pada {tahun} meningkat **{int(naik)}** dibanding tahun sebelumnya.")
            elif naik < 0:
                st.write(f"Jumlah siswa pada {tahun} menurun **{abs(int(naik))}** dibanding tahun sebelumnya.")
            else:
                st.write(f"Jumlah siswa pada {tahun} sama seperti tahun sebelumnya.")

    with tab3:
        if laki > perempuan:
            st.write(f"Laki-laki lebih banyak daripada perempuan (**{laki} vs {perempuan}**).")
        elif perempuan > laki:
            st.write(f"Perempuan lebih banyak daripada laki-laki (**{perempuan} vs {laki}**).")
        else:
            st.write("Jumlah siswa laki-laki dan perempuan seimbang.")
        st.write("Analisis ini membantu memahami distribusi gender dalam setiap angkatan.")

    # DOWNLOAD ANALISIS
   
    output = BytesIO()
    writer = pd.ExcelWriter(output, engine='openpyxl')
    df.to_excel(writer, index=False, sheet_name="Data Siswa")
    total_tahun.to_excel(writer, sheet_name="Total Per Tahun")
    kenaikan.to_excel(writer, sheet_name="Kenaikan")
    writer.close()

    st.download_button(
        label="Download Hasil Analisis (Excel)",
        data=output.getvalue(),
        file_name="hasil_analisis.xlsx",
        mime="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
    )

else:
    st.info("Silakan upload file Excel siswa untuk mulai analisis.")
