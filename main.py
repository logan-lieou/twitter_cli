import twitter
import yaml

def init():
    # read config
    with open(r"./config.yaml") as f:
        contents = yaml.load(f, Loader=yaml.FullLoader)
        print(contents)
        f.close()

    # get keys from config
    c_key = contents['consumer']['key']
    c_sec = contents['consumer']['sec']
    a_key = contents['token']['key']
    a_sec = contents['token']['sec']

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
    # iterate through the tweets
    for i in range(len(timeline)):
        text = timeline[i].text
        name = timeline[i].user.screen_name
        print("{0}\n{1}".format(name, text))

# main function
def main():
    api = init()
    user_selection = int(input("\nSelect an Option:\n0:\tGet Timeline\n1:\tTweet\n2:\tSearch\n3:\tQuit\n"))
    while(user_selection != 3):
        user_selection = int(input("\nSelect an Option:\n0:\tGet Timeline\n1:\tTweet\n2:\tSearch\n3:\tQuit\n"))
        # no switch statement in python??
        if (user_selection == 0):
            print("YOUR TIMELINE:\n")
            get_timeline(api)
        elif (user_selection == 1):
            pass
        elif (user_selection == 2):
            pass
        elif (user_selection == 3):
            break
        else:
            print("There was an error!")

# execute main function
if __name__ == "__main__":
    main()

