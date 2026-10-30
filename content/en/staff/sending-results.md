---
title: Sending results to 121
lead: Approved payments stay on the phone until you send them. Send them as soon as you have internet.
---
<ol class="steps">
{% call step("program-send", "Program screen lower part with Payments ready to send, and the Send button highlighted") %}With internet, open the program screen. **{{ app.payments_ready_send | label }}** shows how many approved payments are waiting. Tap **Send**.{% endcall %}
{% call step("sent-done", "Program screen after sending: count back to zero and Last submission showing the time") %}When it works, the count goes back to zero and **{{ app.last_payments_submit | label }}** shows the time.{% endcall %}
</ol>

{% call note() %}If sending fails, the screen says why, and the payments stay on the phone. Try again later. Do not clear the browser’s data or uninstall the app while payments are waiting, because that deletes them.{% endcall %}

If you don’t see the send section, your 121 account cannot record payments. Ask your administrator.
