---
title: Avant de partir
lead: Préparez le téléphone tant que vous avez internet. Connectez-vous, téléchargez les personnes de votre programme et enregistrez les écrans pour une utilisation hors ligne.
---
<ol class="steps">
{% call step("staff-home", "Home screen with the Distribution Staff button highlighted") %}Ouvrez 121 Scan et appuyez sur **{{ app.home_fsp }}**.{% endcall %}
{% call step("staff-login", "Distribution staff login with a username typed in") %}Connectez-vous avec votre propre nom d’utilisateur et mot de passe 121.{% endcall %}
{% call step("program-list", "Program list") %}Sous **{{ app.program_select_title }}**, choisissez le programme pour lequel vous distribuez.{% endcall %}
{% call step("program-top", "Program screen top: status box showing Online, and the Sync button highlighted") %}Vérifiez que la case en haut indique **{{ app.status_online }}**.{% endcall %}
{% call step("sync-progress", "Sync in progress") %}Appuyez sur **Sync** et patientez. La case affiche chaque étape. Un grand programme peut prendre plusieurs minutes. Si vous fermez ou actualisez l’écran, la synchronisation continue.{% endcall %}
{% call step("sync-done", "Sync finished, with Ready to scan and Last synced visible") %}Quand elle est terminée, vérifiez que **{{ app.beneficiaries_ready_to_scan | label }}** indique le nombre de personnes attendu et que **{{ app.last_synced | label }}** indique la date du jour.{% endcall %}
{% call step() %}Appuyez une fois sur **Scan**, puis revenez en arrière. Les écrans de scan sont ainsi enregistrés sur le téléphone et fonctionnent sans internet.{% endcall %}
</ol>

{% call note() %}Seules les personnes ayant un paiement encore en attente dans 121 sont téléchargées. S’il manque quelqu’un, vérifiez son paiement dans 121 et synchronisez à nouveau. Si une synchronisation échoue, les personnes de votre dernière synchronisation réussie restent sur le téléphone.{% endcall %}

## Travailler sans internet

Vous pouvez scanner sans internet. La case en haut de l’écran du programme indique l’un de ces trois états :

- **{{ app.status_online }}** : le téléphone a internet.
- **{{ app.status_offline }}** : le téléphone ne peut pas joindre le serveur. Une courte perte de signal ne change pas cet état.
- **{{ app.status_offline_mode }}** : vous avez choisi de travailler hors ligne.

**Sync** et **Send** fonctionnent uniquement quand la case indique **{{ app.status_online }}**.

<ol class="steps">
{% call step("offline-mode", "Program screen in Offline mode, with Go back online highlighted") %}Pour travailler hors ligne volontairement, appuyez sur **{{ app.work_offline }}**. La case indique alors **{{ app.status_offline_mode }}**. Appuyez sur **{{ app.go_back_online }}** pour utiliser à nouveau internet.{% endcall %}
</ol>
