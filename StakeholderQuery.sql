SELECT 
  SUM(purchasedItemCount) as TotalItemsPurchased, 
  AVG(totalSpent) as AverageSpend, 
  rewardsReceiptStatus 
from 
  "Receipts"."Receipts Data" 
WHERE 
  rewardsReceiptStatus IN ('ACCEPTED', 'REJECTED') 
GROUP BY 
  rewardsReceiptStatus;
