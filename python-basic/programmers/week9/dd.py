import pandas as pd

amazon_ratings = pd.read_csv("https://grepp-reco-test.s3.ap-northeast-2.amazonaws.com/ratings_Beauty.csv")
amaRatings = amazon_ratings.pivot_table(index=['UserId'], columns=['ProductId'], values='Rating')