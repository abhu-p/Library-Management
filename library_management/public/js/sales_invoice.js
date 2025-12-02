frappe.ui.form.on('Sales Invoice', {

    // Number sum trigger
    first_number: function(frm) {
        update_sum(frm);
    },
    second_number: function(frm) {
        update_sum(frm);
    },

    // Name concatenation trigger
    first_name: function(frm) {
        update_full_name(frm);
    },
    last_name: function(frm) {
        update_full_name(frm);
    }

});

// Helper function for sum
function update_sum(frm) {
    frm.set_value('sum_of_the_numbers', 
        (frm.doc.first_number || 0) + (frm.doc.second_number || 0)
    );
}

// Helper function for full name
function update_full_name(frm) {
    frm.set_value('full_name', 
        ((frm.doc.first_name || '') + ' ' + (frm.doc.last_name || '')).trim()
    );
}


frappe.ui.form.on("Sales Invoice", {

    // When the page loads
    onload: function(frm){
        if(frm.doc.posting_date){
            frappe.call({
                method: "library_management.library_management.sales_invoice.get_fiscal_year_from_date",
                args: { date: frm.doc.posting_date },
                callback: function(r){
                    if(r.message){
                        frm.set_value("custom_fiscal_year", r.message);
                    }
                }
            });
        }
    },

    // When user edits posting_date
    posting_date: function(frm){
        if(frm.doc.posting_date){
            frappe.call({
                method: "library_management.library_management.sales_invoice.get_fiscal_year_from_date",
                args: { date: frm.doc.posting_date },
                callback: function(r){
                    if(r.message){
                        frm.set_value("custom_fiscal_year", r.message);
                    }
                }
            });
        }
    }

});


