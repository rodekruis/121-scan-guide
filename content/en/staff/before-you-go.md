---
title: Before you go
lead: Get the phone ready while you still have internet. Log in, download the people for your program, and save the screens for offline use.
---
<ol class="steps">
{% call step("staff-home", "Home screen with the Distribution Staff button highlighted") %}Open 121 Scan and tap **{{ app.home_fsp }}**.{% endcall %}
{% call step("staff-login", "Distribution staff login with a username typed in") %}Log in with your own 121 username and password.{% endcall %}
{% call step("program-list", "Program list") %}Under **{{ app.program_select_title }}**, choose the program you are distributing for.{% endcall %}
{% call step("program-top", "Program screen top: status box showing Online, and the Sync button highlighted") %}Check that the box at the top says **{{ app.status_online }}**.{% endcall %}
{% call step("sync-progress", "Sync in progress") %}Tap **Sync** and wait. The box shows each stage. A large program can take several minutes. If you close or refresh the screen, the sync carries on.{% endcall %}
{% call step("sync-done", "Sync finished, with Ready to scan and Last synced visible") %}When it finishes, check that **{{ app.beneficiaries_ready_to_scan | label }}** shows the number of people you expect, and **{{ app.last_synced | label }}** shows today.{% endcall %}
{% call step() %}Tap **Scan** once, then go back. This saves the scan screens on the phone, so they work without internet.{% endcall %}
</ol>

{% call note() %}Only people with a payment still waiting in 121 are downloaded. If someone is missing, check their payment in 121 and sync again. If a sync fails, the people from your last successful sync stay on the phone.{% endcall %}

## Working without internet

You can scan without internet. The box at the top of the program screen shows one of three states:

- **{{ app.status_online }}**: the phone has internet.
- **{{ app.status_offline }}**: the phone cannot reach the server. A short drop in signal does not change this.
- **{{ app.status_offline_mode }}**: you chose to work offline.

**Sync** and **Send** only work when the box says **{{ app.status_online }}**.

<ol class="steps">
{% call step("offline-mode", "Program screen in Offline mode, with Go back online highlighted") %}To work offline on purpose, tap **{{ app.work_offline }}**. The box then says **{{ app.status_offline_mode }}**. Tap **{{ app.go_back_online }}** to use the internet again.{% endcall %}
</ol>
