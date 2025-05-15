import random
import time
import math


def gen_data(n: int = 75_000) -> list[dict]:
    users = []
    for i in range(75_000):
        user = {
            "id": i,
            "age": random.randint(18, 80),
            "score": random.randint(1, 10000),
            "email": f"user{i}@example.com",
        }
        users.append(user)

    return user


def is_prime(n: int) -> bool:
    if n < 2:
        return False

    _is_prime = True
    for i in range(2, n):
        if n % i == 0:
            _is_prime = False
            break

    return _is_prime


if __name__ == "__main__":
    start = time.time()

    """
        Ideas for optimization
          - [ ] List comprehension
          - 
    """
    users = gen_data(75_000)

    """
        Ideas for optimization
          - [ ]
    
    """
    prime_users = []
    for user in users:
        n = user["id"]

        if is_prime(n):
            prime_users.append(user)

    # Complex and inefficient scoring logic
    """
        Ideas to optimize 
          - [ ]
    
    """
    total_score = 0
    for user in prime_users:
        time.sleep(0.001)  # simulate model latency

        name = user["email"].split("@")[0]  # pretend we're doing name-based scoring
        name_entropy = sum(ord(c) ** 1.5 for c in name)  # unnecessary power ops
        behavior_factor = math.sin(user["score"] / 17) + math.log1p(user["age"])
        noise = sum([random.random() * 0.1 for _ in range(100)])  # artificial noise

        score = name_entropy * behavior_factor + noise
        total_score += int(score)

    # Artificially slow sort and filter
    """
        Ideas to optimize 
          - [ ]
    
    """
    sorted_emails = []
    sorted_users = sorted(prime_users, key=lambda u: u["score"], reverse=True)
    for user in sorted_users:
        time.sleep(0.001)  # simulate I/O delay
        if user["score"] % 3 == 0 and user["email"].startswith("user1"):
            sorted_emails.append(user["email"])

    end = time.time()

    print(f"Total score from prime users: {total_score}")
    print(f"Filtered emails: {sorted_emails[:10]} ...")
    print(f"Execution time: {end - start:.2f} seconds")
