def no_notes(a):
    Q = [2000, 500, 200, 100, 50, 20, 10]
    x = 0
    for i in range(7):
        q = Q[i]
        x = a//Q
        print("Notes of{} = {}".format(q, x))
        a = a%Q


amount = int(input("Enter Total Amount"))
no_notes(amount)