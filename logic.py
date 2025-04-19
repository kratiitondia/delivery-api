def calculate_minimum_cost(order):
    centers = {
        "C1": {"A": 3, "B": 2, "C": 8},
        "C2": {"D": 12, "E": 25, "F": 15},
        "C3": {"G": 0.5, "H": 1, "I": 2}
    }

    distances = {
        ("C1", "L1"): 3,
        ("C2", "L1"): 2.5,
        ("C3", "L1"): 2
    }

    center_orders = {"C1": {}, "C2": {}, "C3": {}}
    weights = {"C1": 0, "C2": 0, "C3": 0}

    for product, qty in order.items():
        for center in centers:
            if product in centers[center]:
                center_orders[center][product] = qty
                weights[center] += centers[center][product] * qty
                break

    total_cost = 0
    delivery_legs = 0

    for center in ["C1", "C2", "C3"]:
        if weights[center] > 0:
            delivery_legs += 1
            dist = distances[(center, "L1")]
            total_cost += compute_leg_cost(weights[center], dist)

    # Add drop surcharge only if multiple delivery legs
    if delivery_legs > 1:
        total_cost += delivery_legs * 10
    return round(total_cost)

def compute_leg_cost(weight, distance):
    if weight <= 5:
        rate = 10
    else:
        rate = 10 + 8 * ((weight - 1) // 5)
    return distance * rate
