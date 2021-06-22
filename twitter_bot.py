import tweepy
import requests
import time
import cv2

CONSUMER_KEY = [redacted]
CONSUMER_SECRET = [redacted]
ACCESS_KEY = [redacted]
ACCESS_SECRET = [redacted]

auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_KEY, ACCESS_SECRET)
api = tweepy.API(auth)

FILE_NAME = 'last_seen_id.txt'

def retrieve_last_seen_id(file_name):
    f_read = open(file_name, 'r')
    last_seen_id = int(f_read.read().strip())
    f_read.close()
    return last_seen_id

def store_last_seen_id(last_seen_id, file_name):
    f_write = open(file_name, 'w')
    f_write.write(str(last_seen_id))
    f_write.close()
    return

def check_in_reply_to_media(in_reply_to_status_id):
	if in_reply_to_status_id:
		tweet = api.get_status(in_reply_to_status_id)
		if 'media' in tweet.entities:
			global in_reply_url
			in_reply_url = tweet.entities['media'][0]['media_url']
			return 1
	else:
		in_reply_url = '0'
		return 

def superimpose_masks(unmasked_image_url):
	image = requests.get(unmasked_image_url)
	file = open("unmasked_image.png", "wb")
	file.write(image.content)
	file.close()
	face_cascade = cv2.CascadeClassifier("face_detector.xml")
	img = cv2.imread("unmasked_image.png")
	faces = face_cascade.detectMultiScale(img, 1.1, 4)
	for (x, y, w, h) in faces:
		cv2.rectangle(img, (x, y), (x+w, y+h), (255, 0, 0), 2)
	cv2.imwrite("masked_image.png", img)
	masked_image = api.media_upload('masked_image.png')
	return masked_image



last_seen_id = retrieve_last_seen_id(FILE_NAME)
mentions = api.mentions_timeline(
                        last_seen_id,
                        tweet_mode='extended')
for mention in reversed(mentions):
	in_reply_url = '0'
	last_seen_id = mention.id
	store_last_seen_id(last_seen_id, FILE_NAME)
	if ('media' in mention.entities) or (check_in_reply_to_media(mention.in_reply_to_status_id)):
		if not in_reply_url.isnumeric():
			masked_image = superimpose_masks(in_reply_url)
		else:
			masked_image = superimpose_masks(mention.entities['media'][0]['media_url'])
		api.update_status(
			'@' + mention.user.screen_name + ' stay safe', 
			in_reply_to_status_id=mention.id, 
			media_ids=[masked_image.media_id])
		

























