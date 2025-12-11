frappe.ui.form.on('Sales Invoice', {

    // --- Number sum triggers ---
    first_number: function(frm) {
        update_sum(frm);
    },
    second_number: function(frm) {
        update_sum(frm);
    },

    // --- Name concatenation triggers ---
    first_name: function(frm) {
        update_full_name(frm);
    },
    last_name: function(frm) {
        update_full_name(frm);
    },

    // --- Posting date triggers for fiscal year ---
    onload: function(frm){
        update_fiscal_year(frm);
    },
    posting_date: function(frm){
        update_fiscal_year(frm);
    },

    // --- Child table triggers ---
    item_add: function(frm, cdt, cdn){
        update_child_total(frm, cdt, cdn);
    },
    item_remove: function(frm, cdt, cdn){
        calculate_grand_total(frm);
    }

});

// --- Helper functions ---

// Sum of numbers
function update_sum(frm) {
    frm.set_value('sum_of_the_numbers', 
        (frm.doc.first_number || 0) + (frm.doc.second_number || 0)
    );
}

// Full name
function update_full_name(frm) {
    frm.set_value('full_name', 
        ((frm.doc.first_name || '') + ' ' + (frm.doc.last_name || '')).trim()
    );
}

// Fiscal year from posting date
function update_fiscal_year(frm){
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



//sales invoice grand total amount


frappe.ui.form.on('Sales Invoice', {
    refresh: function(frm) {
        calculate_custom_grand_total(frm);
    },
    
    onload: function(frm) {
        calculate_custom_grand_total(frm);
    },
    
    before_save: function(frm) {
        calculate_custom_grand_total(frm);
    },
    
    validate: function(frm) {
        calculate_custom_grand_total(frm);
    }
});

frappe.ui.form.on('Sales Invoice Item', {
    qty: function(frm, cdt, cdn) {
        calculate_custom_grand_total(frm);
    },
    
    rate: function(frm, cdt, cdn) {
        calculate_custom_grand_total(frm);
    },
    
    items_remove: function(frm) {
        calculate_custom_grand_total(frm);
    },
    
    items_add: function(frm) {
        calculate_custom_grand_total(frm);
    }
});

function calculate_custom_grand_total(frm) {
    let custom_g_total = 0;
    
    if (frm.doc.items && frm.doc.items.length > 0) {
        frm.doc.items.forEach(function(item) {
            // Formula: qty * rate * 0.85
            custom_g_total += (item.qty || 0) * (item.rate || 0) * 0.85;
        });
    }
    
    // Set in custom_grand_total_amount field
    frm.set_value('custom_grand_total_amount', custom_g_total);
}