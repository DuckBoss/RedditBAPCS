import praw


class RedditBAPCS:

    redditInstance = None
    subredditInstance = None
    submissions = None

    # Keywords/Categories Lists -
    listing_seek = ["GTX1080", "I7-7700K"]
    # Available Categories Include - GPU,CPU,PSU,RAM,HDD,SSD,MOBO,COOLER,KEYBOARD,MOUSE,MONITOR,CASE,LAPTOP,HEADPHONES,FAN,WEBCAM,ETC...
    listing_category = ["GPU", "CPU", "PSU"]
    
    # Optional Parameters -
    allow_stream = True #DEFAULT True
    search_limit = 1024 #DEFAULT 1024

    def __init__(self):
        print("RedditBAPCS Initialized!")
        self.redditInstance = praw.Reddit('bot1')
        self.subredditInstance = self.redditInstance.subreddit("buildapcsales")

        print("Current User: %s" % self.redditInstance.user.me())


    def main(self):
        self.scan_submissions()

    def scan_submissions(self):
        print("Historical Scan Starting!")
        self.submissions = list(self.subredditInstance.new(limit=self.search_limit))

        for submission in self.submissions:
            flair = submission.link_flair_text
            if flair:
                if any(x in flair for x in self.listing_category):
                    if any(x in str.upper(submission.title) for x in self.listing_seek):
                        self.print_listing(submission)

        if self.allow_stream:
            self.stream_scan_submissions()

        print("Historical Scan Complete!")

    def stream_scan_submissions(self):
        print("Realtime Scan Starting!")
        for submission in self.subredditInstance.stream.submissions():
            flair = submission.link_flair_text
            if flair:
                if any(x in flair for x in self.listing_category):
                    if any(x in str.upper(submission.title) for x in self.listing_seek):
                        self.print_listing(submission)

        print("Realtime Scan Complete!")

    @staticmethod
    def print_listing(listing):
        print("\nListing: %s \nCategory: %s \nLink: %s\n" % (listing.title, listing.link_flair_text, listing.url))



if __name__ == "__main__":
    redditBCAPS = RedditBAPCS()
    redditBCAPS.main()
