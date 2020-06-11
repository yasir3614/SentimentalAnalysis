import tweepy
import random
import time
import lorem

# Authenticate to Twitter
auth = tweepy.OAuthHandler("uWMdjmYr3gIZNkKrX5Zahv3wj", "k5RjvEas7roGc7wvYK2smbDcpgIg896BxPXaXy1N9gtPlAXqDf")
auth.set_access_token("1316999414-1PvkeUiTxwdF04oytlF83SBTe3dzxHlNOhcBy4P", "YNF2FiBglmwQ2lylkaOXmUtzGsILphi4QiGZyEfTejY46")

# Create API object
api = tweepy.API(auth)

# Create a tweet


tags  = "#Headphoneshow #WaqarZaka #TechnologyMovementPakistan #TehreekETech "
# msg = ["Poor country like Venezuela had received $735 million on the first day of a pre-sale of the country's “petro” cryptocurrency","Iranian President Hassan Rouhani says the Muslim world needs its own cryptocurrency, here is a Pakistani Muslim team ","In currency CORONA situation how Pakistan is planning to earn money or after this crisis? there is no product except this","Plz see @ImranKhanPTI @DRezaBaqir that @binance  has set up a $50 million Crypto technology fund for India, weeks after the Supreme Court struck down the curbs on cryptocurrency trade in the country.","Because of Corona India’s CoinDCX, has raised $3 million from backers including Bain Capital Ventures, signaling that global investors are drawn to the space","Because of Corona, Italian Bank Opens Bitcoin Trading to 1.2 Million during LockDown, @ImranKhanPTI we need to listen #WaqarZaka ","Growing crypto adoption and the COVID-19 outbreak has encouraged Italy’s Banco Sella to launch a Bitcoin trading service" , "South Korea burning cash to prevent spreading the coronavirus & Seoul, led a government initiative to introduce its own cryptocurrency","Small Crypto company Block.One raised a record-breaking $4.1 billion in a year, why @ImranKhanPTI @DRezaBaqir is not listening to #WaqarZaka","Why @ImranKhanPti is not giving chance to #WaqarZaka team #Tenup to work for free to bring Crypto investment in Pakistan ? ","I guess #Tenup is a Pakistani engineers team, is that the reason @ImranKhanPti is not allowing them to work? www.tenup.io Wallets & crypto Exchange is ready for use","Sir @ImranKhanPti @ @DRezaBaqir why don’t you ask your team to download Wallets from www.tenup.io , test and see its whitepaper ","Sir @ImrankhanPti @DrezaBaqir PayPal is not willing to come to Pakistan, Now Crypto exchanges are also delisting us, why don’t u listen ","Crypto is digital Assets, its not a currency of any country, its simply a digital Gold which the world is enjoying, why PAK is not in the race of collecting more digital ","Crypto is not an investment plan, it’s the internet of money, just like internet changed the world of information","If Bitcoin is financially terrorist activities then why all modern the countries allowed Bitcoin ATM since 2014?","FBR will get real-time tax if Govt allows cryptocurrency, common Pakistani can trade with the world anytime and FBR & State bank can monitor ", "FATF can easily BAN crypto but why FATF in Japan recently stated countries should work on Crypto KYC & AML","There is no way Crypto mining machines can transfer money outside Pakistan, these machines can only bring money in and State bank can easily keep track of all transactions ","Frauds with currency notes are already happening in Pakistan, double shah type ponzi schemes too"]
# # msg = ["Wa	qar Zaka Kia Topic Hona Chayay? ","What should be the topic? "]
# # msg = ["May Allah Forgive our mistakes and forgive all the muslims around the globe! ","This night is the night of forgiveness ", "This is the night you can repent for your sins! ", "Wo He Khuda hay, Nizam e Hasti Chala Raha Hay "]
# msg=[' Imran Khan Has taken the most viable solutions yet ',' Imran Khan has been doing a great job ' , ' Imran khan you are doing best for the nation! ']
msg = ["Literally bought headphones for this show xD","This show helped me in quaranteene haha <3","One of the best time pass show :P","Technology overlaps education yet we are stuck in 1997 with out dated books.","We need a educational revolution asap. I stand with Waqar!","Waqar zaka has started the most prominent movement yet!","We need more people in with waqar zaka to support his movement","Big Companies are not investing in technology movement for pakistan. They should step up their game!"]
# print(msg)

def myFun():
	try:
		t = lorem.sentence()
		api.update_status(tags + msg[random.randint(0,len(msg)-1)] +  str(random.randint(0,9999)))
		x=random.randint(2,4)
		print(x)
		time.sleep(x)
	except:
		print("Exception Waiting")
		time.sleep(60)
		print("Done With Sleep 20")
		myFun()
while(1>=1):
	myFun()

# def myFun():
# 	for tweet in tweepy.Cursor(api.search, q=('#TechnologyMovementPakistan -filter:retweets')).items(5):
# 		try:
# 			# Add \n escape character to print() to organize tweets
# 			print('\nTweet by: @' + tweet.user.screen_name)

# 			# Retweet tweets as they are found
# 			tweet.retweet()
# 			api.update_status(tags + msg[random.randint(0,len(msg)-1)] +  str(random.randint(0,9999)))
# 			print('Retweeted the tweet')

# 		except tweepy.TweepError as e:
# 			myFun()


	

# for tweet in tweepy.Cursor(api.search, q=('#Arduino OR #GIS OR #Python OR #Triathlon-filter:retweets'),lang='en').items(10):
#             try:
#                 # Add \n escape character to print() to organize tweets
#                 print('\nTweet by: @' + tweet.user.screen_name)

#                 # Retweet tweets as they are found
#                 tweet.favorite()
#                 print('Like the tweet')

#                 time.sleep(5)

#             except tweepy.TweepError as e:
#                 print(e.reason)

#             except StopIteration:
#                 break