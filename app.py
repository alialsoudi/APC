import streamlit as st

st.title("حاسبة كمية البوتاس المتبقية")

# التطبيق الرئيسي
loading_rate_str = st.text_input("معدل التحميل (طن/ساعة):")
location_input_str = st.text_input("الموقع (متر):")

if st.button("احسب"):
    if loading_rate_str and location_input_str:  # Check if both inputs are filled
        try:
            loading_rate = float(loading_rate_str)
            location_input = float(location_input_str)
            location = location_input + 100  # Add 100 to the location

            if loading_rate > 0 and location_input > 0:
                BELT_SPEED = 2.75
                POTASH_DENSITY = 1500

                loading_rate_kg_per_sec = loading_rate * 1000 / 3600
                cross_sectional_area = loading_rate_kg_per_sec / (POTASH_DENSITY * BELT_SPEED)
                remaining_potash_volume = cross_sectional_area * location
                remaining_potash_mass = remaining_potash_volume * POTASH_DENSITY
                remaining_potash_tons = remaining_potash_mass / 1000

                st.write(f"كمية البوتاس المتبقية: {remaining_potash_tons:.2f} طن")
            else:
                st.error("الرجاء إدخال قيم صحيحة لمعدل التحميل والموقع (أكبر من صفر).")

        except ValueError:
            st.error("الرجاء إدخال أرقام صحيحة.")
    else:
        st.error("الرجاء إدخال قيم لمعدل التحميل والموقع.")

# زر للانتقال إلى صفحة المطور
if st.button("صفحة المطور"):
    st.session_state.page = "developer"  # تخزين حالة الصفحة في session_state
    st.experimental_rerun()  # إعادة تشغيل التطبيق لعرض الصفحة الجديدة
