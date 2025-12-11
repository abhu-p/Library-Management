import frappe
from frappe.utils import getdate

# ----------------------------
# Validate and calculate numbers
# ----------------------------
def validate_numbers(doc, method):
    """
    Calculate sum_of_the_numbers on validate
    """
    doc.sum_of_the_numbers = (doc.first_number or 0) + (doc.second_number or 0)


def update_numbers_on_submit(doc, method):
    """
    Calculate sum_of_the_numbers on submit and save to database
    """
    doc.sum_of_the_numbers = (doc.first_number or 0) + (doc.second_number or 0)
    doc.db_update()


# ----------------------------
# Fiscal year helper
# ----------------------------
@frappe.whitelist()
def get_fiscal_year_from_date(date):
    """
    Returns Fiscal Year name for a given date
    """
    date = getdate(date)
    fy = frappe.db.get_value(
        "Fiscal Year",
        {"year_start_date": ("<=", date), "year_end_date": (">=", date)},
        "name"
    )
    return fy


#sales invoice grand total amount


def calculate_custom_total(doc, method):
    
    custom_g_total = 0
    
    if doc.items:
        for item in doc.items:
            
            custom_g_total += (item.qty or 0) * (item.rate or 0) * 0.85
    
    
    doc.custom_grand_total_amount = custom_g_total