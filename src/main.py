from database import Database
from api import API
import json
import subprocess


class Bot:
    def __init__(self, database_path):
        self.database = Database(database_path)
        self.api = API()
        self.criteria = None

    def load_criteria(self, path="search_criteria.json"):
        """

        :param path:
        Load the criteria
        """
        with open(path) as file:
            self.criteria = json.loads(file.read())

    def fetch_api(self):
        """

        Fetch the api
        """
        if self.criteria is None:
            self.load_criteria()
        for criterion in self.criteria:
            self.database.add_tweets(self.api.get_tweets(criterion))


if __name__ == "__main__":
    bot = Bot("president")
    bot.fetch_api()
    bot.database.conn.close()
    list()
