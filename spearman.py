#Made by github.com/badover

column_1 = [] #init 1
column_2 = [] #init 2

"""
FUNCTIONS
"""

def spearman_ranking(oglist, sorting='btl'):

    index_list = []
    for position, value in enumerate(oglist):
        index_list.append((value, position))

    if sorting == 'btl':
        index_list.sort(key=lambda x: x[0], reverse=True)
    else:
        index_list.sort(key=lambda x: x[0], reverse=False)

    temp_ranks = []
    i = 0

    while i < len(index_list):
        current = index_list[i][0]

        count = 1

        while(i + count < len(index_list) and index_list[i + count][0] == current):
            count = count + 1

        start_rank = i + 1
        end_rank = i + count
        average_rank = (start_rank + end_rank) / 2

        for _ in range(count):
            temp_ranks.append(average_rank)

        i += count

    final_ranks = [0] * len(oglist)

    for sorted_pos, (value, original_position) in enumerate(index_list):
        final_ranks[original_position] = temp_ranks[sorted_pos]

    return final_ranks


def spearmancalc(ranks1, ranks2):
    n = len(ranks1)

    mean_r1 = sum(ranks1) / n
    mean_r2 = sum(ranks2) / n

    numerator = sum((ranks1[i] - mean_r1) * (ranks2[i] - mean_r2) for i in range(n))
    denominator = (sum((r - mean_r1) ** 2 for r in ranks1) * sum((r - mean_r2) ** 2 for r in ranks2)) ** 0.5

    result = numerator / denominator
    return result, None, None


"""
MAIN
"""

print("=== SPEARMAN COEFFECIENT CALCULATION MADE BY GITHUB.COM/BADOVER ===")

numnums = int(input("Enter how many numbers there are in the first column: "))
for i in range(numnums):
    finput = float(input("Start entering numbers from the first column: "))
    column_1.append(finput)

numnums2 = int(input("Enter how many numbers there are in the second column: "))
for j in range(numnums2):
    sinput = float(input("Start entering numbers from the second column: "))
    column_2.append(sinput)

if len(column_1) != len(column_2):
    print("The number of columns does not match the number of columns in the first column.")
    exit(1)

print("\n=== INPUT DATA ===")
print("Column 1: ", column_1)
print("Column 2: ", column_2)

condition_for_sort = input("Do you want to rank your data from bigger to lower or from lower to bigger? (print btl or ltb) : ")
if condition_for_sort != 'btl' or condition_for_sort != 'ltb':
    print("Enter btl or ltb")

print("\nranking...")
ranks1 = spearman_ranking(column_1, condition_for_sort)
ranks2 = spearman_ranking(column_2, condition_for_sort)

print("\ncalculating spearman coefficient...")
spearman_coef, difference, squared_difference = spearmancalc(ranks1, ranks2)

print("\nYour spearman coefficient is: ",spearman_coef)

print("\n=== RESULT EXPLANATION ===")
if abs(spearman_coef) >= 0.9:
    print("Very strong correlation")
elif abs(spearman_coef) >= 0.7:
    print("Strong correlation")
elif abs(spearman_coef) >= 0.5:
    print("Average correlation")
elif abs(spearman_coef) >= 0.3:
    print("Weak correlation")
else:
    print("Very weak correlation or no correlation")

if spearman_coef > 0:
    print("Direction: positive correlarion")
else:
    print("Direction: negative correlarion")








