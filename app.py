
import cv2

face_cascade = cv2.CascadeClassifier("face_detector.xml")
img = cv2.imread("unmasked_image.png")
faces = face_cascade.detectMultiScale(img, 1.1, 4)
for (x, y, w, h) in faces:
	cv2.rectangle(img, (x, y), (x+w, y+h), (255, 0, 0), 2)
cv2.imwrite("face_detected.png", img)


mentions = api.mentions_timeline()



mentions[0].entities['media'][0]['media_url']

#to download
image = requests.get("https://i.imgur.com/ExdKOOz.png")
file = open("sample_image.png", "wb")
file.write(image.content)
file.close()

#for mentions in replies:
id = mentions[0].in_reply_to_status_id
tweet = api.get_status(id)
tweet.entities['media'][0]['media_url']

#to check
if 'media' in mentions[0].entities:
	for image1 in  mentions[0].entities['media']:
		print(image1['media_url'])



tweet = api.get_status(mention.in_reply_to_status_id)
if 'media' in tweet.entities:
	in_reply_url = tweet.entities['media'][0]['media_url']
	return 





api.update_status('@' + mention.user.screen_name + ' sup', mention.id)

id = api.media_upload('test.png')
api.update_status('@' + t[0].user.screen_name + ' hi', in_reply_to_status_id=t[0].id, media_ids=[id.media_id])

1301859172020039680 in reply id

1302376469373628418 media id

