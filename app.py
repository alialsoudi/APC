import streamlit as st

st.title(" كمية البوتاس")

loading_rate = st.number_input("معدل التحميل (طن/ساعة):", min_value=0.0)
location_input = st.number_input("الموقع (متر):", min_value=0.0)

if st.button("احسب"):
    try:
        if loading_rate > 0 and location_input > 0:
            BELT_SPEED = 2.75  # سرعة القشاط (متر/ثانية)
            POTASH_DENSITY = 1500  # كثافة البوتاس (كجم/متر مكعب)

            location = location_input + 100  # إضافة 100 إلى قيمة الموقع
            loading_rate_kg_per_sec = loading_rate * 1000 / 3600  # تحويل معدل التحميل إلى كجم/ثانية
            cross_sectional_area = loading_rate_kg_per_sec / (POTASH_DENSITY * BELT_SPEED)  # حساب مساحة المقطع العرضي
            remaining_potash_volume = cross_sectional_area * location  # حساب حجم البوتاس المتبقي
            remaining_potash_mass = remaining_potash_volume * POTASH_DENSITY  # حساب كتلة البوتاس المتبقية

            remaining_potash_tons = remaining_potash_mass / 1000  # تحويل الكتلة إلى طن
            st.write(f"كمية البوتاس المتبقية: {remaining_potash_tons:.2f} طن")
        else:
            st.error("خطأ: يجب أن تكون جميع القيم المدخلة موجبة.")

    except ValueError:
        st.error("خطأ: يرجى إدخال أرقام صحيحة.")
