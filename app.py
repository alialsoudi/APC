import streamlit as st

# تنسيقات CSS مخصصة
st.markdown(
    """
    <style>
    body {
        font-family: sans-serif; /* تغيير نوع الخط */
        background-color: #f0f0f0; /* تغيير لون الخلفية */
    }
    .main .block-container {
        max-width: 800px; /* تحديد عرض أقصى للحاوية الرئيسية */
        padding-top: 3rem; /* إضافة مساحة أعلى الحاوية */
        padding-bottom: 3rem; /* إضافة مساحة أسفل الحاوية */
    }
    .stButton>button {
        background-color: #4CAF50; /* تغيير لون زر "احسب" */
        color: white; /* تغيير لون نص زر "احسب" */
    }
    .stTextInput, .stNumberInput {
        margin-bottom: 1rem; /* إضافة مساحة أسفل مربعات الإدخال */
    }
    </style>
    """,
    unsafe_allow_html=True,
)

# عنوان التطبيق مع توسيط النص
st.title("حاسبة كمية البوتاس المتبقية")

# حاوية لمربعات الإدخال مع توسيط المحتوى
col1, col2, col3 = st.columns([1, 2, 1])
with col2:
    loading_rate = st.number_input("معدل التحميل (طن/ساعة):", min_value=0.0, step=0.1)
    location = st.number_input("الموقع (متر):", min_value=0.0, step=1.0)

    if st.button("احسب"):
        if loading_rate > 0 and location > 0:
            BELT_SPEED = 2.75
            POTASH_DENSITY = 1500

            loading_rate_kg_per_sec = loading_rate * 1000 / 3600
            cross_sectional_area = loading_rate_kg_per_sec / (POTASH_DENSITY * BELT_SPEED)
            remaining_potash_volume = cross_sectional_area * location
            remaining_potash_mass = remaining_potash_volume * POTASH_DENSITY
            remaining_potash_tons = remaining_potash_mass / 1000

            st.write(f"كمية البوتاس المتبقية: {remaining_potash_tons:.2f} طن")
        else:
            st.error("الرجاء إدخال قيم صحيحة لمعدل التحميل والموقع.")

# حقوق الملكية مع توسيط النص
st.markdown(
    """
    <div style="text-align: center; font-size: 14px; color: gray;">
        جميع الحقوق محفوظة &copy; 2025 علي السعودي
    </div>
    """,
    unsafe_allow_html=True,
)
