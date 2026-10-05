def maximumToys(prices, k):
    prices.sort()

    count = 0

    for price in prices:
        if price <= k:
            k -= price
            count += 1
        else:
            break

    return count


if __name__ == '__main__':
    first_multiple_input = input().split()

    n = int(first_multiple_input[0])
    k = int(first_multiple_input[1])

    prices = list(map(int, input().rstrip().split()))

    result = maximumToys(prices, k)

    print(result)
