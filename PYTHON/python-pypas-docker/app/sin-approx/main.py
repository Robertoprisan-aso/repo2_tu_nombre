import math

def run(x: float) -> float:
    term1 = 4 * x
    term2 = 180 - x
    term3 = 40500 - x * term2
    sin= (term1 * term2) / term3
    
    return sin
    



# DO NOT TOUCH THE CODE BELOW
if __name__ == '__main__':
    import vendor

    vendor.launch(run)
