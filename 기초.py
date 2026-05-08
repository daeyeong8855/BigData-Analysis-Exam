import pandas as pd
df = pd.read_csv('https://raw.githubusercontent.com/Datamanim/datarepo/main/churn/train.csv')
# Q1. df의 상위 5개 행을 출력하시오.
print(df.head())
# Q2. df의 행과 열의 개수를 출력하시오.
print(df.shape)
# Q3. df의 컬럼명을 출력하시오.
print(df.columns)
# Q4. df의 데이터 타입을 출력하시오.
print(df.dtypes)
# Q5. df의 결측치 개수를 출력하시오.
print(df.isnull().sum())
# Q6. df의 'TotalCharges' 컬럼의 데이터 타입을 float으로 변환하시오.
df['TotalCharges'] = pd.to_numeric(df['TotalCharges'], errors='coerce')
print(df['TotalCharges'].dtype)
# Q7. df의 'TotalCharges' 컬럼의 결측치 개수를 출력하시오.
print(df['TotalCharges'].isnull().sum())
# Q8. df의 'TotalCharges' 컬럼의 결측치를 0으로 대체하시오.
df['TotalCharges'] = df['TotalCharges'].fillna(0)
print(df['TotalCharges'].isnull().sum())
# Q9. df의 'TotalCharges' 컬럼의 평균값을 출력하시오.
print(df['TotalCharges'].mean())
# Q10. df의 'TotalCharges' 컬럼의 중앙값을 출력하시오.
print(df['TotalCharges'].median())
# Q11. df의 'TotalCharges' 컬럼의 최빈값을 출력하시오.
print(df['TotalCharges'].mode()[0])
# Q12. df의 'TotalCharges' 컬럼의 표준편차를 출력하시오.
print(df['TotalCharges'].std())
# Q13. df의 'TotalCharges' 컬럼의 분산을 출력하시오.
print(df['TotalCharges'].var())
# Q14. df의 'TotalCharges' 컬럼의 최소값을 출력하시오.
print(df['TotalCharges'].min())
# Q15. df의 'TotalCharges' 컬럼의 최대값을 출력하시오.
print(df['TotalCharges'].max())
# Q16. df의 'TotalCharges' 컬럼의 25% 분위값을 출력하시오.
print(df['TotalCharges'].quantile(0.25))
# Q17. df의 'TotalCharges' 컬럼의 50% 분위값을 출력하시오.
print(df['TotalCharges'].quantile(0.5))
# Q18. df의 'TotalCharges' 컬럼의 75% 분위값을 출력하시오.
print(df['TotalCharges'].quantile(0.75))
# Q19. df의 'TotalCharges' 컬럼의 IQR을 출력하시오.
Q1 = df['TotalCharges'].quantile(0.25)
Q3 = df['TotalCharges'].quantile(0.75)
IQR = Q3 - Q1
print(IQR)
# Q20. df의 'TotalCharges' 컬럼의 이상치 개수를 출력하시오.
lower_bound = Q1 - 1.5 * IQR
upper_bound = Q3 + 1.5 * IQR
outliers = df[(df['TotalCharges'] < lower_bound) | (df['TotalCharges'] > upper_bound)]
print(outliers.shape[0])
# Q21. df의 'TotalCharges' 컬럼의 이상치를 제거한 후, 상위 5개 행을 출력하시오.
df_no_outliers = df[(df['TotalCharges'] >= lower_bound) & (df['TotalCharges'] <= upper_bound)]
print(df_no_outliers.head())
# Q22. df의 'TotalCharges' 컬럼의 이상치를 제거한 후, 행과 열의 개수를 출력하시오.
print(df_no_outliers.shape)
# Q23. df의 'TotalCharges' 컬럼의 이상치를 제거한 후, 결측치 개수를 출력하시오.
print(df_no_outliers['TotalCharges'].isnull().sum())
# Q24. df의 'TotalCharges' 컬럼의 이상치를 제거한 후, 평균값을 출력하시오.
print(df_no_outliers['TotalCharges'].mean())
# Q25. df의 'TotalCharges' 컬럼의 이상치를 제거한 후, 중앙값을 출력하시오.
print(df_no_outliers['TotalCharges'].median())
# Q26. df의 'TotalCharges' 컬럼의 이상치를 제거한 후, 최빈값을 출력하시오.
print(df_no_outliers['TotalCharges'].mode()[0])
# Q27. df의 'TotalCharges' 컬럼의 이상치를 제거한 후, 표준편차를 출력하시오.
print(df_no_outliers['TotalCharges'].std())
# Q28. df의 'TotalCharges' 컬럼의 이상치를 제거한 후, 분산을 출력하시오.
print(df_no_outliers['TotalCharges'].var())
# Q29. df의 'TotalCharges' 컬럼의 이상치를 제거한 후, 최소값을 출력하시오.
print(df_no_outliers['TotalCharges'].min())
# Q30. df의 'TotalCharges' 컬럼의 이상치를 제거한 후, 최대값을 출력하시오.
print(df_no_outliers['TotalCharges'].max())
# Q31. df의 'TotalCharges' 컬럼의 이상치를 제거한 후, 25% 분위값을 출력하시오.
print(df_no_outliers['TotalCharges'].quantile(0.25))
# Q32. df의 'TotalCharges' 컬럼의 이상치를 제거한 후, 50% 분위값을 출력하시오.
print(df_no_outliers['TotalCharges'].quantile(0.5))
# Q33. df의 'TotalCharges' 컬럼의 이상치를 제거한 후, 75% 분위값을 출력하시오.
print(df_no_outliers['TotalCharges'].quantile(0.75))
# Q34. df의 'TotalCharges' 컬럼의 이상치를 제거한 후, IQR을 출력하시오.
Q1_no_outliers = df_no_outliers['TotalCharges'].quantile(0.25)
Q3_no_outliers = df_no_outliers['TotalCharges'].quantile(0.75)
IQR_no_outliers = Q3_no_outliers - Q1_no_outliers
print(IQR_no_outliers)
# Q35. df의 'TotalCharges' 컬럼의 이상치를 제거한 후, 이상치 개수를 출력하시오.
lower_bound_no_outliers = Q1_no_outliers - 1.5 * IQR_no_outliers
upper_bound_no_outliers = Q3_no_outliers + 1.5 * IQR_no_outliers
outliers_no_outliers = df_no_outliers[(df_no_outliers['TotalCharges'] < lower_bound_no_outliers) | (df_no_outliers['TotalCharges'] > upper_bound_no_outliers)]
print(outliers_no_outliers.shape[0])
