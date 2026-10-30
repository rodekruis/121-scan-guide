---
title: Choisir ce que voit le personnel
lead: Choisissez les informations affichées à côté de la photo pendant un scan, et comment le personnel retrouve une personne sans code QR.
---
<ol class="steps">
{% call step() %}Sur le tableau de bord, ouvrez **{{ app.config_title }}** et choisissez le programme sous **{{ app.program_id }}**. Tout ce qui se trouve sur cet écran s’applique uniquement à ce programme.{% endcall %}
{% call step("fields-list", "Displayed fields with Add Field highlighted") %}Sous **{{ app.fields_section_title }}**, appuyez sur **+ {{ app.add_field }}** et choisissez un **{{ app.field_name_121 }}**, par exemple le nom de la personne. Les libellés en anglais, français et arabe se remplissent automatiquement ; modifiez-les si nécessaire. Ces informations s’affichent à côté de la photo lors d’un scan.{% endcall %}
{% call step("fields-editable", "Displayed fields with the Editable column highlighted") %}Activez **{{ app.editable }}** pour un champ que le personnel remplit pendant le scan, par exemple un numéro de carte. Ce qu’il saisit est envoyé à 121 avec le paiement. Le numéro de téléphone et l’identifiant de référence ne peuvent pas être modifiés ainsi.{% endcall %}
{% call step("fields-lower", "Photo, scan method and lookup settings") %}Sous **{{ app.photo_config_title }}**, activez **{{ app.enable_photo_field }}** et choisissez le **{{ app.field_key }}** : la question photo du formulaire KoboToolbox.{% endcall %}
{% call step() %}Laissez **{{ app.enable_qr_scan }}** activé, sauf si le programme n’utilise pas de codes QR. S’il est désactivé, le personnel tape toujours un code.{% endcall %}
{% call step() %}**{{ app.lookup_field_label }}** définit ce que le personnel tape quand un code QR ne peut pas être utilisé. Par défaut, c’est l’identifiant de référence imprimé sur le coupon. Si vous choisissez un autre champ, l’écran vérifie qu’il est unique. Les personnes qui partagent une même valeur ne peuvent pas être retrouvées par ce champ : le personnel doit alors utiliser leur identifiant de référence.{% endcall %}
{% call step() %}Appuyez sur **{{ app.save }}**. Les téléphones reçoivent les changements la prochaine fois que le personnel appuie sur **Sync**.{% endcall %}
</ol>

{% call note() %}Le personnel ne voit les champs modifiables que si son rôle dans 121 lui permet de mettre à jour les enregistrements et les paiements. Voir [Rôles du personnel et ce qu’ils permettent](@admin/staff-roles).{% endcall %}
