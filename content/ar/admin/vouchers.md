---
title: طباعة القسائم
lead: حوّل قائمة الأشخاص من 121 إلى قسائم برموز QR جاهزة للطباعة.
---
<ol class="steps">
{% call step() %}في 121، صدّر قائمة المدفوعات للبرنامج كملف CSV أو Excel. يجب أن يحتوي الملف على عمود للمعرّف المرجعي باسم *referenceId* أو *reference id* أو *reference_id* أو *refid* أو *id*.{% endcall %}
{% call step("vouchers-upload", "Voucher generator with the file area highlighted") %}في لوحة التحكم، افتح **{{ app.generate_vouchers }}** واختر **{{ app.program }}** في الأعلى. اضغط **{{ app.choose_csv }}** لاختيار الملف، ثم **{{ app.upload_csv }}**.{% endcall %}
{% call step() %}إذا لم يكن للبرنامج تصميم بعد، تعرض الشاشة *{{ app.voucher_design_incomplete_title }}*. اضغط **{{ app.voucher_design_go }}** وأكمل [تصميم القسيمة](@admin/voucher-design) أولًا.{% endcall %}
{% call step("vouchers-fields", "Fields on the voucher list highlighted") %}في **{{ app.voucher_fields_title }}**، اختر ما يُطبع. اسحب الحقل، أو استخدم أسهمه، لتغيير الترتيب. اضغط على الاسم لتغيير طريقة طباعته. أوقف الحقل حتى لا يظهر على القسيمة. تُحفظ هذه الخيارات للبرنامج.{% endcall %}
{% call step("vouchers-download", "Download vouchers (PDF) highlighted") %}اضغط **{{ app.download_vouchers }}**. كل قسيمة بحجم A5 أفقي، ويحمل رمز QR الخاص بها المعرّف المرجعي للشخص.{% endcall %}
</ol>

{% call note() %}راجع بعض القسائم المطبوعة قبل التوزيع. عندما يتعذر مسح رمز QR، يكتب الموظفون المعرّف المرجعي المطبوع أسفله.{% endcall %}
