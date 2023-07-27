# %%
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import os

# %%
path_dir = "./data/instagram/"

for dirpath, dirnames, filenames in os.walk(path_dir):
    for filename in filenames:
        print(os.path.join(dirpath, filename))

# %%
df_comments = pd.read_csv(os.path.join(path_dir, "comments.csv"))
df_follows = pd.read_csv(os.path.join(path_dir, "follows.csv"))
df_users = pd.read_csv(os.path.join(path_dir, "users.csv"))
df_tags = pd.read_csv(os.path.join(path_dir, "tags.csv"))
df_photos = pd.read_csv(os.path.join(path_dir, "photos.csv"))
df_phototags = pd.read_csv(os.path.join(path_dir, "photo_tags.csv"))
df_likes = pd.read_csv(os.path.join(path_dir, "likes.csv"))
df_comments

# %%
df_comments.info()
df_comments.describe()

# %%
df_comments.isnull().sum()

# %%
df_comments["emoji used"].value_counts()

# %%
df_comments["Hashtags used count"].value_counts().plot(kind="pie", autopct="%1.1f%%")
plt.show()

# %%
df_follows

# %%
df_follows.isnull().sum()

# %%
df_follows = df_follows.replace("Private", "private")

# %%
df_follows["followee Acc status"].value_counts().plot(kind="bar")
plt.show()

# %%
df_likes

# %%
df_likes.isnull().sum()

# %%
df_likes.duplicated().sum()

# %%
df_likes["following or not"].value_counts().plot(
    kind="bar", xlabel="Following or not", ylabel="Count"
)
plt.show()

# %%
df_likes["like type"].value_counts()

# %%
df_likes["like type"].value_counts().plot(
    kind="bar", xlabel="Like type", ylabel="Count"
)
plt.show()

# %%
df_users

# %%
df_users["private/public"].value_counts()

# %%
df_users["post count"].describe()

# %%
plt.hist(df_users["post count"], range=[10, 2500])
plt.xlabel("Post count")
plt.ylabel("Count")
plt.show()

# %%
df_users["Verified status"].value_counts()

# %%
df_tags

# %%
df_tags["location"].value_counts()

# %%
df_photos

# %%
df_photos["Insta filter used"].value_counts().plot(
    kind="bar", xlabel="Was Insta Filter Used", ylabel="Count"
)
plt.show()

# %%
df_phototags

# %%
