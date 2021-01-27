l = list(map(int, input().split()))

negatives = [el for el in l if el < 0]
positives = [el for el in l if el > 0]
print(sum(negatives))
print(sum(positives))
if sum(positives) < abs(sum(negatives)):
    print("The negatives are stronger than the positives")
else:
    print("The positives are stronger than the negatives")
