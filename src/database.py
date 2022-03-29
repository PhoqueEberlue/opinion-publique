import sqlite3
import re


class Database:
    def __init__(self, file_name):
        self.conn = sqlite3.connect(f'{file_name}.db')
        self.generate_table()
        self.file_name = file_name

    def generate_table(self):
        """

        generate a table
        """
        self.conn.execute("CREATE TABLE IF NOT EXISTS TWEETS ( \
                     tweet_id int PRIMARY KEY NOT NULL, \
                     text TEXT, \
                     date DATETIME \
                     )")

    def add_tweet(self, tweet):
        """

        :param tweet:
        Add a tweet in the tweets table
        """
        text = self.delete_link(tweet.text)

        if not self.is_doublon(text):
            query = "INSERT INTO TWEETS (tweet_id, text, date) VALUES(?, ?, ?)"
            try:
                self.conn.execute(query, (tweet.id, text, tweet.created_at))
            except sqlite3.IntegrityError as e:
                print(e)
            self.conn.commit()

    def add_tweets(self, tweets):
        """

        :param tweets:
        Add tweet in tweets.
        """
        for tweet in tweets:
            self.add_tweet(tweet)

    def get_nb_lines(self):
        res = self.conn.execute("select count() from tweets")
        res = res.fetchall()
        return res[0][0]

    def is_doublon(self, text):
        """

        :param text:
        get duplicate tweet
        """
        text = text.replace("'", "''")
        res = self.conn.execute("select * from tweets where text='" + text + "'")
        self.conn.commit()
        print("__________________")
        print("test de doublons")
        print(text)
        res = res.fetchall()
        print(res)
        print("_______________________")
        return False if res == [] else True

    def get_tweet_count(self, keywords, date=None, hour=None):
        condition = "("
        for i, keyword in enumerate(keywords):
            condition += f"text like '%{keyword}%'"
            if i + 1 != len(keywords):
                condition += " or "
        condition += ")"

        if date is not None:
            condition += f" and date like '{date}%'"
        if hour is not None:
            condition += f" and date like '%{hour}:__:__%'"

        query = 'select count() from tweets where ' + condition
        res = self.conn.execute(query)
        res = res.fetchone()
        return res[0]

    @staticmethod
    def delete_link(text):
        """

        :param text:
        Delete a link in a tweet
        """
        return re.sub(r'http\S+', '', text)


if __name__ == "__main__":
    database = Database("president")
    print(database.get_tweet_count(""))
