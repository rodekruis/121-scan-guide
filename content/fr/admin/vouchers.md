---
title: Imprimer les coupons
lead: Transformez la liste des personnes de 121 en coupons avec code QR, prêts à imprimer.
---
<ol class="steps">
{% call step() %}Dans 121, exportez la liste des paiements du programme en fichier CSV ou Excel. Il faut une colonne d’identifiant de référence, nommée *referenceId*, *reference id*, *reference_id*, *refid* ou *id*.{% endcall %}
{% call step("vouchers-upload", "Voucher generator with the file area highlighted") %}Sur le tableau de bord, ouvrez **{{ app.generate_vouchers }}** et choisissez le **{{ app.program }}** en haut. Appuyez sur **{{ app.choose_csv }}** pour choisir le fichier, puis sur **{{ app.upload_csv }}**.{% endcall %}
{% call step() %}Si le programme n’a pas encore de conception, l’écran indique *{{ app.voucher_design_incomplete_title }}*. Appuyez sur **{{ app.voucher_design_go }}** et terminez d’abord [Concevoir le coupon](@admin/voucher-design).{% endcall %}
{% call step("vouchers-fields", "Fields on the voucher list highlighted") %}Sous **{{ app.voucher_fields_title }}**, choisissez ce qui est imprimé. Faites glisser un champ, ou utilisez ses flèches, pour changer l’ordre. Appuyez sur un nom pour changer la façon dont il est imprimé. Désactivez un champ pour qu’il ne figure pas sur le coupon. Ces choix sont enregistrés pour le programme.{% endcall %}
{% call step("vouchers-download", "Download vouchers (PDF) highlighted") %}Appuyez sur **{{ app.download_vouchers }}**. Chaque coupon est au format A5 paysage, et son code QR contient l’identifiant de référence de la personne.{% endcall %}
</ol>

{% call note() %}Vérifiez quelques coupons imprimés avant la distribution. Quand un code QR ne se lit pas, le personnel tape l’identifiant de référence imprimé en dessous.{% endcall %}
