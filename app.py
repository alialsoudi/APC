import streamlit as st  # استيراد مكتبة Streamlit، وهي مكتبة بايثون تُستخدم لإنشاء تطبيقات ويب تفاعلية بسهولة.

# عنوان التطبيق
st.title("كمية البوتاس")  # عرض عنوان التطبيق في أعلى الصفحة.
# مربعات الإدخال
loading_rate = st.number_input("معدل التحميل (طن/ساعة):", min_value=0.0)  # إنشاء مربع إدخال رقمي لـ "معدل التحميل".
# number_input: يُستخدم لإدخال أرقام عشرية.
# min_value=0.0: يعني أن الحد الأدنى للقيمة المُدخلة هو 0.0.

location_input = st.number_input("الموقع (متر):", min_value=0.0)  # إنشاء مربع إدخال رقمي لـ "الموقع".

# زر الحساب
if st.button("احسب"):  # إنشاء زر باسم "احسب"،  وسيتم تنفيذ الكود التالي عند الضغط عليه.
    try:  # try:  يستخدم لمحاولة تنفيذ كود معين، وإذا حدث خطأ سيتم الانتقال إلى except.
        if loading_rate > 0 and location_input > 0:  # التحقق من أن القيم المُدخلة (معدل التحميل والموقع) أكبر من صفر.
            BELT_SPEED = 2.75  # سرعة القشاط (متر/ثانية).  ثابت، ولا يتغير.
            POTASH_DENSITY = 1500  # كثافة البوتاس (كجم/متر مكعب). ثابت، ولا يتغير.

            location = location_input + 100  # إضافة 100 إلى قيمة "الموقع" المُدخلة.
            loading_rate_kg_per_sec = loading_rate * 1000 / 3600  # تحويل معدل التحميل من (طن/ساعة) إلى (كجم/ثانية).
            cross_sectional_area = loading_rate_kg_per_sec / (POTASH_DENSITY * BELT_SPEED)  # حساب مساحة المقطع العرضي.
            remaining_potash_volume = cross_sectional_area * location  # حساب حجم البوتاس المتبقي.
            remaining_potash_mass = remaining_potash_volume * POTASH_DENSITY  # حساب كتلة البوتاس المتبقية.

            remaining_potash_tons = remaining_potash_mass / 1000  # تحويل كتلة البوتاس المتبقية من (كجم) إلى (طن).
            st.write(f"كمية البوتاس المتبقية: {remaining_potash_tons:.2f} طن")  # عرض النتيجة النهائية.
        else:  # else:  إذا لم يكن الشرط if صحيحاً، سيتم تنفيذ هذا الكود.
            st.error("خطأ: يجب أن تكون جميع القيم المدخلة موجبة.")  # عرض رسالة خطأ للمستخدم.

    except ValueError:  # except:  يتم تنفيذ هذا الكود إذا حدث خطأ من نوع ValueError (عادةً عند إدخال نص بدلاً من رقم).
        st.error("خطأ: يرجى إدخال أرقام صحيحة.")  # عرض رسالة خطأ للمستخدم.
