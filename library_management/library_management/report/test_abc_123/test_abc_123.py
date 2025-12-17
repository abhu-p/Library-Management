'''import frappe

def get_columns():
    return [
        {
            "label": "ID",
            "fieldname": "name",
            "fieldtype": "Data",
            "width": 140
        },
        {
            "label": "Title",
            "fieldname": "title",
            "fieldtype": "Data",
            "width": 200
        },
        {
            "label": "Customer",
            "fieldname": "customer",
            "fieldtype": "Link",
            "options": "Customer",
            "width": 200
        },
        {
            "label": "Status",
            "fieldname": "status",
            "fieldtype": "Data",
            "width": 120
        },
        {
            "label": "Grand Total",
            "fieldname": "grand_total",
            "fieldtype": "Currency",
            "width": 140
        }
    ]

def get_data(filters=None):
    if not filters:
        filters = {}

    return frappe.get_all(
        "Sales Invoice",
        fields=[
            "name",
            "title",
            "customer",
            "status",
            "grand_total"
        ],
        filters=filters,
        limit_page_length=50
    )

def execute(filters=None):
    columns = get_columns()
    data = get_data(filters)
    return columns, data
'''