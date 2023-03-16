# python3

def parallel_processing(n, data):
    output = []
    threads = [0] * n

    for t in data:
        how_soon = min(threads)
        soon_thread = threads.index(how_soon)
        output += [(soon_thread, how_soon)]
        threads[soon_thread] += t

    return output

def main():
    input_type = input()

    if "F" in input_type:
        filename = input()
        if ".a" in filename:
            return
        if "tests/" not in filename:
            filename = "tests/" + filename
        if "tests/" in filename:
            with open(filename) as f:
                n = int(f.readline().strip().split()[0])
                data = list(map(int, f.readline().strip().split()))
                result = parallel_processing(n, data)

    elif "I" in input_type:
        n = int(input().split()[0])
        data = list(map(int, input().split()))
        result = parallel_processing(n, data)

    result = parallel_processing(n, data)

    for i, j in result:
        print(i, j)




if __name__ == "__main__":
    main()
