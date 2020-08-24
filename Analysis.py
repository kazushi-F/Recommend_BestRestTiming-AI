import numpy as np
import random

#報酬を計算する関数
def reward(solve, reward_sum):
    for i in range(len(solve)):
        reward_one = 1 / solve[i]
        reward_sum = reward_sum + reward_one
    return(reward_sum)

#解答時間を予想するAI関数（回帰分析）
def regression(solve, series_study, series_rest, continuous, solve_last, time_rest, time_answer, solve_x, solve_y, rest_coef):
    print("予測中...")
    solve_one = 0
    coefficient = 0
    difference = 0
    time_solve = 0
    time_passage = (continuous - 1) * 900
    coefficient = np.polyfit(solve_x[series_study], solve_y[series_study], 2)
    print("係数完了")
    if time_rest != 0:
        solve_last = solve_last - np.mean(rest_coef[series_rest][time_rest - 1])
    print("平均とり完了")
    solve_one = np.poly1d(coefficient)(time_passage)
    print("値取得")
    solve_one = round(solve_one, 5)
    difference = solve_last - solve_one
    time_passage = time_passage + solve_last
    while time_answer > time_solve:
        solve_one = 0
        solve_one = np.poly1d(coefficient)(time_passage)
        solve_one = round(solve_one, 5) + difference
        solve.append(solve_one)
        time_passage = time_passage + solve_one
        time_solve = time_solve + solve_one
    if time_solve > time_answer:
        solve.pop(-1)
    return(solve)

