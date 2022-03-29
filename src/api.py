import tweepy


class API:
    def __init__(self):
        self.client = tweepy.Client(bearer_token=self.get_bearer_token())

    def get_tweets(self, criterion):
        """

        :param criterion:
        :return: tweets, type : tweet
        """
        query = f"({' OR '.join(criterion['keywords'])}) lang:fr -is:reply -is:retweet -is:quote -@{criterion['at']}"

        print(query)
        input()
        tweets = self.client.search_recent_tweets(query,
                                                  tweet_fields=["created_at", "public_metrics"],
                                                  expansions='author_id',
                                                  max_results='10')
        return tweets.data

    @staticmethod
    def get_bearer_token(path: str = None):
        if path is None:
            path = "../token.txt"

        with open(path) as file:
            token = file.read()
        print(token)
        return token
