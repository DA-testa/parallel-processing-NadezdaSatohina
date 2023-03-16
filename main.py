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
    n = int(input().split()[0])
    data = list(map(int, input().split()))

    result = parallel_processing(n, data)

    for i, j in result:
        print(i,j)




if __name__ == "__main__":
    main()