#休憩時間を提案するAI関数
def rest(series_study, series_rest, continuous, solve_last, time_sum, solve_x, solve_y, rest_coef):
    reward_cho = [0,0,0,0,0]
    series_study_now = series_study
    series_rest_now = series_rest
    continuous_now = continuous
    solve_last_now = solve_last
    time_sum_now = time_sum
    for i in range(5):
        for j in range(5):
            for k in range(5):
                for l in range(5):
                    for m in range(5):
                        for n in range(5):
                            for o in range(5):
                                series_study = series_study_now
                                series_rest = series_rest_now
                                continuous = continuous_now
                                solve_last = solve_last_now
                                time_answer = 15
                                time_sum = time_sum_now
                                reward_any = 0
                                if i == 0:
                                    continuous = continuous + 1
                                else:
                                    series_study = series_study + 1
                                    series_rest = series_rest + 1
                                    continuous = 1
                                time_sum = time_sum + (5 * i)
                                if time_sum >= 120:
                                    continue
                                if (time_sum + 15) > 120:
                                    time_answer = 120 - time_sum
                                solve = []
                                solve = regression(solve, series_study, series_rest - 1, continuous, solve_last, i, time_answer * 60, solve_x, solve_y, rest_coef)
                                reward_any = reward(solve, reward_any)
                                time_sum = time_sum + time_answer
                                if time_sum == 120:
                                    reward_cho[i] = max(reward_cho[i], reward_any)
                                    continue
                                solve_last = solve[-1]
                                if j == 0:
                                    continuous = continuous + 1
                                else:
                                    series_study = series_study + 1
                                    series_rest = series_rest + 1
                                    continuous = 1
                                time_sum = time_sum + (5 * j)
                                if time_sum >= 120:
                                    reward_cho[i] = max(reward_cho[i], reward_any)
                                    continue
                                if (time_sum + 15) > 120:
                                    time_answer = 120 - time_sum
                                solve = []
                                solve = regression(solve, series_study, series_rest - 1, continuous, solve_last, j, time_answer * 60, solve_x, solve_y, rest_coef)
                                reward_any = reward(solve, reward_any)
                                time_sum = time_sum + time_answer
                                if time_sum == 120:
                                    reward_cho[i] = max(reward_cho[i], reward_any)
                                    continue
                                solve_last = solve[-1]
                                if k == 0:
                                    continuous = continuous + 1
                                else:
                                    series_study = series_study + 1
                                    series_rest = series_rest + 1
                                    continuous = 1
                                time_sum = time_sum + (5 * k)
                                if time_sum >= 120:
                                    reward_cho[i] = max(reward_cho[i], reward_any)
                                    continue
                                if (time_sum + 15) > 120:
                                    time_answer = 120 - time_sum
                                solve = []
                                solve = regression(solve, series_study, series_rest - 1, continuous, solve_last, k, time_answer * 60, solve_x, solve_y, rest_coef)
                                reward_any = reward(solve, reward_any)
                                time_sum = time_sum + time_answer
                                if time_sum == 120:
                                    reward_cho[i] = max(reward_cho[i], reward_any)
                                    continue
                                solve_last = solve[-1]
                                if l == 0:
                                    continuous = continuous + 1
                                else:
                                    series_study = series_study + 1
                                    series_rest = series_rest + 1
                                    continuous = 1
                                time_sum = time_sum + (5 * l)
                                if time_sum >= 120:
                                    reward_cho[i] = max(reward_cho[i], reward_any)
                                    continue
                                if (time_sum + 15) > 120:
                                    time_answer = 120 - time_sum
                                solve = []
                                solve = regression(solve, series_study, series_rest - 1, continuous, solve_last, l, time_answer * 60, solve_x, solve_y, rest_coef)
                                reward_any = reward(solve, reward_any)
                                time_sum = time_sum + time_answer
                                if time_sum == 120:
                                    reward_cho[i] = max(reward_cho[i], reward_any)
                                    continue
                                solve_last = solve[-1]
                                if m == 0:
                                    continuous = continuous + 1
                                else:
                                    series_study = series_study + 1
                                    series_rest = series_rest + 1
                                    continuous = 1
                                time_sum = time_sum + (5 * m)
                                if time_sum >= 120:
                                    reward_cho[i] = max(reward_cho[i], reward_any)
                                    continue
                                if (time_sum + 15) > 120:
                                    time_answer = 120 - time_sum
                                solve = []
                                solve = regression(solve, series_study, series_rest - 1, continuous, solve_last, m, time_answer * 60, solve_x, solve_y, rest_coef)
                                reward_any = reward(solve, reward_any)
                                time_sum = time_sum + time_answer
                                if time_sum == 120:
                                    reward_cho[i] = max(reward_cho[i], reward_any)
                                    continue
                                solve_last = solve[-1]
                                if n == 0:
                                    continuous = continuous + 1
                                else:
                                    series_study = series_study + 1
                                    series_rest = series_rest + 1
                                    continuous = 1
                                time_sum = time_sum + (5 * n)
                                if time_sum >= 120:
                                    reward_cho[i] = max(reward_cho[i], reward_any)
                                    continue
                                if (time_sum + 15) > 120:
                                    time_answer = 120 - time_sum
                                solve = []
                                solve = regression(solve, series_study, series_rest - 1, continuous, solve_last, n, time_answer * 60, solve_x, solve_y, rest_coef)
                                reward_any = reward(solve, reward_any)
                                time_sum = time_sum + time_answer
                                if time_sum == 120:
                                    reward_cho[i] = max(reward_cho[i], reward_any)
                                    continue
                                solve_last = solve[-1]
                                if o == 0:
                                    continuous = continuous + 1
                                else:
                                    series_study = series_study + 1
                                    series_rest = series_rest + 1
                                    continuous = 1
                                time_sum = time_sum + (5 * o)
                                if time_sum >= 120:
                                    reward_cho[i] = max(reward_cho[i], reward_any)
                                    continue
                                if (time_sum + 15) > 120:
                                    time_answer = 120 - time_sum
                                solve = []
                                solve = regression(solve, series_study, series_rest - 1, continuous, solve_last, o, time_answer * 60, solve_x, solve_y, rest_coef)
                                reward_any = reward(solve, reward_any)
                                reward_cho[i] = max(reward_cho[i], reward_any)
    return(np.argmax(reward_cho))

#回帰分析用の係数を更新する関数（勉強）
def setS(solve, series_study, continuous, solve_x, solve_y):
    time_x = continuous * 900
    for i in range(len(solve)):
        solve_y[series_study].append(solve[i])
        time_x = time_x + solve[i]
        solve_x[series_study].append(time_x)
    return(solve_x, solve_y)

