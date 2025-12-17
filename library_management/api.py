'''import frappe

@frappe.whitelist()
def save_partners(names):
    """
    Save list of partner names into Partner DocType
    """
    if isinstance(names, str):
        import json
        names = json.loads(names)

    for name in names:
        doc = frappe.new_doc("Partner")
        doc.name1 = name
        doc.insert()

    frappe.db.commit()
    return "OK"
'''