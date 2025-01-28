import frappe

def distribute_freight_cost(doc, event):
    """
    Distribute freight cost across items in the Purchase Order.
    """
    if doc.custom_freight_amount:
        total_rows = len(doc.items)
        if total_rows > 0:
            freight_cost_per_row = doc.custom_freight_amount / total_rows

            for item in doc.items:
                if item.qty and item.qty > 0:
                    item.custom_freight_cost = freight_cost_per_row
                    item.custom_qty_freight = round(freight_cost_per_row / item.qty, 2)



@frappe.whitelist()
def calculate_custom_g_total(doc, method):
    if isinstance(doc, str):  # Check if `doc` is passed as a JSON string
        doc = frappe.parse_json(doc)
    freight_amount = float(doc.get("custom_freight_amount", 0) or 0)  # Convert to float
    total = float(doc.get("total", 0) or 0)  # Convert to float
    doc.custom_g_total = freight_amount + total

