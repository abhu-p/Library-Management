frappe.ui.form.on('Student Result', {
    a(frm) {
        frm.set_value('c', (frm.doc.a || 0) + (frm.doc.b || 0));
    },
    b(frm) {
        frm.set_value('c', (frm.doc.a || 0) + (frm.doc.b || 0));
    }
});
