---
title: Printing vouchers
lead: Turn the list of people from 121 into QR vouchers, ready to print.
---
<ol class="steps">
{% call step() %}In 121, export the payment list for the program as a CSV or Excel file. It needs a reference ID column, named *referenceId*, *reference id*, *reference_id*, *refid* or *id*.{% endcall %}
{% call step("vouchers-upload", "Voucher generator with the file area highlighted") %}On the dashboard, open **{{ app.generate_vouchers }}** and choose the **{{ app.program }}** at the top. Tap **{{ app.choose_csv }}** to pick the file, then **{{ app.upload_csv }}**.{% endcall %}
{% call step() %}If the program has no design yet, the screen says *{{ app.voucher_design_incomplete_title }}*. Tap **{{ app.voucher_design_go }}** and finish [Designing the voucher](@admin/voucher-design) first.{% endcall %}
{% call step("vouchers-fields", "Fields on the voucher list highlighted") %}Under **{{ app.voucher_fields_title }}**, choose what is printed. Drag a field, or use its arrows, to change the order. Tap a name to change how it is printed. Switch a field off to leave it off the voucher. This is saved for the program.{% endcall %}
{% call step("vouchers-download", "Download vouchers (PDF) highlighted") %}Tap **{{ app.download_vouchers }}**. Each voucher is A5 landscape, and its QR code holds the person’s reference ID.{% endcall %}
</ol>

{% call note() %}Check a few printed vouchers before the distribution. When a QR code won’t scan, staff type the reference ID printed under it.{% endcall %}
