from calculation import calculate_shipping_fee

def test_cal_shipping_fee_01():
    weight_unit = 'Kilograms'
    weight = 10
    distance_unit = 'Kilometers'
    distance = 100
    selected_method = 'Standard'

    fee = calculate_shipping_fee(weight_unit, weight, distance_unit, distance, selected_method)
    assert f'{fee:.2f}' == '11.00'

def test_cal_shipping_fee_02():
    weight_unit = 'Kilograms'
    weight = 10
    distance_unit = 'Kilometers'
    distance = 100
    selected_method = 'Express'

    fee = calculate_shipping_fee(weight_unit, weight, distance_unit, distance, selected_method)
    assert f'{fee:.2f}' == '16.00'

def test_cal_shipping_fee_03():
    weight_unit = 'Kilograms'
    weight = 0
    distance_unit = 'Kilometers'
    distance = 100
    selected_method = 'Express'
    try:
        fee = calculate_shipping_fee(weight_unit, weight, distance_unit, distance, selected_method)
        assert False
    except ValueError as e:
        assert str(e) == 'Weight must be greater than 0'

def test_cal_shipping_fee_04():
    weight_unit = 'Kilograms'
    weight = 'Ten'
    distance_unit = 'Kilometers'
    distance = 100
    selected_method = 'Express'
    try:
        fee = calculate_shipping_fee(weight_unit, weight, distance_unit, distance, selected_method)
        assert False
    except ValueError as e:
        assert str(e) == 'Invalid weight number'

def test_cal_shipping_fee_05():
    try:
        shipping_method = calculate_shipping_fee('Pounds', 10, 'Miles', 20, '')
        assert False
    except ValueError as e:
        assert str(e) == 'shipping_method can not be empty'