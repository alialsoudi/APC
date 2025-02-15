import streamlit as st

st.title("كمية البوتاس")

# مربع إدخال "معدل التحميل"
loading_rate_str = st.text_input("معدل التحميل (طن/ساعة):")  # استخدام st.text_input

# مربع إدخال "الموقع"
location_input_str = st.text_input("الموقع (متر):")  # استخدام st.text_input

if st.button("احسب"):
    try:
        # التحقق من أن القيم المدخلة ليست فارغة
        if loading_rate_str and location_input_str:
            loading_rate = float(loading_rate_str)  # تحويل القيمة إلى float
            location_input = float(location_input_str)  # تحويل القيمة إلى float

            if loading_rate > 0 and location_input > 0:
                BELT_SPEED = 2.75
                POTASH_DENSITY = 1500

                location = location_input + 100
                loading_rate_kg_per_sec = loading_rate * 1000 / 3600
                cross_sectional_area = loading_rate_kg_per_sec / (POTASH_DENSITY * BELT_SPEED)
                remaining_potash_volume = cross_sectional_area * location
                remaining_potash_mass = remaining_potash_volume * POTASH_DENSITY

                remaining_potash_tons = remaining_potash_mass / 1000
                st.write(f"كمية البوتاس المتبقية: {remaining_potash_tons:.2f} طن")
            else:
                st.error("خطأ: يجب أن تكون جميع القيم المدخلة موجبة.")

        else:
            st.error("خطأ: يرجى إدخال قيم لمعدل التحميل والموقع.")  # رسالة خطأ جديدة

    except ValueError:
        st.error("خطأ: يرجى إدخال أرقام صحيحة.")
