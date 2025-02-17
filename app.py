import streamlit as st  # استيراد مكتبة Streamlit، وهي مكتبة بايثون تُستخدم لإنشاء تطبيقات ويب تفاعلية بسهولة.

st.title("كمية البوتاس المتبقية")  # عرض عنوان التطبيق في أعلى الصفحة.

# استخدام st.text_input بدلاً من st.number_input للسماح بإدخال قيم فارغة
loading_rate_str = st.text_input("معدل التحميل (طن/ساعة):")  # مربع نصي لإدخال معدل التحميل.
location_input_str = st.text_input("الموقع (متر):")  # مربع نصي لإدخال الموقع.

if st.button("احسب"):  # زر "احسب"، عند الضغط عليه سيتم تنفيذ الكود التالي.
    try:  # محاولة تنفيذ الكود التالي، وفي حالة حدوث خطأ سيتم الانتقال إلى الجزء الخاص بالتعامل مع الأخطاء.
        if loading_rate_str and location_input_str:  # التحقق من أن القيم المدخلة (معدل التحميل والموقع) ليست فارغة.
            loading_rate = float(loading_rate_str)  # تحويل قيمة معدل التحميل إلى رقم عشري (float).
            location_input = float(location_input_str)  # تحويل قيمة الموقع إلى رقم عشري (float).

            if loading_rate > 0 and location_input > 0:  # التحقق من أن القيم المدخلة (معدل التحميل والموقع) أكبر من صفر.
                BELT_SPEED = 2.75  # سرعة القشاط (متر/ثانية). ثابت، ولا يتغير.
                POTASH_DENSITY = 1500  # كثافة البوتاس (كجم/متر مكعب). ثابت، ولا يتغير.

                location = location_input + 100  # إضافة 100 إلى قيمة "الموقع" المُدخلة.
                loading_rate_kg_per_sec = loading_rate * 1000 / 3600  # تحويل معدل التحميل من (طن/ساعة) إلى (كجم/ثانية).
                cross_sectional_area = loading_rate_kg_per_sec / (POTASH_DENSITY * BELT_SPEED)  # حساب مساحة المقطع العرضي.
                remaining_potash_volume = cross_sectional_area * location  # حساب حجم البوتاس المتبقي.
                remaining_potash_mass = remaining_potash_volume * POTASH_DENSITY  # حساب كتلة البوتاس المتبقية.

                remaining_potash_tons = remaining_potash_mass / 1000  # تحويل كتلة البوتاس المتبقية من (كجم) إلى (طن).
                st.write(f"كمية البوتاس المتبقية: {remaining_potash_tons:.2f} طن")  # عرض النتيجة النهائية.
            else:  # إذا لم يكن الشرط if صحيحاً، سيتم تنفيذ هذا الكود.
                st.error("خطأ: يجب أن تكون جميع القيم المدخلة موجبة.")  # عرض رسالة خطأ للمستخدم.

        else:  # إذا لم يتم إدخال قيم لمعدل التحميل والموقع.
            st.error("خطأ: يرجى إدخال قيم لمعدل التحميل والموقع.")  # عرض رسالة خطأ للمستخدم.

    except ValueError:  # يتم تنفيذ هذا الكود إذا حدث خطأ من نوع ValueError (عادةً عند إدخال نص بدلاً من رقم).
        st.error("خطأ: يرجى إدخال أرقام صحيحة.")  # عرض رسالة خطأ للمستخدم.
