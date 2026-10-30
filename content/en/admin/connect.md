---
title: Connecting KoboToolbox and programs
lead: Do this once for each new program, so distribution staff can see it and photos can be shown.
---
<ol class="steps">
{% call step("admin-login", "Administrator login") %}Open 121 Scan, tap **{{ app.home_admin }}** and log in with your 121 username and password.{% endcall %}
{% call step("admin-dashboard", "Admin dashboard with System Configuration highlighted") %}On the dashboard, open **{{ app.config_system }}**.{% endcall %}
{% call step("kobo-token", "KoboToolbox section with Verify token highlighted") %}Under KoboToolbox, choose the **Kobo Server** your forms are on. Paste the **{{ app.kobo_api_token }}** and tap **{{ app.verify_token }}**. You find the token in KoboToolbox under *Account settings → Security → API token*. When it works, the screen shows *{{ app.token_linked_to }}* and the Kobo account name.{% endcall %}
{% call step("kobo-programs", "121 Platform section with Add program highlighted") %}Under 121 Platform, tap **+ Add program**. Choose the program and enter its **Kobo Asset ID**: the ID of the KoboToolbox form that registered the program’s people. When the ID is right, the row shows *✓ Connected to* and the form name.{% endcall %}
{% call step() %}Add any other programs the same way, then tap **{{ app.save }}**.{% endcall %}
</ol>

{% call note() %}Distribution staff see every program listed here, so only add programs that use 121 Scan. The connection to 121 itself is set up by 510, not on this screen.{% endcall %}
