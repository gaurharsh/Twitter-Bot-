import twitter
import datetime
api= twitter.Api(consumer_key = 'VZKAz9cluWKChugolV3hNCzK8',
consumer_secret = 'atPXOF7fcUyI1WMhH43HvLfVpmxG8b5xFRo5iezubIX1NWFSFt',
access_token_key=  '1127472838175100928-8100wEMBhTlwOmJ8WP9yFA8nWP1Q6k',
access_token_secret = 'JncROZf6GlITOZ6xzebg2mPyRPUabL1FIH5zCM2wopwfs')

# Get the current date
today= datetime.datetime.now()

#construct the tweet message
tweet_text = f"Today date is {today.strftime('%B %d , %Y')}..."


#post the tweet
api.PostUpdate(tweet_text)