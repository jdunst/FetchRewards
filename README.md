# FetchRewards
Repo for the purposes of the assignment provided by Fetch Rewards

Notes on 1)
1. I created the database diagram in a program called DeZign since I did not currently have one installed on my computer. Whether or not this played to advantage is up for debate,
but that's the application that that "File" is expecting. Otherwise, I included the screensnip. My methodology was as follows:

Data flows downwards from the users table, but laterally from the brands table. My thinking was that we don't generate data on receipts
for a customer who hasn't installed and created an account on our app. However, it is entirely possible we may be ingesting a large range
of brands at any given time, so that should not depend on other tables. Receipts also should not depend on brands because it's possible
to purchase something that we don't know about, so at best we hope that we have all brands, but it's not guaranteed.

2. The link between Receipts and Brands is the match between the barcode element inside the Receipts.rewardsReceiptItemList array column and 
the Brand.barcode column. I considered mapping rewardsReceiptItemList into its own "Items" table, but ultimately decided that scaling that
out would lead to performance issues extremely quickly, since customers may purchase hundreds of things at a time, possibly in quick
succession, which would cause it to be a reporting table of little value.

Notes on 2)
1. Not much to add here! Query provided answers bullets 3 and 4.

Notes on 3)
1. No notes to add here! Found data quality issues within a matter of minutes so I did not delve past finding two issues.

Notes on 4)
1. No notes here! I have an English background so I tend to lean towards verbose rather than brief, so sorry if it's longer than expected!

Lastly, thanks for the opportunity! Enjoyed doing this!
