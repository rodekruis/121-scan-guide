---
title: إرسال النتائج إلى 121
lead: تبقى المدفوعات التي تمت الموافقة عليها على الهاتف إلى أن ترسلها. أرسلها فور توفر الإنترنت.
---
<ol class="steps">
{% call step("program-send", "Program screen lower part with Payments ready to send, and the Send button highlighted") %}افتح شاشة البرنامج مع وجود إنترنت. يعرض **{{ app.payments_ready_send | label }}** عدد المدفوعات الموافق عليها التي تنتظر الإرسال. اضغط **Send**.{% endcall %}
{% call step("sent-done", "Program screen after sending: count back to zero and Last submission showing the time") %}عند نجاح الإرسال يعود العدد إلى صفر، ويعرض **{{ app.last_payments_submit | label }}** الوقت.{% endcall %}
</ol>

{% call note() %}إذا فشل الإرسال، تعرض الشاشة السبب وتبقى المدفوعات على الهاتف. حاول مرة أخرى لاحقًا. لا تمسح بيانات المتصفح ولا تحذف التطبيق ما دامت هناك مدفوعات تنتظر الإرسال، لأن ذلك يحذفها.{% endcall %}

إذا لم يظهر لك قسم الإرسال، فإن حسابك في 121 لا يستطيع تسجيل المدفوعات. اسأل المسؤول.
