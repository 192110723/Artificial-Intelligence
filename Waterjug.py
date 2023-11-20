def water_jug_problem(capacity_x, capacity_y, target):
    jug_x = 0
    jug_y = 0

    while jug_x != target and jug_y != target:
        if jug_y == 0:
            jug_y = capacity_y
            print(f"Fill jug Y: ({jug_x}, {jug_y})")
        elif jug_x < capacity_x:
            transfer_amount = min(jug_y, capacity_x - jug_x)
            jug_y -= transfer_amount
            jug_x += transfer_amount
            print(f"Pour {transfer_amount} units from jug Y to jug X: ({jug_x}, {jug_y})")
        elif jug_x == capacity_x:
            jug_x = 0
            print(f"Empty jug X: ({jug_x}, {jug_y})")
    print(f"Target {target} achieved!")
capacity_x = int(input("Enter the capacity of jug X: "))
capacity_y = int(input("Enter the capacity of jug Y: "))
target = int(input("Enter the target amount: "))
water_jug_problem(capacity_x, capacity_y, target)
