---
title: عندما لا يُقرأ رمز QR
lead: استخدم هذه الخطوات إذا كان الرمز غير واضح أو باهتًا أو تالفًا، أو إذا لم تعمل الكاميرا.
---
<ol class="steps">
{% call step("cant-scan-button", "Scan screen with the Can't scan QR? button highlighted") %}في شاشة المسح، اضغط **{{ app.no_qr_btn }}**.{% endcall %}
{% call step("manual-entry", "Manual entry box with a partly typed code and the one-match hint") %}اكتب المعرّف المرجعي المطبوع أسفل رمز QR. يكفي أن تكتب أول {{ facts.min_prefix }} أحرف. يكون ما كتبته كافيًا عندما يعرض المربع: *{{ app.lookup_one }}*{% endcall %}
{% call step("manual-go", "Manual entry box with the Go button highlighted") %}اضغط **{{ app.manual_submit }}**، ثم تأكد من أن الصورة تطابق الشخص.{% endcall %}
</ol>

{% call note() %}تسمح بعض البرامج أيضًا بالعثور على الشخص بقيمة أخرى، مثل اسمه أو رقم هويته. في هذه الحالة يحمل المربع اسم هذا الحقل. يمكنك كتابة هذه القيمة كاملة كما سُجّلت تمامًا، أو كتابة المعرّف المرجعي كما سبق. إذا كان مسح رمز QR متوقفًا في برنامجك، فستكتب الرمز دائمًا.{% endcall %}
