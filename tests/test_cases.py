from src.main import calculate_total,apply_coupon,shipping_charge,final_bill

def test_ct():
    assert calculate_total([
    {"name":"Laptop","price":50000,"qty":1},
    {"name":"Mouse","price":1000,"qty":2}
    ]) == 52000
    
    assert calculate_total([]) == 0 
    
    assert calculate_total([
    {"name":"Laptop","price":-50000,"qty":1},
    {"name":"Mouse","price":1000,"qty":2}
    ]) == -1
    
    assert calculate_total([
    {"name":"Laptop","price":50000,"qty":1},
    {"name":"Mouse","price":1000,"qty":-2}
    ]) == -1
    
    assert calculate_total([
    {"name":"Laptop","price":50000,"qty":0},
    {"name":"Mouse","price":1000,"qty":0}
    ]) == 0
    
def test_sc():
    assert shipping_charge(1001) == 1001 
    assert shipping_charge(0) == 0
    assert shipping_charge(999) == 1999
    assert shipping_charge(1000) == 1000


def test_ac():
    assert apply_coupon(100,'SAVE10') == 90
    assert apply_coupon(100,None) == 100
    assert apply_coupon(100,"SAVE100") == 0
    assert apply_coupon(-100,"") == -1
    assert apply_coupon(10,"Invalid") == 10
    assert apply_coupon(100,'save10') == 90
    assert apply_coupon(100,'sAvE10') == 90
    
    
def test_fb():

    # Normal order + valid coupon
    assert final_bill(
        [
            {"name":"Book","price":500,"qty":2}
        ],
        "SAVE10"
    ) == 1900

    # Normal order + no coupon
    assert final_bill(
        [
            {"name":"Book","price":500,"qty":2}
        ],
        None
    ) == 1000

    # Normal order + invalid coupon
    assert final_bill(
        [
            {"name":"Book","price":500,"qty":2}
        ],
        "INVALID"
    ) == 1000

    # Invalid cart
    assert final_bill(
        [
            {"name":"Book","price":500,"qty":-2}
        ],
        "SAVE10"
    ) == "Invalid Data cannot calculate bill."