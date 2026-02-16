def main():
    n = 5
    arr = [1, 2, 3, 4, 5]
    total_sum = 0.0
    for i in range(n):
        total_sum += float(arr[i])
        average = total_sum / n
    print(f"The average is {average}")


if __name__ == "__main__":
    main()