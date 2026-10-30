---
title: When a QR code won’t scan
lead: Use this if the code is blurred, faded or damaged, or the camera won’t start.
---
<ol class="steps">
{% call step("cant-scan-button", "Scan screen with the Can't scan QR? button highlighted") %}On the scan screen, tap **{{ app.no_qr_btn }}**.{% endcall %}
{% call step("manual-entry", "Manual entry box with a partly typed code and the one-match hint") %}Type the Reference ID printed under the QR code. You can type just the first {{ facts.min_prefix }} characters. You have typed enough when the box says: *{{ app.lookup_one }}*{% endcall %}
{% call step("manual-go", "Manual entry box with the Go button highlighted") %}Tap **{{ app.manual_submit }}**, then check the photo matches the person.{% endcall %}
</ol>

{% call note() %}Some programs also let you find a person by another value, such as their name or ID number. The box is then labelled with that field. You can type that value in full, exactly as it was registered, or the Reference ID as above. If QR scanning is switched off for your program, you always type the code.{% endcall %}
