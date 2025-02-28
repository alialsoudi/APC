import streamlit as st

st.title("حاسبة كمية البوتاس المتبقية")

# خانات إدخال لجميع المعطيات مع قيم افتراضية
POTASH_DENSITY = st.number_input("كثافة البوتاس (كجم/متر مكعب):", value=1500.0, step=1.0)
loading_rate = st.number_input("معدل التحميل (طن/ساعة):", value=1500.0, step=1.0)
location_input = st.number_input("الموقع (متر):", value=250.0, step=1.0)
BELT_SPEED = st.number_input("سرعة القشاط (متر/ثانية):", value=2.75, step=0.01)

if st.button("احسب"):
    location = location_input + 100

    if loading_rate > 0 and location_input > 0 and BELT_SPEED > 0 and POTASH_DENSITY > 0:
        loading_rate_kg_per_sec = loading_rate * 1000 / 3600
        cross_sectional_area = loading_rate_kg_per_sec / (POTASH_DENSITY * BELT_SPEED)
        remaining_potash_volume = cross_sectional_area * location
        remaining_potash_mass = remaining_potash_volume * POTASH_DENSITY
        remaining_potash_tons = remaining_potash_mass / 1000

        st.write(f"كمية البوتاس المتبقية: {remaining_potash_tons:.2f} طن")
    else:
        st.error("الرجاء إدخال قيم صحيحة (أكبر من صفر).")

# حقوق الملكية
st.markdown(
    """
    <div style="text-align: center; font-size: 14px; color: gray;">
        جميع الحقوق محفوظة &copy; 2025 علي السعودي
    </div>
    """,
    unsafe_allow_html=True,
)
