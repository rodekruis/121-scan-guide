---
title: Scanning someone
lead: How to scan a voucher, check the person and record the payment.
---
<ol class="steps">
{% call step("program-scan", "Program screen with the Scan button highlighted") %}On the program screen, tap **Scan**.{% endcall %}
{% call step("start-camera", "Scan screen with the Start camera button highlighted") %}Tap **{{ app.start_camera }}**. If your phone asks to use the camera, allow it.{% endcall %}
{% call step("scan-camera", "Scan screen with the camera pointed at a voucher") %}Point the camera at the QR code on the voucher and hold the phone steady. The person’s details open by themselves.{% endcall %}
{% call step("beneficiary", "Beneficiary screen showing a photo and details") %}Compare the photo and details with the person in front of you.{% endcall %}
{% call step("select-payment", "Beneficiary screen with the payment list highlighted") %}If the person has more than one payment, choose the one you are handing over under **{{ app.select_payment }}**.{% endcall %}
{% call step("approve-skip", "Beneficiary screen with the Approve and Skip buttons highlighted") %}Tap **{{ app.payment_approved }}** when you hand over the payment. Tap **{{ app.payment_rejected }}** if you are not handing it over now.{% endcall %}
{% call step("success", "Success screen with the Scan next beneficiary button highlighted") %}Tap **{{ app.scan_next }}** to continue with the next person.{% endcall %}
</ol>

{% call note() %}**{{ app.payment_approved }}** saves the payment on this phone only. It reaches 121 when you tap **Send** on the program screen with internet. **{{ app.payment_rejected }}** saves nothing, so you can scan the person again later.{% endcall %}

If the QR code will not scan, see [When a QR code won’t scan](@staff/code-wont-scan).
