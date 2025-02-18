import streamlit as st  # استيراد مكتبة Streamlit

# تحديد عنوان التطبيق
st.title("حاسبة كمية البوتاس المتبقية")

# مربع إدخال لمعدل التحميل (طن/ساعة) - فارغ افتراضياً
loading_rate_str = st.text_input("معدل التحميل (طن/ساعة):")

# مربع إدخال للموقع (متر) - فارغ افتراضياً
location_input_str = st.text_input("الموقع (متر):")

# زر "احسب"
if st.button("احسب"):  # عند النقر على الزر

    # التحقق من أن القيم المدخلة صحيحة (ليست فارغة وأكبر من صفر)
    if loading_rate_str and location_input_str:
        try:
            loading_rate = float(loading_rate_str)  # تحويل القيمة إلى رقم عشري
            location_input = float(location_input_str)  # تحويل القيمة إلى رقم عشري
            location = location_input + 100  # إضافة 100 إلى قيمة الموقع

            if loading_rate > 0 and location_input > 0:  # التأكد من أن القيم أكبر من صفر
                BELT_SPEED = 2.75  # سرعة القشاط (متر/ثانية) - قيمة ثابتة
                POTASH_DENSITY = 1500  # كثافة البوتاس (كجم/متر مكعب) - قيمة ثابتة

                # حساب كمية البوتاس المتبقية (العمليات الحسابية)
                loading_rate_kg_per_sec = loading_rate * 1000 / 3600  # تحويل معدل التحميل إلى كجم/ثانية
                cross_sectional_area = loading_rate_kg_per_sec / (POTASH_DENSITY * BELT_SPEED)  # حساب مساحة المقطع العرضي
                remaining_potash_volume = cross_sectional_area * location  # حساب حجم البوتاس المتبقي
                remaining_potash_mass = remaining_potash_volume * POTASH_DENSITY  # حساب كتلة البوتاس المتبقية
                remaining_potash_tons = remaining_potash_mass / 1000  # تحويل الكتلة إلى طن

                # عرض النتيجة
                st.write(f"كمية البوتاس المتبقية: {remaining_potash_tons:.2f} طن")  # عرض النتيجة مع تقريبها لرقمين عشريين

            else:
                # عرض رسالة خطأ إذا كانت القيم المدخلة غير صحيحة (أقل من أو يساوي صفر)
                st.error("الرجاء إدخال قيم صحيحة لمعدل التحميل والموقع (أكبر من صفر).")  # رسالة خطأ للمستخدم

        except ValueError:  # إذا لم يتم إدخال أرقام
            st.error("الرجاء إدخال أرقام صحيحة.")  # رسالة خطأ للمستخدم

    else:
        # عرض رسالة خطأ إذا كانت القيم المدخلة فارغة
        st.error("الرجاء إدخال قيم لمعدل التحميل والموقع.")  # رسالة خطأ للمستخدم

# حقوق الملكية
st.markdown(
    """
    <div style="text-align: center; font-size: 14px; color: gray;">
        جميع الحقوق محفوظة &copy; 2025 علي السعودي
    </div>
    """,
    unsafe_allow_html=True,
)
