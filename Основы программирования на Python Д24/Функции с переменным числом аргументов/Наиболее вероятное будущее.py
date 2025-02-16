def best_future(*data):
    ans = []
    for i in range(len(data)):
        for j in range(i + 1, len(data)):
            if data[j] < data[i]:
                ans.append(j)
                break
        else:
            ans.append(-1)
    return ans