#回帰分析用の係数を更新する関数（休憩）
def setR(solve_first, solve_last, series_rest, time_rest, rest_coef):
    rest_coef[series_rest][time_rest].append(solve_last - solve_first)
    return(rest_coef)

#バーチャルスチューデント関数
def virtualstudent(solve, series_study, continuous, continuous_before, solve_last, time_rest, time_answer, tilt):
    recovery = 0
    time_sum = 0
    time_answer = time_answer * 60
    if continuous == 1:
        tilt = 1
    if time_rest == 1:
        recovery = random.uniform(1.4, 1.6)
    elif time_rest == 2:
        recovery = random.uniform(1.8, 2.1)
    elif time_rest == 3:
        recovery = random.uniform(2.4, 2.8)
    elif time_rest == 4:
        recovery = random.uniform(3.2, 3.8)
    if series_study > 1:
        recovery = (recovery - (series_study * 0.2)) + (continuous_before * 0.5)
    solve_last = solve_last - recovery
    if solve_last ==0:
        solve_last = 6.5
    while time_answer >= time_sum:
        tilts = tilt * tilt
        solve_one = random.uniform(solve_last - 1.5, solve_last)
        solve_one = solve_one + (tilts * 0.01)
        solve.append(solve_one)
        time_sum = time_sum + solve_one
        tilt = tilt + (0.1 * series_study)
    if time_sum > time_answer:
        solve.pop(-1)
    return(solve, continuous, tilt)

