import twitter
import yaml

def init():
    # read config
    with open(r"./config.yaml") as f:
        contents = yaml.load(f, Loader=yaml.FullLoader)
        f.close()

    # get keys from config
    c_key = contents['consumer']['key']
    c_sec = contents['consumer']['sec']
    a_key = contents['token']['key']
    a_sec = contents['token']['sec']

    # if any of the expected contents are missing
    if (c_key == "" or c_sec == "" or a_key == "" or a_sec == ""):
        # this creates an error that I can catch yes I know this is bad
        return broken 

    # initialize the api
    api = twitter.Api(consumer_key = c_key,
                      consumer_secret = c_sec,
                      access_token_key = a_key,
                      access_token_secret = a_sec)
    # return the api
    return api


def get_timeline(api):
    # get timeline
    timeline = api.GetHomeTimeline()

    # output the tweets
    for i in range(len(timeline)):
        text = timeline[len(timeline)-1-i].text
        name = timeline[len(timeline)-1-i].user.screen_name
        coor = timeline[len(timeline)-1-i].created_at
        print("\n{0}\n{1}\n{2}\n".format(name, text, coor))

def send_tweet(api):
    post = str(input("> "))
    api.PostUpdates(post)

def lookup_tweets(api):
    search = str(input("Search Term: "))
    # query string after q= is the search term we're looking for all the other params are less important
    results = api.GetSearch(raw_query="q={0}%20&result_type=recent&since=2014-07-19&count=100".format(search))

    # output the tweets
    for i in range(len(results)):
        text = results[len(results)-1-i].text
        name = results[len(results)-1-i].user.screen_name
        coor = results[len(results)-1-i].created_at
        print("\n{0}\n{1}\n{2}\n".format(name, text, coor))

# main function
def main():
    # catch the error
    try:
        api = init()
    except NameError:
        print("Error keys missing from config.yaml")
        return

    # initialize user selection
    user_selection = 4
    # while loop
    while(user_selection != 3):
        try:
            user_selection = int(input("\nSelect an Option:\n0:\tGet Timeline\n1:\tTweet\n2:\tSearch\n3:\tQuit\n"))
        except ValueError:
            print("Enter a valid value!")
        # no switch statement in python??
        if (user_selection == 0):
            get_timeline(api)
        elif (user_selection == 1):
            send_tweet(api)
        elif (user_selection == 2):
            lookup_tweets(api)
        elif (user_selection == 3):
            # does nothing the loop quits on it's own
            break
        else:
            # for out of bounds such as user_selection = 4
            print("There was an error!") 

# execute main function
if __name__ == "__main__":
    main()

