---
title: تصميم القسيمة
lead: لكل برنامج تصميم قسيمة خاص به، يتضمن عنوانًا وعنوانًا فرعيًا وشعارات.
---
<ol class="steps">
{% call step() %}في لوحة التحكم، افتح **{{ app.voucher_design_title }}** واختر البرنامج.{% endcall %}
{% call step() %}املأ **{{ app.voucher_title_label }}** و**{{ app.voucher_subtitle_label }}**. اضغط Enter في العنوان الفرعي لإضافة سطر ثانٍ.{% endcall %}
{% call step() %}في **{{ app.voucher_logos_label }}**، اضغط **{{ app.voucher_logo_upload }}** لإضافة شعار على اليسار أو اليمين، واختر حجمه: S أو M أو L. تعطي صورة PNG بخلفية شفافة أفضل نتيجة.{% endcall %}
{% call step() %}أوقف **{{ app.voucher_show_qr }}** فقط إذا كانت قسائم هذا البرنامج لا تحتاج إلى رمز QR.{% endcall %}
{% call step("voucher-design", "Voucher design screen with the live preview, and Save design highlighted") %}راجع **{{ app.voucher_live_preview }}** الذي يعرض القسيمة بحجم الطباعة (A5 أفقي)، ثم اضغط **{{ app.voucher_save_design }}**.{% endcall %}
</ol>
