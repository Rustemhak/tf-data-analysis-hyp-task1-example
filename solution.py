import pandas as pd
import numpy as np


chat_id = 326525586 # Ваш chat ID, не меняйте название переменной

def solution(x_success: int, 
             x_cnt: int, 
             y_success: int, 
             y_cnt: int) -> bool:
    # Измените код этой функции
    # Это будет вашим решением
    # Не меняйте название функции и её аргументы
    p1 = x_success / x_cnt
    p2 = y_success / y_cnt

    p_pool = (x_success + y_success) / (x_cnt + y_cnt)
    std_err = np.sqrt(p_pool * (1 - p_pool) * (1 / x_cnt + 1 / y_cnt))

    z_stat = (p1 - p2) / std_err

    # Двусторонний тест
    alpha = 0.06
    z_critical = stats.norm.ppf(1 - alpha / 2)
    return abs(z_stat) > z_critical # Ваш ответ, True или False
