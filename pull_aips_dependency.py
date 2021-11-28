import sys
sys.path.append('..')
import requests

def pull_dependency(file_name):
  print ("Pulling: \"" + file_name + "\"")
  with open(file_name, "wb") as file:
    for part in map(chr,range(ord('a'),ord('z')+1)):
      part_name = "part_" + str(part)
      url = "https://github.com/ai-powered-search/outdoors/raw/master/" + file_name + "." + part_name
      response = requests.get(url)
      if response.status_code == 200:
        print("Successfully downloaded " + part_name)
        file.write(response.content)
      elif response.status_code == 404:
        print('404')
        break
      else:
        raise Exception("Error: Status Code " + response.status_code + "\n" + response.text)
  print(file_name + " successfully pulled")

if len(sys.argv) == 2:  
  pull_dependency(sys.argv[1])