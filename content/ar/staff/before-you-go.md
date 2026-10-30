---
title: قبل التوجّه إلى التوزيع
lead: جهّز الهاتف ما دام الإنترنت متاحًا. سجّل الدخول، ونزّل قائمة الأشخاص في برنامجك، واحفظ الشاشات لاستخدامها دون اتصال.
---
<ol class="steps">
{% call step("staff-home", "Home screen with the Distribution Staff button highlighted") %}افتح 121 Scan واضغط **{{ app.home_fsp }}**.{% endcall %}
{% call step("staff-login", "Distribution staff login with a username typed in") %}سجّل الدخول باسم المستخدم وكلمة المرور الخاصين بك في 121.{% endcall %}
{% call step("program-list", "Program list") %}من **{{ app.program_select_title }}**، اختر البرنامج الذي توزّع له.{% endcall %}
{% call step("program-top", "Program screen top: status box showing Online, and the Sync button highlighted") %}تأكد من أن المربع في أعلى الشاشة يعرض **{{ app.status_online }}**.{% endcall %}
{% call step("sync-progress", "Sync in progress") %}اضغط **Sync** وانتظر. يعرض المربع كل مرحلة. قد يستغرق البرنامج الكبير عدة دقائق. إذا أغلقت الشاشة أو حدّثتها، تستمر المزامنة.{% endcall %}
{% call step("sync-done", "Sync finished, with Ready to scan and Last synced visible") %}عند انتهائها، تأكد من أن **{{ app.beneficiaries_ready_to_scan | label }}** يعرض عدد الأشخاص المتوقع، وأن **{{ app.last_synced | label }}** يعرض تاريخ اليوم.{% endcall %}
{% call step() %}اضغط **Scan** مرة واحدة ثم ارجع. بذلك تُحفظ شاشات المسح على الهاتف وتعمل دون إنترنت.{% endcall %}
</ol>

{% call note() %}لا يُنزَّل إلا الأشخاص الذين لديهم دفعة ما زالت في الانتظار في 121. إذا كان أحدهم غير موجود، تحقق من دفعته في 121 ثم أعد المزامنة. إذا فشلت المزامنة، يبقى على الهاتف الأشخاص من آخر مزامنة ناجحة.{% endcall %}

## العمل دون إنترنت

يمكنك المسح دون إنترنت. يعرض المربع في أعلى شاشة البرنامج إحدى ثلاث حالات:

- **{{ app.status_online }}**: الهاتف متصل بالإنترنت.
- **{{ app.status_offline }}**: لا يستطيع الهاتف الوصول إلى الخادم. الانقطاع القصير في الإشارة لا يغيّر هذه الحالة.
- **{{ app.status_offline_mode }}**: اخترت العمل دون اتصال.

لا يعمل **Sync** و**Send** إلا عندما يعرض المربع **{{ app.status_online }}**.

<ol class="steps">
{% call step("offline-mode", "Program screen in Offline mode, with Go back online highlighted") %}للعمل دون اتصال عن قصد، اضغط **{{ app.work_offline }}**. يعرض المربع عندها **{{ app.status_offline_mode }}**. اضغط **{{ app.go_back_online }}** لاستخدام الإنترنت مرة أخرى.{% endcall %}
</ol>
