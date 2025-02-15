import streamlit as st

# تضمين أنماط CSS مخصصة
st.markdown(
    """
    <style>
    body {
        background-color: #f4f4f4; /* لون الخلفية */
        font-family: sans-serif; /* نوع الخط */
    }

    .stTextInput, .stNumberInput, .stButton {
        margin-bottom: 10px; /* تباعد بين العناصر */
    }

    .stButton>button {
        background-color: #007bff; /* لون زر "احسب" */
        color: white; /* لون نص زر "احسب" */
    }

    .stAlert {
        color: red; /* لون رسائل الخطأ */
    }
    </style>
    """,
    unsafe_allow_html=True,
)

st.title("حاسبة كمية البوتاس")

loading_rate = st.number_input("معدل التحميل (طن/ساعة):", min_value=0.0)
location_input = st.number_input("الموقع (متر):", min_value=0.0)

if st.button("احسب"):
    try:
        if loading_rate > 0 and location_input > 0:
            location = location_input + 100  # إضافة 100 إلى قيمة الموقع
            loading_rate_kg_per_sec = loading_rate * 1000 / 3600
            cross_sectional_area = loading_rate_kg_per_sec / (1500 * 2.75)
            remaining_potash_volume = cross_sectional_area * location
            remaining_potash_mass = remaining_potash_volume * 1500

            remaining_potash_tons = remaining_potash_mass / 1000
            st.write(f"كمية البوتاس المتبقية: {remaining_potash_tons:.2f} طن")
        else:
            st.error("خطأ: يجب أن تكون جميع القيم المدخلة موجبة.")

    except ValueError:
        st.error("خطأ: يرجى إدخال أرقام صحيحة.")