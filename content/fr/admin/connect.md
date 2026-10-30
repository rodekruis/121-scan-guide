---
title: Connecter KoboToolbox et les programmes
lead: À faire une fois pour chaque nouveau programme, pour que le personnel de distribution le voie et que les photos s’affichent.
---
<ol class="steps">
{% call step("admin-login", "Administrator login") %}Ouvrez 121 Scan, appuyez sur **{{ app.home_admin }}** et connectez-vous avec votre nom d’utilisateur et mot de passe 121.{% endcall %}
{% call step("admin-dashboard", "Admin dashboard with System Configuration highlighted") %}Sur le tableau de bord, ouvrez **{{ app.config_system }}**.{% endcall %}
{% call step("kobo-token", "KoboToolbox section with Verify token highlighted") %}Sous KoboToolbox, choisissez le **Kobo Server** où se trouvent vos formulaires. Collez le **{{ app.kobo_api_token }}** et appuyez sur **{{ app.verify_token }}**. Le jeton se trouve dans KoboToolbox sous *Account settings → Security → API token*. Quand cela fonctionne, l’écran affiche *{{ app.token_linked_to }}* et le nom du compte Kobo.{% endcall %}
{% call step("kobo-programs", "121 Platform section with Add program highlighted") %}Sous 121 Platform, appuyez sur **+ Add program**. Choisissez le programme et saisissez son **Kobo Asset ID** : l’identifiant du formulaire KoboToolbox qui a enregistré les personnes du programme. Quand l’identifiant est correct, la ligne affiche *✓ Connected to* et le nom du formulaire.{% endcall %}
{% call step() %}Ajoutez les autres programmes de la même façon, puis appuyez sur **{{ app.save }}**.{% endcall %}
</ol>

{% call note() %}Le personnel de distribution voit tous les programmes listés ici : n’ajoutez que les programmes qui utilisent 121 Scan. La connexion à 121 elle-même est configurée par 510, pas sur cet écran.{% endcall %}
