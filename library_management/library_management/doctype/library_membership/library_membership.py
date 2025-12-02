# Copyright (c) 2025, Abhu and contributors
# For license information, please see license.txt

import frappe
from frappe.model.document import Document
from frappe.model.docstatus import DocStatus


class LibraryMembership(Document):
    def before_submit(self):
        # Check if there is already an active membership for this member
        exists = frappe.db.exists(
            "Library Membership",
            {
                "library_member": self.library_member,
                "docstatus": DocStatus.submitted(),
                # check if the membership's end date is later than this membership's start date
                "to_date": (">", self.from_date),
            },
        )
        if exists:
            frappe.throw("There is an active membership for this member")

        # Set membership end date based on loan period in settings
        loan_period = frappe.db.get_single_value("Library Setting", "loan_period")
        self.to_date = frappe.utils.add_days(self.from_date, loan_period or 30)
