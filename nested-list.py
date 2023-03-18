if __name__ == '__main__':
    records = []
    for _ in range(int(input())):
        name = input()
        score = float(input())
        records.append([name, score])
    records.sort(key=lambda x: x[1])
    s_low =records[0][1]
    for i in range(len(records)):
        if records[i][1] > s_low:
            s_low = records[i][1]
            break
    records.sort(key=lambda x: x[0])
    print(*(n[0] for n in records if n[1]==s_low), sep='\n')