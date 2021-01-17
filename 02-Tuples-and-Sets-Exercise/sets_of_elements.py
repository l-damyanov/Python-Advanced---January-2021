n, m = input().split()
n_elements = set()
m_elements = set()

for num in range(int(n)):
    number = int(input())
    n_elements.add(number)

for num in range(int(m)):
    number = int(input())
    m_elements.add(number)

unique_elements = n_elements.intersection(m_elements)

for el in unique_elements:
    print(el)
