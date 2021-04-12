import pandas as pd

# Create our receipts dataframe and clean up the dictionary-type _id column
# This assumes that our _id column will have a single value in the dictionary which makes sense
# but theoretically is not guaranteed if something were to go terribly wrong
df_rec = pd.read_json(r'C:\Users\Joey\GitHub\Repos\FetchProj\receipts.json', lines=True)
df_rec['_id'] = pd.json_normalize(df_rec['_id'])

# Create our list of customers that live in our receipts data
receiptcustomers = df_rec['userId'].unique().tolist()

# Create our users dataframe and clean up the dictionary_type _id column. This once again
# assumes a single-value dictionary in that dataframe column
df_use = pd.read_json(r'C:\Users\Joey\GitHub\Repos\FetchProj\users.json', lines=True)
df_use['_id'] = pd.json_normalize(df_use['_id'])

# Display how many rows there are total
print(len(df_use))

# Versus how many unique user IDs we have. This suggests we are not treating user_id as unique, which we should
# Importing this data would require cleanup before we could be certain that we're maintaining a single account
# for a single customer
uniquecustomers = df_use['_id'].unique()
print(len(df_use['_id'].unique()))

# Bonus data issue
# Identify customers who we have receipts for that don't exist in our system
for customer in receiptcustomers:
    if customer not in uniquecustomers:
        print(customer)

# The above either a non-logical flow of receipts that belong to customers not in our system
# or that we are not cleaning up receipts for customers who are no longer in the system
# OR that we are maintaining receipts for customers who have left (and maybe returned), but we don't necessarily
# have a system in place to ensure that a returning customer would then maintain their history






