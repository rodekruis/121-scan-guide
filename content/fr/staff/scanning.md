---
title: Scanner une personne
lead: Comment scanner un coupon, vérifier la personne et enregistrer le paiement.
---
<ol class="steps">
{% call step("program-scan", "Program screen with the Scan button highlighted") %}Sur l’écran du programme, appuyez sur **Scan**.{% endcall %}
{% call step("start-camera", "Scan screen with the Start camera button highlighted") %}Appuyez sur **{{ app.start_camera }}**. Si le téléphone demande l’accès à la caméra, autorisez-le.{% endcall %}
{% call step("scan-camera", "Scan screen with the camera pointed at a voucher") %}Pointez la caméra vers le code QR du coupon et tenez le téléphone immobile. Les informations de la personne s’ouvrent automatiquement.{% endcall %}
{% call step("beneficiary", "Beneficiary screen showing a photo and details") %}Comparez la photo et les informations avec la personne en face de vous.{% endcall %}
{% call step("select-payment", "Beneficiary screen with the payment list highlighted") %}Si la personne a plus d’un paiement, choisissez celui que vous remettez sous **{{ app.select_payment }}**.{% endcall %}
{% call step("approve-skip", "Beneficiary screen with the Approve and Skip buttons highlighted") %}Appuyez sur **{{ app.payment_approved }}** quand vous remettez le paiement. Appuyez sur **{{ app.payment_rejected }}** si vous ne le remettez pas maintenant.{% endcall %}
{% call step("success", "Success screen with the Scan next beneficiary button highlighted") %}Appuyez sur **{{ app.scan_next }}** pour passer à la personne suivante.{% endcall %}
</ol>

{% call note() %}**{{ app.payment_approved }}** enregistre le paiement sur ce téléphone uniquement. Il arrive dans 121 quand vous appuyez sur **Send** sur l’écran du programme, avec internet. **{{ app.payment_rejected }}** n’enregistre rien : vous pourrez scanner la personne à nouveau plus tard.{% endcall %}

Si le code QR ne se lit pas, consultez [Quand un code QR ne se lit pas](@staff/code-wont-scan).
