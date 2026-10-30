---
title: مسح رمز شخص
lead: كيف تمسح القسيمة، وتتحقق من الشخص، وتسجّل الدفعة.
---
<ol class="steps">
{% call step("program-scan", "Program screen with the Scan button highlighted") %}في شاشة البرنامج، اضغط **Scan**.{% endcall %}
{% call step("start-camera", "Scan screen with the Start camera button highlighted") %}اضغط **{{ app.start_camera }}**. إذا طلب الهاتف استخدام الكاميرا، اسمح بذلك.{% endcall %}
{% call step("scan-camera", "Scan screen with the camera pointed at a voucher") %}وجّه الكاميرا نحو رمز QR على القسيمة وثبّت الهاتف. تُفتح بيانات الشخص تلقائيًا.{% endcall %}
{% call step("beneficiary", "Beneficiary screen showing a photo and details") %}قارن الصورة والبيانات بالشخص الموجود أمامك.{% endcall %}
{% call step("select-payment", "Beneficiary screen with the payment list highlighted") %}إذا كان للشخص أكثر من دفعة، اختر الدفعة التي تسلّمها من **{{ app.select_payment }}**.{% endcall %}
{% call step("approve-skip", "Beneficiary screen with the Approve and Skip buttons highlighted") %}اضغط **{{ app.payment_approved }}** عندما تسلّم الدفعة. اضغط **{{ app.payment_rejected }}** إذا كنت لن تسلّمها الآن.{% endcall %}
{% call step("success", "Success screen with the Scan next beneficiary button highlighted") %}اضغط **{{ app.scan_next }}** للانتقال إلى الشخص التالي.{% endcall %}
</ol>

{% call note() %}الضغط على **{{ app.payment_approved }}** يحفظ الدفعة على هذا الهاتف فقط. تصل إلى 121 عندما تضغط **Send** في شاشة البرنامج مع وجود إنترنت. أما **{{ app.payment_rejected }}** فلا يحفظ شيئًا، لذلك يمكنك مسح رمز الشخص مرة أخرى لاحقًا.{% endcall %}

إذا لم يُقرأ رمز QR، راجع [عندما لا يُقرأ رمز QR](@staff/code-wont-scan).
