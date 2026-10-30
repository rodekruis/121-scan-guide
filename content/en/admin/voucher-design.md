---
title: Designing the voucher
lead: Each program has its own voucher design, with a title, a subtitle and logos.
---
<ol class="steps">
{% call step() %}On the dashboard, open **{{ app.voucher_design_title }}** and choose the program.{% endcall %}
{% call step() %}Fill in the **{{ app.voucher_title_label }}** and **{{ app.voucher_subtitle_label }}**. Press Enter in the subtitle for a second line.{% endcall %}
{% call step() %}Under **{{ app.voucher_logos_label }}**, tap **{{ app.voucher_logo_upload }}** to add a left or right logo, and choose its size: S, M or L. A PNG with a transparent background works best.{% endcall %}
{% call step() %}Turn off **{{ app.voucher_show_qr }}** only if this program’s vouchers don’t need a QR code.{% endcall %}
{% call step("voucher-design", "Voucher design screen with the live preview, and Save design highlighted") %}Check the **{{ app.voucher_live_preview }}**, which shows the voucher at its printed size (A5 landscape), then tap **{{ app.voucher_save_design }}**.{% endcall %}
</ol>
