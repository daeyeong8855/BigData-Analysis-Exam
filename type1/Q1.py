# 이 데이터는 날짜별 트렌딩 기록이다. 같은 영상은 channelTitle과 title이 모두 같은 경우로 본다. 날짜순으로 정렬했을 때, 전날에도 트렌딩에 있었고 dislike 수가 전일보다 증가한 날이 가장 길게 이어진 영상의 channelTitle을 출력하라

import pandas as pd
import kagglehub

# Download latest version
path = kagglehub.dataset_download("thedevastator/youtube-trending-videos-dataset")
# 데이터 불러오기
df = pd.read_csv(path + "/youtube.csv")

print(df.head())
