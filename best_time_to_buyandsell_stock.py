def best_profit(arr):
    profit = 0
    min = arr[0]
    for i in range(len(arr)):
        if min > arr[i]:
            min = arr[i]
        cost = arr[i] - min
        if profit < cost:
            profit = cost
    return cost
print(best_profit([0,13]))