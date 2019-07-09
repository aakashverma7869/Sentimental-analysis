import twitter
from textblob import TextBlob
consumerKey = 'OwENz4tXuarnZIi0PKtmfhlh7'
consumerSecret = 'L3IOhPkMhKyFH6zAHcQEKLqRWBwDIwPdRiexcBs0j11rtkVdPO'
access_token='451334829-k8h4sCMhPTqd9JhhlqzoJcvMAZSdk6v3mlJc91cY'
access_token_secret='d6JdyHLrP1VkxXccadjlxvTN2YWi6f0IxeqtHl0jrM3lV'
api = twitter.Api(consumer_key = consumerKey , consumer_secret = consumerSecret , access_token_key = access_token , access_token_secret = access_token_secret)
#print(api.VerifyCredentials())
#friends = api.GetFriends(screen_name ="@TechAakash1")
#print(friends)
followers = api.GetFollowers(screen_name = "@rockamar41")
#for tweet in followers:
	#print(tweet,"\n"*5)
textList = str(followers)
gh = textList.split(",")
#print(followers)
for line in gh:
	tet = open("fol.txt","w")
	tet.write(str(line))
	tet.write("\n")
tet.close()
#user = list(api.GetFollowers(screen_name='@TechAakash1'))
#use = list(user.txt)
#print(use.split("["))
#test_file =  open ("test.txt","w")
#test_file.write(user)
#test_file.close()
#auth  = tweepy.OAuthHandler(consumerKey,consumerSecret)
#auth.set_access_token(access_token,access_token_secret)
#api = tweepy.API(auth)
#tweets=tweepy.Cursor(api.followers,screen_name="@mauryan98",count=100).items()
#tweets=api.followers("@TechAakash1")
#for tweet in tweets:
#    print(tweets.screen_name("@TechAakash1"))

