# Copyright (c) 2025, Abhu and contributors
# For license information, please see license.txt


import frappe
from frappe.model.document import Document
from frappe.model.naming import make_autoname

class CustomerData(Document):   
    def autoname(self):
        auto_no = make_autoname(".####")
        self.name = f"{self.customer}-{self.place}-{auto_no}"
