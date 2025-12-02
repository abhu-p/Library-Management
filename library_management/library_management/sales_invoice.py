import frappe
from frappe.utils import getdate

def validate_numbers(doc, method):
    doc.sum_of_the_numbers = (doc.first_number or 0) + (doc.second_number or 0)

def update_numbers_on_submit(doc, method):
    doc.sum_of_the_numbers = (doc.first_number or 0) + (doc.second_number or 0)
    doc.db_update()





@frappe.whitelist()
def get_fiscal_year_from_date(date):
    
    date = getdate(date)
    fy = frappe.db.get_value(
        "Fiscal Year",
        {"year_start_date": ("<=", date), "year_end_date": (">=", date)},
        "name"
    )
    return fy
