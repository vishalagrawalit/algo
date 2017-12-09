"""
Greedy Algorithm - 1
It may not be very useful for the Competitive Programmers.
This algorithm is built for practice purpose. Still you can use it as a built-in function.

Job Scheduling Algorithm with deadline.
"""

# This function returns the total profit in JOb Scheduling Algorithm with a deadline.
def job_scheduleing(jobs, n):
    jobs = sorted(jobs, key=lambda x:x[2])

    slots = [False]*n
    for i in range(n):
        for j in range(min(n, jobs[i][1])-1, -1, -1):
            if slots[j]==False:
                slots[j] = jobs[i][2]

    total_profit = 0
    for i in range(n):
        if slots[i]:
            total_profit += slots[i]

    return total_profit
