---
title: Quand un code QR ne se lit pas
lead: À utiliser si le code est flou, effacé ou abîmé, ou si la caméra ne démarre pas.
---
<ol class="steps">
{% call step("cant-scan-button", "Scan screen with the Can't scan QR? button highlighted") %}Sur l’écran de scan, appuyez sur **{{ app.no_qr_btn }}**.{% endcall %}
{% call step("manual-entry", "Manual entry box with a partly typed code and the one-match hint") %}Tapez l’identifiant de référence (Reference ID) imprimé sous le code QR. Les {{ facts.min_prefix }} premiers caractères suffisent. Vous en avez tapé assez quand la case indique : *{{ app.lookup_one }}*{% endcall %}
{% call step("manual-go", "Manual entry box with the Go button highlighted") %}Appuyez sur **{{ app.manual_submit }}**, puis vérifiez que la photo correspond à la personne.{% endcall %}
</ol>

{% call note() %}Certains programmes permettent aussi de retrouver une personne par une autre information, comme son nom ou son numéro d’identité. La case porte alors le nom de ce champ. Vous pouvez taper cette information en entier, exactement comme lors de l’enregistrement, ou l’identifiant de référence comme ci-dessus. Si le scan des codes QR est désactivé pour votre programme, vous tapez toujours le code.{% endcall %}
