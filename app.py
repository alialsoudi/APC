import streamlit as st
import base64

st.title("كمية البوتاس")

# تحويل الصورة إلى base64 (إذا كنت تستخدم بايثون)
with open("APC_LOGO.jpg", "rb") as image_file:  # افتح الصورة في وضع البايت
    encoded_string = base64.b64encode(image_file.read()).decode()  # قم بتحويلها إلى base64

# عرض الصورة في Streamlit0
st.markdown(
    f"""
    <img src="data:image/png;base64,{encoded_string}" width="200">  """,  # تضمين الصورة في HTML
    unsafe_allow_html=True,
)

loading_rate = st.number_input("معدل التحميل (طن/ساعة):", min_value=0.0)
location_input = st.number_input("الموقع (متر):", min_value=0.0)

if st.button("احسب"):
    try:
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

    except ValueError:
        st.error("خطأ: يرجى إدخال أرقام صحيحة.")
