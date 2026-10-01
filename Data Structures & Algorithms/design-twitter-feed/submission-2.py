class Twitter:
    def __init__(self):
        self.time = 0
        self.tweets = defaultdict(list)
        self.following = defaultdict(set)

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.tweets[userId].append((self.time, tweetId))
        self.time += 1

    def getNewsFeed(self, userId: int) -> List[int]:
        heap = []
        users = self.following[userId] | {userId}

        for user in users:
            tweets = self.tweets[user]

            if tweets:
                index = len(tweets) - 1
                time, tweetId = tweets[index]
                heap.append((-time, tweetId, user, index))

        heapq.heapify(heap)
        feed = []

        while heap and len(feed) < 10:
            _, tweetId, user, index = heapq.heappop(heap)
            feed.append(tweetId)

            if index > 0:
                index -= 1
                time, prevTweetId = self.tweets[user][index]
                heapq.heappush(
                    heap,
                    (-time, prevTweetId, user, index)
                )

        return feed

    def follow(self, followerId: int, followeeId: int) -> None:
        self.following[followerId].add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        self.following[followerId].discard(followeeId)