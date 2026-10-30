---
title: Concevoir le coupon
lead: Chaque programme a sa propre conception de coupon, avec un titre, un sous-titre et des logos.
---
<ol class="steps">
{% call step() %}Sur le tableau de bord, ouvrez **{{ app.voucher_design_title }}** et choisissez le programme.{% endcall %}
{% call step() %}Remplissez le **{{ app.voucher_title_label }}** et le **{{ app.voucher_subtitle_label }}**. Appuyez sur Entrée dans le sous-titre pour une deuxième ligne.{% endcall %}
{% call step() %}Sous **{{ app.voucher_logos_label }}**, appuyez sur **{{ app.voucher_logo_upload }}** pour ajouter un logo à gauche ou à droite, et choisissez sa taille : S, M ou L. Un PNG avec un fond transparent donne le meilleur résultat.{% endcall %}
{% call step() %}Désactivez **{{ app.voucher_show_qr }}** uniquement si les coupons de ce programme n’ont pas besoin de code QR.{% endcall %}
{% call step("voucher-design", "Voucher design screen with the live preview, and Save design highlighted") %}Vérifiez l’**{{ app.voucher_live_preview }}**, qui montre le coupon à sa taille d’impression (A5 paysage), puis appuyez sur **{{ app.voucher_save_design }}**.{% endcall %}
</ol>
