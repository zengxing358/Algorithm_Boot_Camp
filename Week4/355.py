class User:
    def __init__(self) -> None:
        self.postTweet={}
        self.postTime=[]
        self.capcity=10
        self.fllow=set()
    def postw(self,tweetId,time):
        self.postTweet[time]=tweetId
        self.postTime=[time]+self.postTime
        if len(self.postTweet)>10:
            self.postTweet.pop(self.postTime.pop())
    def fllower(self,followeeId):
        self.fllow.add(followeeId)
    def unfllower(self,followeeId):
        if followeeId in self.fllow:
            self.fllow.remove(followeeId)
    def getNews(self):
        return self.postTweet
    def getfollow(self):
        return self.fllow

class Twitter:
    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.user={}
        self.time=0

    def postTweet(self, userId: int, tweetId: int) -> None:
        """
        Compose a new tweet.
        """
        if userId not in self.user:
            self.user[userId]=User()
        self.user[userId].postw(tweetId,self.time)
        self.time+=1

    def getNewsFeed(self, userId: int) -> List[int]:
        """
        Retrieve the 10 most recent tweet ids in the user's news feed. Each item in the news feed must be posted by users who the user followed or by the user herself. Tweets must be ordered from most recent to least recent.
        """
        if userId not in self.user:
            self.user[userId]=User()
            return []
        news=self.user[userId].getNews().copy()
        for follow in self.user[userId].getfollow():
            news.update(self.user[follow].getNews())
        t=sorted(news,reverse=True)[:10]
        res=[]
        for i in t:
            res.append(news[i])
        return res

    def follow(self, followerId: int, followeeId: int) -> None:
        """
        Follower follows a followee. If the operation is invalid, it should be a no-op.
        """
        if followerId!=followeeId:
            if followerId not in self.user:
                self.user[followerId]=User()
            if followeeId not in self.user:
                self.user[followeeId]=User()
            self.user[followerId].fllower(followeeId)


    def unfollow(self, followerId: int, followeeId: int) -> None:
        """
        Follower unfollows a followee. If the operation is invalid, it should be a no-op.
        """
        if followerId!=followeeId:
            if followerId not in self.user:
                self.user[followerId]=User()
            if followeeId not in self.user:
                self.user[followeeId]=User()
            self.user[followerId].unfllower(followeeId)



# Your Twitter object will be instantiated and called as such:
# obj = Twitter()
# obj.postTweet(userId,tweetId)
# param_2 = obj.getNewsFeed(userId)
# obj.follow(followerId,followeeId)
# obj.unfollow(followerId,followeeId)