---
title: ربط KoboToolbox والبرامج
lead: قم بذلك مرة واحدة لكل برنامج جديد، حتى يراه موظفو التوزيع وتظهر الصور.
---
<ol class="steps">
{% call step("admin-login", "Administrator login") %}افتح 121 Scan، واضغط **{{ app.home_admin }}**، وسجّل الدخول باسم المستخدم وكلمة المرور الخاصين بك في 121.{% endcall %}
{% call step("admin-dashboard", "Admin dashboard with System Configuration highlighted") %}في لوحة التحكم، افتح **{{ app.config_system }}**.{% endcall %}
{% call step("kobo-token", "KoboToolbox section with Verify token highlighted") %}في قسم KoboToolbox، اختر **Kobo Server** الذي توجد عليه نماذجك. الصق **{{ app.kobo_api_token }}** واضغط **{{ app.verify_token }}**. تجد الرمز في KoboToolbox ضمن *Account settings → Security → API token*. عند النجاح، تعرض الشاشة *{{ app.token_linked_to }}* واسم حساب Kobo.{% endcall %}
{% call step("kobo-programs", "121 Platform section with Add program highlighted") %}في قسم 121 Platform، اضغط **+ Add program**. اختر البرنامج وأدخل **Kobo Asset ID** الخاص به، وهو معرّف نموذج KoboToolbox الذي سُجّل به أشخاص البرنامج. عندما يكون المعرّف صحيحًا، يعرض السطر *✓ Connected to* واسم النموذج.{% endcall %}
{% call step() %}أضف البرامج الأخرى بالطريقة نفسها، ثم اضغط **{{ app.save }}**.{% endcall %}
</ol>

{% call note() %}يرى موظفو التوزيع كل البرامج المدرجة هنا، لذلك لا تضف إلا البرامج التي تستخدم 121 Scan. أما الاتصال بنظام 121 نفسه فيُعدّه فريق 510، وليس من هذه الشاشة.{% endcall %}
