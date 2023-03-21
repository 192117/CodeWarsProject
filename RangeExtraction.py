
def solution(args):
    count = 0
    answer = ''
    check = []
    for number in args:
        if len(check) == 0:
            check.append(number)
            count += 1
        else:
            if check[-1] + 1 == number:
                check.append(number)
                count += 1
            else:
                if count >= 3:
                    answer += str(check[0]) + '-' + str(check[-1]) + ','
                else:
                    for n in check:
                        answer += str(n) + ','
                check.clear()
                check.append(number)
                count = 1
    if len(check) != 0:
        if count >= 3:
            answer += str(check[0]) + '-' + str(check[-1]) + ','
        else:
            for n in check:
                answer += str(n) + ','
        check.clear()
    return answer.rstrip(',')





print(solution([-10, -9, -8, -6, -3, -2, -1, 0, 1, 3, 4, 5, 7, 8, 9, 10, 11, 14, 15, 17, 18, 19, 20]))
# returns "-10--8,-6,-3-1,3-5,7-11,14,15,17-20"