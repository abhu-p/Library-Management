import frappe
import json

@frappe.whitelist()
def get_partners():
    """Get all partners from the database"""
    try:
        partners = frappe.get_all("Partner", fields=["name", "name1"], order_by="creation desc")
        frappe.log_error(f"Fetched {len(partners)} partners", "Get Partners Debug")
        return partners
    except Exception as e:
        frappe.log_error(f"Error in get_partners: {str(e)}", "Get Partners Error")
        return []

@frappe.whitelist()
def save_partners(partners):
    """Save multiple new partners"""
    try:
        # Parse JSON string if needed
        if isinstance(partners, str):
            partners = json.loads(partners)
        
        count = 0
        errors = []
        
        for idx, item in enumerate(partners, start=1):
            name = item.get('name1', '').strip()
            if not name:
                errors.append(f"Partner {idx} name is empty.")
                continue
            
            try:
                # Check if partner already exists
                if frappe.db.exists("Partner", {"name1": name}):
                    errors.append(f"Partner '{name}' already exists.")
                    continue
                
                doc = frappe.get_doc({
                    "doctype": "Partner",
                    "name1": name
                })
                doc.insert(ignore_permissions=True)
                count += 1
                frappe.log_error(f"Created partner: {name}", "Save Partner Debug")
            except Exception as e:
                errors.append(f"Error saving partner '{name}': {str(e)}")
                frappe.log_error(f"Error saving partner '{name}': {str(e)}", "Save Partner Error")
        
        frappe.db.commit()
        
        if errors:
            return {
                "success": True if count > 0 else False,
                "count": count,
                "error": "; ".join(errors)
            }
        
        return {"success": True, "count": count}
        
    except Exception as e:
        frappe.log_error(f"Error in save_partners: {str(e)}", "Save Partners Error")
        frappe.db.rollback()
        return {"success": False, "error": str(e)}

@frappe.whitelist()
def update_partner(partner_id, new_name):
    """Update an existing partner's name"""
    try:
        new_name = new_name.strip()
        
        if not new_name:
            return {"success": False, "error": "Name cannot be empty."}
        
        # Check if partner exists
        if not frappe.db.exists("Partner", partner_id):
            frappe.log_error(f"Partner not found: {partner_id}", "Update Partner Error")
            return {"success": False, "error": f"Partner '{partner_id}' not found."}
        
        # Get the document
        doc = frappe.get_doc("Partner", partner_id)
        old_name = doc.name1
        
        # Update the field
        doc.name1 = new_name
        
        # Save with ignore permissions
        doc.save(ignore_permissions=True)
        
        # Commit the transaction
        frappe.db.commit()
        
        frappe.log_error(f"Updated partner {partner_id}: '{old_name}' -> '{new_name}'", "Update Partner Debug")
        
        return {"success": True, "message": f"Updated from '{old_name}' to '{new_name}'"}
        
    except Exception as e:
        frappe.db.rollback()
        error_msg = str(e)
        frappe.log_error(f"Error in update_partner ({partner_id}): {error_msg}", "Update Partner Error")
        return {"success": False, "error": error_msg}

@frappe.whitelist()
def delete_partner(partner_id):
    """Delete a partner"""
    try:
        # Check if partner exists
        if not frappe.db.exists("Partner", partner_id):
            frappe.log_error(f"Partner not found: {partner_id}", "Delete Partner Error")
            return {"success": False, "error": f"Partner '{partner_id}' not found."}
        
        # Get the document
        doc = frappe.get_doc("Partner", partner_id)
        partner_name = doc.name1
        
        # Delete with ignore permissions
        doc.delete(ignore_permissions=True)
        
        # Commit the transaction
        frappe.db.commit()
        
        frappe.log_error(f"Deleted partner: {partner_id} ({partner_name})", "Delete Partner Debug")
        
        return {"success": True, "message": f"Deleted partner '{partner_name}'"}
        
    except Exception as e:
        frappe.db.rollback()
        error_msg = str(e)
        frappe.log_error(f"Error in delete_partner ({partner_id}): {error_msg}", "Delete Partner Error")
        return {"success": False, "error": error_msg}