#学習する関数
def study(solve_x, solve_y, rest_coef):
    count = 0
    for i in range(5):
        for j in range(5):
            for k in range(5):
                for l in range(5):
                    for m in range(5):
                        for n in range(5):
                            for o in range(5):
                                count+=1
                                print(count, "回目の学習")
                                series_study = 0
                                series_rest = 0
                                continuous = 1
                                continuous_before = 1
                                tilt = 1
                                solve_last = 0
                                time_answer = 15
                                time_sum = 0
                                setR_on = 0
                                solve = []
                                solve, continuous_last, tilt = virtualstudent(solve, series_study + 1, continuous, continuous_before, solve_last, 0, time_answer, tilt)
                                solve_x, solve_y = setS(solve, series_study, continuous - 1, solve_x, solve_y)
                                time_sum = time_sum + time_answer
                                if i == 0:
                                    setR_on = 0
                                    continuous = continuous + 1
                                else:
                                    print("勉強：", continuous * 15, "分")
                                    print("休憩：", i * 5, "分")
                                    setR_on = 1
                                    series_study = series_study + 1
                                    continuous = 1
                                solve_last = solve[-1]
                                time_sum = time_sum + (5 * i)
                                if time_sum >= 120:
                                    print("---------------終了---------------")
                                    continue
                                if (time_sum + 15) > 120:
                                    time_answer = 120 - time_sum
                                solve = []
                                solve, continuous_last, tilt = virtualstudent(solve, series_study + 1, continuous, continuous_before, solve_last, i, time_answer, tilt)
                                solve_x, solve_y = setS(solve, series_study, continuous - 1, solve_x, solve_y)
                                time_sum = time_sum + time_answer
                                if setR_on == 1:
                                    rest_coef = setR(solve[0], solve_last, series_rest, i - 1, rest_coef)
                                    series_rest = series_rest + 1
                                if j == 0:
                                    setR_on = 0
                                    continuous = continuous + 1
                                else:
                                    print("勉強：", continuous * 15, "分")
                                    print("休憩：", j * 5, "分")
                                    setR_on = 1
                                    series_study = series_study + 1
                                    continuous = 1
                                solve_last = solve[-1]
                                time_sum = time_sum + (5 * j)
                                if time_sum >= 120:
                                    print("---------------終了---------------")
                                    continue
                                if (time_sum + 15) > 120:
                                    time_answer = 120 - time_sum
                                solve = []
                                solve, continuous_last, tilt = virtualstudent(solve, series_study + 1, continuous, continuous_before, solve_last, j, time_answer, tilt)
                                solve_x, solve_y = setS(solve, series_study, continuous - 1, solve_x, solve_y)
                                time_sum = time_sum + time_answer
                                if setR_on == 1:
                                    rest_coef = setR(solve[0], solve_last, series_rest, j - 1, rest_coef)
                                    series_rest = series_rest + 1
                                if k == 0:
                                    setR_on = 0
                                    continuous = continuous + 1
                                else:
                                    print("勉強：", continuous * 15, "分")
                                    print("休憩：", k * 5, "分")
                                    setR_on = 1
                                    series_study = series_study + 1
                                    continuous = 1
                                solve_last = solve[-1]
                                time_sum = time_sum + (5 * k)
                                if time_sum >= 120:
                                    print("---------------終了---------------")
                                    continue
                                if (time_sum + 15) > 120:
                                    time_answer = 120 - time_sum
                                solve = []
                                solve, continuous_last, tilt = virtualstudent(solve, series_study + 1, continuous, continuous_before, solve_last, k, time_answer, tilt)
                                solve_x, solve_y = setS(solve, series_study, continuous - 1, solve_x, solve_y)
                                time_sum = time_sum + time_answer
                                if setR_on == 1:
                                    rest_coef = setR(solve[0], solve_last, series_rest, k - 1, rest_coef)
                                    series_rest = series_rest + 1
                                if l == 0:
                                    setR_on = 0
                                    continuous = continuous + 1
                                else:
                                    print("勉強：", continuous * 15, "分")
                                    print("休憩：", l * 5, "分")
                                    setR_on = 1
                                    series_study = series_study + 1
                                    continuous = 1
                                solve_last = solve[-1]
                                time_sum = time_sum + (5 * l)
                                if time_sum >= 120:
                                    print("---------------終了---------------")
                                    continue
                                if (time_sum + 15) > 120:
                                    time_answer = 120 - time_sum
                                solve = []
                                solve, continuous_last, tilt = virtualstudent(solve, series_study + 1, continuous, continuous_before, solve_last, l, time_answer, tilt)
                                solve_x, solve_y = setS(solve, series_study, continuous - 1, solve_x, solve_y)
                                time_sum = time_sum + time_answer
                                if setR_on == 1:
                                    rest_coef = setR(solve[0], solve_last, series_rest, l - 1, rest_coef)
                                    series_rest = series_rest + 1
                                if m == 0:
                                    setR_on = 0
                                    continuous = continuous + 1
                                else:
                                    print("勉強：", continuous * 15, "分")
                                    print("休憩：", m * 5, "分")
                                    setR_on = 1
                                    series_study = series_study + 1
                                    continuous = 1
                                solve_last = solve[-1]
                                time_sum = time_sum + (5 * m)
                                if time_sum >= 120:
                                    print("---------------終了---------------")
                                    continue
                                if (time_sum + 15) > 120:
                                    time_answer = 120 - time_sum
                                solve = []
                                solve, continuous_last, tilt = virtualstudent(solve, series_study + 1, continuous, continuous_before, solve_last, m, time_answer, tilt)
                                solve_x, solve_y = setS(solve, series_study, continuous - 1, solve_x, solve_y)
                                time_sum = time_sum + time_answer
                                if setR_on == 1:
                                    rest_coef = setR(solve[0], solve_last, series_rest, m - 1, rest_coef)
                                    series_rest = series_rest + 1
                                if n == 0:
                                    setR_on = 0
                                    continuous = continuous + 1
                                else:
                                    print("勉強：", continuous * 15, "分")
                                    print("休憩：", n * 5, "分")
                                    setR_on = 1
                                    series_study = series_study + 1
                                    continuous = 1
                                solve_last = solve[-1]
                                time_sum = time_sum + (5 * n)
                                if time_sum >= 120:
                                    print("---------------終了---------------")
                                    continue
                                if (time_sum + 15) > 120:
                                    time_answer = 120 - time_sum
                                solve = []
                                solve, continuous_last, tilt = virtualstudent(solve, series_study + 1, continuous, continuous_before, solve_last, n, time_answer, tilt)
                                solve_x, solve_y = setS(solve, series_study, continuous - 1, solve_x, solve_y)
                                time_sum = time_sum + time_answer
                                if setR_on == 1:
                                    rest_coef = setR(solve[0], solve_last, series_rest, n - 1, rest_coef)
                                    series_rest = series_rest + 1
                                if o == 0:
                                    setR_on = 0
                                    continuous = continuous + 1
                                else:
                                    print("勉強：", continuous * 15, "分")
                                    print("休憩：", o * 5, "分")
                                    setR_on = 1
                                    series_study = series_study + 1
                                    continuous = 1
                                solve_last = solve[-1]
                                time_sum = time_sum + (5 * o)
                                if time_sum >= 120:
                                    print("---------------終了---------------")
                                    continue
                                if (time_sum + 15) > 120:
                                    time_answer = 120 - time_sum
                                solve = []
                                solve, continuous_last, tilt = virtualstudent(solve, series_study + 1, continuous, continuous_before, solve_last, o, time_answer, tilt)
                                solve_x, solve_y = setS(solve, series_study, continuous - 1, solve_x, solve_y)
                                time_sum = time_sum + time_answer
                                if setR_on == 1:
                                    rest_coef = setR(solve[0], solve_last, series_rest, o - 1, rest_coef)
                                print("---------------終了---------------")
    return(solve_x, solve_y, rest_coef)

