from functools import lru_cache, cache


@cache
def fib(n:int) -> int:
    if n <= 1:
        return 1
    else:
        return fib(n-1) + fib(n-2)

if __name__ == "__main__":    
    for i in range(100):
        print(f"{i} - {fib(i)}")