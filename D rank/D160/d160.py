# Problem: Convert Mountain Height to "Gou" Units
# Paiza Rank D Problem
# Description: 
# Given mountain heigh N (meters) and a gou-level M (1 gou = N/10),
# calculate the height in meters at M gou.

def calculate_gou_height(mountain_height, gou_level):
    gou_unit = mountain_height // 10
    return gou_unit * gou_level

if __name__ == "__main__":
    n = int(input("Enter mountain height (meters): "))
    m = int(input("Enter gou level (1-10): "))
    result = calculate_gou_height(n, m)
    print(result)