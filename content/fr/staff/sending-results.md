---
title: Envoyer les résultats à 121
lead: Les paiements approuvés restent sur le téléphone jusqu’à leur envoi. Envoyez-les dès que vous avez internet.
---
<ol class="steps">
{% call step("program-send", "Program screen lower part with Payments ready to send, and the Send button highlighted") %}Avec internet, ouvrez l’écran du programme. **{{ app.payments_ready_send | label }}** indique combien de paiements approuvés attendent. Appuyez sur **Send**.{% endcall %}
{% call step("sent-done", "Program screen after sending: count back to zero and Last submission showing the time") %}Quand l’envoi réussit, le nombre revient à zéro et **{{ app.last_payments_submit | label }}** indique l’heure.{% endcall %}
</ol>

{% call note() %}Si l’envoi échoue, l’écran en indique la raison et les paiements restent sur le téléphone. Réessayez plus tard. N’effacez pas les données du navigateur et ne désinstallez pas l’application tant que des paiements attendent, car cela les supprime.{% endcall %}

Si vous ne voyez pas la partie d’envoi, votre compte 121 ne peut pas enregistrer de paiements. Demandez à votre administrateur.
