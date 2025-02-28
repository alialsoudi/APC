import streamlit as st

st.title("حاسبة كمية البوتاس المتبقية")

# خانات إدخال لجميع المعطيات - فارغة
loading_rate_str = st.text_input("معدل التحميل (طن/ساعة):")
location_input_str = st.text_input("الموقع (متر):")
BELT_SPEED_str = st.text_input("سرعة القشاط (متر/ثانية):")
POTASH_DENSITY_str = st.text_input("كثافة البوتاس (كجم/متر مكعب):")

if st.button("احسب"):
    # التحقق من أن جميع الخانات ليست فارغة
    if loading_rate_str and location_input_str and BELT_SPEED_str and POTASH_DENSITY_str:
        try:
            # تحويل القيم المدخلة إلى أرقام
            loading_rate = float(loading_rate_str)
            location_input = float(location_input_str)
            BELT_SPEED = float(BELT_SPEED_str)
            POTASH_DENSITY = float(POTASH_DENSITY_str)

            location = location_input + 100  # إضافة 100 إلى الموقع

            if loading_rate > 0 and location_input > 0 and BELT_SPEED > 0 and POTASH_DENSITY > 0:
                loading_rate_kg_per_sec = loading_rate * 1000 / 3600
                cross_sectional_area = loading_rate_kg_per_sec / (POTASH_DENSITY * BELT_SPEED)
                remaining_potash_volume = cross_sectional_area * location
                remaining_potash_mass = remaining_potash_volume * POTASH_DENSITY
                remaining_potash_tons = remaining_potash_mass / 1000

                st.write(f"كمية البوتاس المتبقية: {remaining_potash_tons:.2f} طن")
            else:
                st.error("الرجاء إدخال قيم صحيحة (أكبر من صفر).")

        except ValueError:
            st.error("الرجاء إدخال أرقام صحيحة.")
    else:
        st.error("الرجاء إدخال جميع القيم.")

# حقوق الملكية
st.markdown(
    """
    <div style="text-align: center; font-size: 14px; color: gray;">
        جميع الحقوق محفوظة &copy; 2025 علي السعودي
    </div>
    """,
    unsafe_allow_html=True,
)
