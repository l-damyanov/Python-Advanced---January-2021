# jobs = list(map(int, input().split(', ')))
# job_index = int(input())
#
# valid_numbers = []
#
# for j_i in range(len(jobs)):
#     if jobs[j_i] <= jobs[job_index]:
#         valid_numbers.append(jobs[j_i])
#
# print(sum(valid_numbers))


def read_input():
    return (map(int, input().split(', ')), int(input()))

def get_min_cycles_for_job(values, job_index):
    sorted_jobs = sorted([(v, i) for (i, v) in enumerate(jobs)])
    cycles = 0
    for (job, index) in sorted_jobs:
        cycles += job
        if index == job_index:
            break
    return cycles

def print_result(result):
    print(result)

(jobs, job_index) = read_input()
result = get_min_cycles_for_job(jobs, job_index)
print_result(result)