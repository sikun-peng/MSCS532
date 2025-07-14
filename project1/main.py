from RecommendationSystem import RecommendationSystem

recsys = RecommendationSystem()

# Add interactions
recsys.add_interaction("user1", "item1", 4)
recsys.add_interaction("user1", "item2", 5)
recsys.add_interaction("user2", "item1", 3)

# Index item features
recsys.index_item_by_feature("item1", ["electronics", "gaming"])
recsys.index_item_by_feature("item2", ["electronics", "laptop"])

# Get similar items
print("Similar to item1:", recsys.get_similar_items("item1"))

# Predict score
print("Predicted score for user2 on item2:", recsys.predict_score("user2", "item2"))

# Rank top-N
candidates = recsys.get_similar_items("item1") | {"item2"}
print("Top recommendations for user2:", recsys.rank_top_n("user2", candidates))