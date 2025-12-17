/*
frappe.ui.form.on('Check', {
    onload: function(frm) {
        make_company_fields_read_only(frm);
    },
    refresh: function(frm) {
        make_company_fields_read_only(frm);
    }
});

function make_company_fields_read_only(frm) {
    if (!frm.is_new()) {
        ['company', 'custom_company'].forEach(function(field) {
            if (frm.fields_dict[field]) {
                frm.set_df_property(field, 'read_only', 1);
                frm.refresh_field(field); // This ensures the field becomes greyed out
            }
        });
    }
}
    */