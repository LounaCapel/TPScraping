import requests
from bs4 import BeautifulSoup 
import json
import re


##############################################################################

# Test Functions

def Test_GetTitle () :
    assert GetTitle() == "Title : Pierre Niney : L’interview face cachée par HugoDécrypte"

def Test_GetAuthor () :
    assert GetAuthor() == "Author : HugoDécrypte"
    
def Test_GetView () :
    # Can change
    assert GetView() == "View : 732998"

def Test_GetLikes () :
    # Same prblem of variation
    assert GetLikes() == "Likes : 30 438 clics"

"""
# Launch test
Test_GetTitle()
Test_GetAuthor()
Test_GetView()
Test_GetLikes()
"""
##############################################################################





# copy youtube url from YouTube website  
#video_url = "https://www.youtube.com/watch?v=ilm6dmeOW38" 
video_url = "https://www.youtube.com/watch?v=fmsoym8I-3o" 
# init an HTML Session  
page = requests.get(video_url) 
# create bs object to parse HTML  
soup = BeautifulSoup(page.content, "html.parser")  
#print(soup)


"""
What we want to collect :

- Titre de la vidéo OK
- Nom du vidéaste OK 
- Nombre de pouces bleu OK
- Description de la vidéo (format plein text) OK
- Liens exceptionnels de la description (s’il y en a, par exemple, des liens vers un timestamp vidéo ou un compte Twitter)
- id de la vidéo youtube
- Les n premiers commentaires (s’ils existent)
"""

def GetTitle() :
    return "Title : " + soup.find("meta", itemprop="name")["content"]

def GetAuthor () :
    return "Author : " + soup.find("span", itemprop="author").next.next["content"]

def GetView () :
    return "View : " + soup.find("meta",itemprop="interactionCount")['content']  

def GetLikes () :
    data = re.search(r"var ytInitialData = ({.*?});", soup.prettify()).group(1)  
    data_json = json.loads(data)
    videoPrimaryInfoRenderer = data_json['contents']['twoColumnWatchNextResults']['results']['results']['contents'][0]['videoPrimaryInfoRenderer']  
    videoSecondaryInfoRenderer = data_json['contents']['twoColumnWatchNextResults']['results']['results']['contents'][1]['videoSecondaryInfoRenderer']  
    # number of likes  
    likes_label = videoPrimaryInfoRenderer['videoActions']['menuRenderer']['topLevelButtons'][0]['segmentedLikeDislikeButtonRenderer']['likeButton']['toggleButtonRenderer']['defaultText']['accessibility']['accessibilityData']['label'] # "No likes" or "###,### likes"  
    likes_str = likes_label.split(' ')[0].replace(',','')  
    likes = '0' if likes_str == 'No' else likes_str
    return "Likes : " + likes

def GetDescription () :
    #description = soup.find("meta", itemprop="description")["content"]
    pattern = re.compile('(?<=shortDescription":").*(?=","isCrawlable)')
    return "Description : " + pattern.findall(str(soup))[0].replace('\\n','\n')
    
def GetId () :
    with open("/data/Documents/ING3/DevOps/input.json", "r") as f:
        #video_id = json.load(f)["videos_id"]
        
    #return "Id : " + video_id

print(GetTitle())
print(GetAuthor())
print(GetView())
print(GetLikes())
print(GetDescription())
print(GetId())


#print("Title : ", title)
#print('Author : ', author)
#print("Description : ", description)

#Description :
#https://stackoverflow.com/questions/72354649/how-to-scrape-youtube-video-description-with-beautiful-soup?fbclid=IwAR139DNghEC-EC4aKOtagqYcqCI4c5XvVRYUUZe81JJNOUZ4hi2YyVQK8Gw
#Like
#https://www.javatpoint.com/how-to-extract-youtube-data-in-python?fbclid=IwAR0JZGVA67pI8L-_YER9vuXqsVqkjG0EmuZqkT_klF6laGRp_lJ8TLTBesM
#Link
#https://stackoverflow.com/questions/839994/extracting-a-url-in-python?fbclid=IwAR0ni6kqComJKUR66ZBWuSLLQdUGl4YmhyyG0P5536gBPYAYz21GVWG4tWc








# write on JSON file :
person_dict = {"name": "Bob",
"languages": ["English", "French"],
"married": True,
"age": 32
}

with open('person.txt', 'w') as json_file:
  json.dump(person_dict, json_file)