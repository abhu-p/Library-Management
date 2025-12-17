'''import frappe
from frappe.model.document import Document

class Check(Document):
    def validate(self):
        self._validate_company_fields()

    def _validate_company_fields(self):
        company_fields = ['company', 'custom_company']
        if not self.is_new():
            old_doc = self.get_doc_before_save()
            if old_doc:
                for field in company_fields:
                    if hasattr(self, field) and getattr(old_doc, field) != getattr(self, field):
                        frappe.throw(f"'{field}' cannot be changed after saving the document.") '''
