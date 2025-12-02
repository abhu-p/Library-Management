import frappe

def execute(filters=None):
    columns = get_columns()
    data = get_customer_data(filters)
    return columns, data

def get_columns():
    return [
        {
            "label": "Name",
            "fieldname": "name",
            "fieldtype": "Link",
            "options": "Customer Data",
            "width": 100
        },
        {
            "label": "Customer",
            "fieldname": "customer",
            "fieldtype": "Data",
            "width": 120
        },
        {
            "label": "Customer Unboard Date",
            "fieldname": "customer_unboard_date",
            "fieldtype": "Date",
            "width": 120
        },
        {
            "label": "Phone",
            "fieldname": "phone_number",
            "fieldtype": "Data",
            "width": 120
        },
        {
            "label": "Gender",
            "fieldname": "gender",
            "fieldtype": "Data",
            "width": 100
        },
        {
            "label": "Place",
            "fieldname": "place",
            "fieldtype": "Data",
            "width": 120
        }
    ]

def get_customer_data(filters=None):
    if not filters:
        filters = {}

    conditions = ""
    values = {}

    # Fiscal Year filter
    fiscal_year_name = filters.get("fiscal_year")
    if fiscal_year_name:
        fy = frappe.get_doc("Fiscal Year", fiscal_year_name)
        if fy.year_start_date and fy.year_end_date:
            conditions += " AND customer_unboard_date BETWEEN %(start)s AND %(end)s "
            values.update({
                "start": fy.year_start_date,
                "end": fy.year_end_date
            })

    query = f"""
        SELECT
            name,
            customer,
            customer_unboard_date,
            phone_number,
            gender,
            place
        FROM `tabCustomer Data`
        WHERE 1=1 {conditions}
        ORDER BY customer_unboard_date DESC
    """

    data = frappe.db.sql(query, values, as_dict=True)
    return data
