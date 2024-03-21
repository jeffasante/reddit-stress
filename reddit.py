import praw, random

# variables
user_agent = 'Comment Extraction (by u/jeffasante)'
client_id = 'INSERT YOUR [client_id]'
client_secret = 'INSERT YOUR [client_secret]'

# Instantiate the Reddit API client with your credentials
reddit = praw.Reddit(client_id=client_id,
                    client_secret=client_secret, 
                    user_agent=user_agent,
                    password="0244760285",
                    username="jeffasante")


def fetch_reddit(reddit=reddit):
                        
    url = 'https://www.reddit.com/r/Stress/comments/fwes89/free_covid19_anxiety_eworkbook_please_take_care/'
    submission = reddit.submission(url=url)

    corpus = []
    for top_level_comment in submission.comments:
        comment = top_level_comment.body 
        corpus.append(comment)
        # print(comment)
    
    return corpus


def fetch_more_reddit(reddit=reddit):

    # fetch subreddit posts 
    subreddit_name = 'Stress'

    # Get a subreddit object
    subreddit = reddit.subreddit(subreddit_name)

    urls_titles = []
    urls = {}

    # Fetch the hottest posts in the subreddit
    for submission in subreddit.hot(limit=10):
        urls_titles.append(submission.title)
        urls[submission.title] = submission.url

    while True:
        url_choice = random.choice(urls_titles)
        print('url_choice', url_choice)

        submission = reddit.submission(url=urls[url_choice])

        corpus = []
        for top_level_comment in submission.comments:
            comment = top_level_comment.body 
            corpus.append(comment)

        if len(corpus) < 2:
            continue
        else:
            break

    print('\n corpus', corpus)

    return corpus, url_choice

