def birthdayCakeCandles(candles):
    maximum = max(candles)
    count = candles.count(maximum)
    return count


if __name__ == '__main__':
    n = int(input())
    candles = list(map(int, input().split()))

    result = birthdayCakeCandles(candles)

    print(result)
