frappe.query_reports["Test ABC 123"] = {
    formatter: function(value, row, column, data, default_formatter) {
        let formatted = default_formatter(value, row, column, data);

        // Right-align Grand Total
        if (column.fieldname === "grand_total") {
            formatted = `<div style="text-align:right; padding:2px;">${value}</div>`;
        }

        // Padding for Customer
        if (column.fieldname === "customer") {
            formatted = `<div style="padding:2px;">${value}</div>`;
        }

        // Padding for Status
        if (column.fieldname === "status") {
            formatted = `<div style="padding:2px;">${value}</div>`;
        }

        // Padding for Invoice ID (name)
        if (column.fieldname === "name") {
            formatted = `<div style="padding:2px;">${value}</div>`;
        }

        return formatted;
    }
};
