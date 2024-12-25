def challenge_result(score,time):
    result = "Ничья!"
    if score[0] > score[1] or score[0] == score[1] and time[0] > time[1]:
        result = "Победа команды Мастера кода!"
    elif score[0] < score[1] or score[0] == score[1] and time[0] < time[1]:
        result = "Победа команды Волшебники Данных!"
    return result

team1_num = 5
team2_num = 6
score_1 = 40
score_2 = 42
team1_time = 1552.512
team2_time = 2153.31451
tasks_total = 82
time_avg = format((team1_time+team2_time)/(score_1+score_2),'.2f')

print("\%d")
print('В команде Мастера кода участников: %d !' % team1_num)
print('Итого сегодня в командах участников: %d и %d!' %(team1_num,team2_num))

print("\nformat")
print("Команда Волшебники данных решила задач: {}!".format(score_2))
print("Волшебники данных решили задачи за {} с !".format(team1_time))

print("\nf-strings")
print(f"Команды решили {score_1} и {score_2} задач.")
print(f"Сегодня было решено {score_1+score_2} задач, в среднем по {time_avg} секунды на задачу!")

print("\n",challenge_result([score_1,score_2],[team1_time,team2_time]))