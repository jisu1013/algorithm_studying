N = int(input())
input_list = []
for _ in range(N):
    input_list.append(int(input()))
input_list = sorted(input_list)
for i in range(N):
    print(input_list[i])
