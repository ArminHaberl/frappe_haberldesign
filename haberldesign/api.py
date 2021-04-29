import frappe

@frappe.whitelist()
def some_function():
    doc = frappe.get_doc({
	"doctype": "Uploads",
	"email": "test@test.at"
    })
    doc.insert()