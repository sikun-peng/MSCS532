import heapq
from collections import defaultdict
from functools import lru_cache

class RecommendationSystem:
    def __init__(self):
        self.user_item_matrix = defaultdict(dict)
        self.inverted_index = defaultdict(set)
        self.item_features = defaultdict(set)
        self.item_ratings_sum = defaultdict(int)
        self.item_ratings_count = defaultdict(int)
        self.global_avg = 0.0
        self.total_ratings_count = 0

    def add_interaction(self, user_id, item_id, rating):
        self.total_ratings_count += 1
        self.global_avg = (self.global_avg * (self.total_ratings_count - 1) + rating) / self.total_ratings_count

        if item_id in self.user_item_matrix[user_id]:
            old_rating = self.user_item_matrix[user_id][item_id]
            self.item_ratings_sum[item_id] -= old_rating
            self.item_ratings_count[item_id] -= 1
        self.user_item_matrix[user_id][item_id] = rating
        self.item_ratings_sum[item_id] += rating
        self.item_ratings_count[item_id] += 1

    def index_item_by_feature(self, item_id, features):
        self.item_features[item_id] = set(features)
        for feature in features:
            hashed_feature = self._hash_feature(feature)
            self.inverted_index[hashed_feature].add(item_id)

    def _hash_feature(self, feature, num_buckets=1000):
        return hash(feature.strip().lower()) % num_buckets

    @lru_cache(maxsize=10000)
    def predict_score(self, user_id, item_id):
        if self.item_ratings_count[item_id] == 0:
            return self.global_avg
        return self.item_ratings_sum[item_id] / self.item_ratings_count[item_id]

    def get_similar_items(self, item_id):
        features = self.item_features[item_id]
        similar = set()
        for f in features:
            hashed_f = self._hash_feature(f)
            similar |= self.inverted_index[hashed_f]
        similar.discard(item_id)
        return similar

    def rank_top_n(self, user_id, candidate_items, N=10):
        scores = [(self.predict_score(user_id, item), item) for item in candidate_items]
        return heapq.nlargest(N, scores, key=lambda x: x[0])