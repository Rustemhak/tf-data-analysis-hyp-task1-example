import pandas as pd
import numpy as np
from statsmodels.stats.proportion import proportions_ztest

chat_id = 326525586 # Ваш chat ID, не меняйте название переменной

def solution(x_success: int, 
             x_cnt: int, 
             y_success: int, 
             y_cnt: int) -> bool:
    # Измените код этой функции
    # Это будет вашим решением
    # Не меняйте название функции и её аргументы
    counts = np.array([x_success, y_success])
    nobs = np.array([x_cnt, y_cnt])
    
    z_stat, p_value = proportions_ztest(counts, nobs, alternative = 'larger')
    alpha = 0.06
    return p_value < alpha # Ваш ответ, True или False
