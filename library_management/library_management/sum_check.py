import frappe

def calculate_c(doc, method):
   
    a = doc.a or 0
    b = doc.b or 0
    doc.c = a + b
