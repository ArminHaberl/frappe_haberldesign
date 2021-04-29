import frappe

@frappe.whitelist()
def some_function():
    doc = frappe.get_doc({
	"doctype": "Project",
	"title": "My new project",
	"status": "Open"
    })
    doc.insert()