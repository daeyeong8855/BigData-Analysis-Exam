import pandas as pd
df = pd.read_csv('https://raw.githubusercontent.com/Datamanim/datarepo/main/churn/train.csv')
# Q1. df의 상위 5개 행을 출력하시오.
print(df.head())
# Q2. df의 행과 열의 개수를 출력하시오.
print(df.shape) 

# 열만
len(df.columns)
# df.shape의 결과는 (행의 개수, 열의 개수) 형태의 튜플입니다.
print(df.shape)     # 출력 예시: (10000, 5)
# 여기서 두 번째 값([1])을 지정하면 열의 개수만 쏙 가져옵니다.
col_count = df.shape[1]
print(col_count)    # 출력 예시: 5



# Q3. df의 컬럼명을 출력하시오.
print(df.columns)
# Q4. df의 데이터 타입을 출력하시오.
print(df.dtypes)
# Q5. df의 결측치 개수를 출력하시오.
print(df.isnull().sum())
# Q6. df의 'TotalCharges' 컬럼의 데이터 타입을 float으로 변환하시오.
df['TotalCharges'] = pd.to_numeric(df['TotalCharges'], errors='coerce')
errors='raise': (기본값) 에러가 나면 코드를 중단합니다.
errors='coerce': 에러가 나는 값은 무조건 NaN으로 뭉개고 진행합니다. (가장 애용됨)
errors='ignore': 에러가 나면 타입을 바꾸지 않고 원본 그대로 둡니다.

df['view_count'] = df['view_count'].astype('float')

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


pd.to_datetime(df[], format=())
df['날짜'].dt.year # 연도 
df['날짜'].dt.month # 월 
df['날짜'].dt.day # 일 
df['날짜'].dt.hour # 시 
df['날짜'].dt.minute # 분 
df['날짜'].dt.second # 초 
df['날짜'].dt.weekday # 요일 (0=월요일) 
df['날짜'].dt.date # 날짜만 (datetime.date) df['날짜'].dt.time # 시간만 (datetime.time)