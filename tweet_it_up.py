import tweepy

from textblob import TextBlob
consumerKey = 'OwENz4tXuarnZIi0PKtmfhlh7'
consumerSecret = 'L3IOhPkMhKyFH6zAHcQEKLqRWBwDIwPdRiexcBs0j11rtkVdPO'
access_token='451334829-k8h4sCMhPTqd9JhhlqzoJcvMAZSdk6v3mlJc91cY'
access_token_secret='d6JdyHLrP1VkxXccadjlxvTN2YWi6f0IxeqtHl0jrM3lV'
auth  = tweepy.OAuthHandler(consumerKey,consumerSecret)
auth.set_access_token(access_token,access_token_secret)
api = tweepy.API(auth)
v = input("   enter the name       ")
#tweets=api.user_timeline("@TechAakash1")
#user=tweepy.Cursor(api.followers,screen_name="@TechAakash1",count=100).items()
#for tweet in user:
public_tweet = api.search(v)
#textList = str(public_tweet)
#gh = textList.split(",")
for tweet in public_tweet:
	print(tweet.text)
	analysis = TextBlob(tweet.text)
	print(analysis.sentiment)
#for line in gh:
#	tet = open("test.txt","w")
#	tet.write(str(line))
#	tet.write("\n")
#tet.close()

#user=api.get_user("@TechAakash1").followers()
#for i in range user:
#	print(i)
	