#AIを使って勉強する関数
def AIstudy(solve_x, solve_y, rest_coef):
    series_study = 0
    series_rest = 0
    continuous = 1
    continuous_before = 1
    solve_last = 0
    tilt = 1
    time_rest = 0
    time_answer = 15
    time_sum = 0
    answer_count = 0
    setR_on = 0
    while time_sum < 120:
        solve = []
        solve, continuous_before, tilt = virtualstudent(solve, series_study + 1, continuous, continuous_before, solve_last, time_rest, time_answer, tilt)
        answer_count = answer_count + len(solve)
        solve_x, solve_y = setS(solve, series_study, continuous - 1, solve_x, solve_y)
        print("勉強：", time_answer, "分")
        time_sum = time_sum + time_answer
        solve_last = solve[-1]
        time_rest = rest(series_study, series_rest, continuous, solve_last, time_sum, solve_x, solve_y, rest_coef)
        if setR_on == 1:
            rest_coef = setR(solve[0], solve_last, series_rest, time_rest - 1, rest_coef)
            series_rest = series_rest + 1
        if time_rest == 0:
            coefR_on = 0
            continuous = continuous + 1
        else:
            coefR_on = 1
            series_study = series_study + 1
            continuous = 1
        print("休憩：", time_rest, "分")
        time_sum = time_sum + (time_rest * 5)
        if (time_sum + 15) > 120:
            time_answer = 120 - time_sum
    return(answer_count, solve_x, solve_y, rest_coef)
    
#メイン関数
def main():
    count_study = 1
    count_AI = 1
    answer = []
    solve_x = [[],[],[],[],[],[]]
    solve_y = [[],[],[],[],[],[]]
    rest_coef = [[[],[],[],[]],[[],[],[],[]],[[],[],[],[]],[[],[],[],[]],[[],[],[],[]]]
    for i in range(count_study):
        print("AI学習中...")
        solve_x, solve_y, rest_coef = study(solve_x, solve_y, rest_coef)
        print("AIの", i,"回目の学習が終了しました。")
    print("AIの学習が終了しました。続いて本番に入ります。")
    for i in range(count_AI):
        print("学習中...")
        answer_one, solve_x, solve_y, rest_coef = AIstudy(solve_x, solve_y, rest_coef)
        answer.append(answer_one)
        print(i, "回目の学習が終了しました。")
    print("結果を出力します。")
    for i in range(len(answer)):
        print(i + 1, ":", answer[i])
    return()
main()
