import pandas as pd

ad_clicks = pd.read_csv('python_shoeFly_project.csv')
#print(ad_clicks.head())

#checking which ad gets the most veiws
most_add_clicks = ad_clicks.groupby('utm_source')\
.user_id.count().reset_index()
print(most_add_clicks)

#checking to see who actually clicked on the ad displayed
ad_clicks['is_click'] = ad_clicks.ad_click_timestamp.notnull()
#print(ad_clicks.head())

#checking clicks by source
clicks_by_source = ad_clicks.groupby(['utm_source', 'is_click'])\
.user_id.count().reset_index()
print(clicks_by_source)

#creating a pivot to make the data easier to understand
clicks_pivot = clicks_by_source.pivot(
  columns='is_click',
  index='utm_source',
  values='user_id').reset_index()
print(clicks_pivot)

#Function to calculate percent clicked to cut down on duplicate code
def add_percent_clicked(df):
    df['percent_clicked'] = df[True] / (df[True] + df[False])
    return df

#Calculate the percent of users who clicked from each source
clicks_pivot = add_percent_clicked(clicks_pivot)
print(clicks_pivot)

#comparing how many saw ads A vs B
clicks_by_group = ad_clicks.groupby(['experimental_group']).user_id.count().reset_index()
print(clicks_by_group)

#creating a group for our pivot
percentage_by_ad = ad_clicks.groupby(['experimental_group', 'is_click'])\
.user_id.count().reset_index()
print(percentage_by_ad)

#making our ad pivot
percentage_by_ad_pivot = percentage_by_ad.pivot(
  columns='is_click',
  index='experimental_group',
  values='user_id').reset_index()
print(percentage_by_ad_pivot)

#adding  a column to our pivot to check percentage per ad
percentage_by_ad_pivot = add_percent_clicked(percentage_by_ad_pivot)
print(percentage_by_ad_pivot)

#creating new dataframes for both A and B clicks
a_clicks = ad_clicks[ad_clicks.experimental_group == 'A']\
.reset_index(drop=True)
b_clicks = ad_clicks[ad_clicks.experimental_group == 'B']\
.reset_index(drop=True)

#grouping A clicks
percent_a_clicks = a_clicks.groupby(['is_click', 'day'])\
.user_id.count().reset_index()

#A clicks pivot
percent_a_clicks_pivot = percent_a_clicks.pivot(
  columns='is_click',
  index='day',
  values='user_id').reset_index()

#Calculate the percentage of users who clicked Ad A by day
percent_a_clicks_pivot = add_percent_clicked(percent_a_clicks_pivot)
print(percent_a_clicks_pivot)

#grouping B clicks
percent_b_clicks = b_clicks.groupby(['is_click', 'day'])\
.user_id.count().reset_index()

#B clicks pivot
percent_b_clicks_pivot = percent_b_clicks.pivot(
  columns='is_click',
  index='day',
  values='user_id').reset_index()

#Calculate the percentage of users who clicked Ad B by day
percent_b_clicks_pivot = add_percent_clicked(percent_b_clicks_pivot)
print(percent_b_clicks_pivot)

print("Based on the weekly click rates, we recommend Ad A because it preformed better over Ad B")
