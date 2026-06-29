import pandas as pd
import numpy as np
import datetime as dt

# Set seed for reproducibility
np.random.seed(42)

rows = 100
base_date = dt.datetime(2023, 1, 1)

data = {
    'Impressions': np.random.randint(1000, 20000, size=rows),
    'From Home': np.random.randint(500, 10000, size=rows),
    'From Hashtags': np.random.randint(100, 5000, size=rows),
    'From Explore': np.random.randint(50, 2000, size=rows),
    'From Other': np.random.randint(10, 500, size=rows),
    'Saves': np.random.randint(10, 500, size=rows),
    'Comments': np.random.randint(5, 100, size=rows),
    'Shares': np.random.randint(2, 50, size=rows),
    'Likes': np.random.randint(50, 2000, size=rows),
    'Profile Visits': np.random.randint(10, 300, size=rows),
    'Follows': np.random.randint(0, 50, size=rows),
    'Caption': ["Check out this #tech insight! #marketing #data" for _ in range(rows)],
    'Hashtags': ["#tech #marketing #data" for _ in range(rows)],
}

# Add some variation to captions/hashtags
captions = [
    "Amazing day at Alfido Tech! #alfidotech #innovation",
    "Data is the new oil. #dataanalytics #bigdata #tech",
    "How to optimize your Instagram? #socialmedia #marketingtips",
    "New reel alert! #reels #viral #trending",
    "Join our community today. #community #growth",
    "Tech tips Tuesday! #techtips #coding #development",
    "The future of AI. #ai #machinelearning #future",
    "Behind the scenes. #worklife #office #culture",
    "Success is a journey. #motivation #success",
    "Analytical thinking 101. #analytics #strategy"
]
data['Caption'] = [np.random.choice(captions) for _ in range(rows)]

# Add Followers if missing, as preferred by the logic
data['Followers'] = np.random.randint(5000, 50000, size=rows)

df = pd.DataFrame(data)
df.to_csv('c:/Users/Admin/Desktop/Instagram_Analysis/dataset/instagram.csv', index=False)
print("Mock dataset created at dataset/instagram.csv")
