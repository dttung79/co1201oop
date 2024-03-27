shipping_methods = {
    'Standard': 5.0,
    'Express': 10.0,
    'Priority': 15.0
}

def calculate_shipping_fee(weight_unit, weight, distance_unit, distance, selected_method):
    if weight <= 0:
        raise ValueError('Weight must be greater than 0')
    if distance <= 0:
        raise ValueError('Distance must be greater than 0')
    
    # Adjust weight based on the selected unit
    if weight_unit == 'Pounds':
        weight *= 0.45  # Convert pounds to kilograms
    
    # Adjust distance based on the selected unit
    if distance_unit == 'Miles':
        distance *= 1.61
    
    # Calculate the total shipping cost based on weight, distance, and the shipping method cost
    total_cost = (weight * 0.1) + (distance * 0.05) + shipping_methods[selected_method]

    return total_cost