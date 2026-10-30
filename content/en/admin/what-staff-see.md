---
title: Choosing what staff see
lead: Choose the details shown next to the photo during a scan, and how staff find people without a QR code.
---
<ol class="steps">
{% call step() %}On the dashboard, open **{{ app.config_title }}** and choose the program under **{{ app.program_id }}**. Everything on this screen applies to that program only.{% endcall %}
{% call step("fields-list", "Displayed fields with Add Field highlighted") %}Under **{{ app.fields_section_title }}**, tap **+ {{ app.add_field }}** and choose a **{{ app.field_name_121 }}**, such as the person’s name. The labels in English, French and Arabic fill in by themselves; change them if needed. These details appear next to the photo when someone is scanned.{% endcall %}
{% call step("fields-editable", "Displayed fields with the Editable column highlighted") %}Turn on **{{ app.editable }}** for a field that staff fill in during the scan, such as a card number. What they type is sent to 121 with the payment. Phone number and reference ID cannot be changed this way.{% endcall %}
{% call step("fields-lower", "Photo, scan method and lookup settings") %}Under **{{ app.photo_config_title }}**, turn on **{{ app.enable_photo_field }}** and choose the **{{ app.field_key }}**: the photo question in the KoboToolbox form.{% endcall %}
{% call step() %}Leave **{{ app.enable_qr_scan }}** on, unless the program does not use QR codes. When it is off, staff always type a code.{% endcall %}
{% call step() %}**{{ app.lookup_field_label }}** sets what staff type when a QR code can’t be used. The default is the reference ID printed on the voucher. If you choose another field, the screen checks whether it is unique. People who share a value cannot be found by it, so staff must use their reference ID.{% endcall %}
{% call step() %}Tap **{{ app.save }}**. Phones get the changes the next time staff tap **Sync**.{% endcall %}
</ol>

{% call note() %}Staff only see editable fields if their 121 role lets them update registrations and payments. See [Staff roles and what they can do](@admin/staff-roles).{% endcall %}
