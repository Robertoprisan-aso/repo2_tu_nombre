import math
def run(radius) -> float:
    
    pi_dec = round(math.pi, 2)

    area = pi_dec * (radius ** 2)
    return area


# DO NOT TOUCH THE CODE BELOW
if __name__ == '__main__':
    import vendor

    vendor.launch(run)
