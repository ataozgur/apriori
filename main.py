# Given data #
total_transactions = 100
transactions_containing_bread = 70
transactions_containing_milk = 50
transactions_containing_both = 40

# Calculate metrics
support_bread = transactions_containing_bread / total_transactions
support_milk = transactions_containing_milk / total_transactions
support_both = transactions_containing_both / total_transactions

confidence_bread_to_milk = support_both / support_bread
# Confidence({bread} => {milk}) indicates that if bread is in a transaction, there's a 57.1% chance that milk is also present.

lift_bread_to_milk = confidence_bread_to_milk / support_milk
# Lift({bread} => {milk}) indicates that the presence of bread increases the likelihood of milk by about 1.142 times compared to when they are independent.

conviction_bread_to_milk = (1 - support_milk) / (1 - confidence_bread_to_milk)
# The Conviction value of approximately 1.166 suggests that the rule {bread} => {milk} is about 1.166 times more confident
# about the consequence (milk) being dependent on the antecedent (bread) than it should be if the two items were independent.
# A conviction value greater than 1 indicates that there is some level of dependency between the items, but it's not extremely strong.

leverage_bread_to_milk = support_both - (support_bread * support_milk)
# The Leverage value of 0.15 indicates that the occurrence of both bread and milk together
# in transactions is 0.15 more than what would be expected if the two items were independent.
# A positive leverage value suggests that there is some association between the items, but the value is relatively small.

precision_bread_to_milk = confidence_bread_to_milk
recall_bread_to_milk = support_both

kulczynski_bread_to_milk = 0.5 * (precision_bread_to_milk + recall_bread_to_milk)
# The Kulczynski Measure value of approximately 0.485 combines both precision and recall aspects of the rule.
# It suggests that the balance between correctly predicting the presence of milk (precision) and capturing all instances of milk
# (recall) is moderate. A higher Kulczynski Measure value indicates a better balance between precision and recall for the rule.

jaccard_bread_to_milk = 0  # Since there is no overlap between {bread} and {milk}

# Print calculated metrics
print(f"Support (bread): {support_bread}")
print(f"Support (milk): {support_milk}")
print(f"Support (bread, milk): {support_both}")
print(f"Confidence (bread => milk): {confidence_bread_to_milk}")
print(f"Lift (bread => milk): {lift_bread_to_milk}")
print(f"Conviction (bread => milk): {conviction_bread_to_milk}")
print(f"Leverage (bread => milk): {leverage_bread_to_milk}")
print(f"Kulczynski (bread => milk): {kulczynski_bread_to_milk}")
print(f"Jaccard (bread, milk): {jaccard_bread_to_milk}")