import requests as req
import json 


def tmdb_api_call(requestURL,parameters):
    response = req.get(url=requestURL,params=parameters)
    if response.status_code != 200:
        print(response.json())
        exit()
    data = response.json()
    return json.dumps(data)



def get_upcoming_movies_by_page(api_key,page_number=1):
    requestURL = "https://api.themoviedb.org/3/movie/upcoming"
    parameters = {"api_key" : api_key, "page" : page_number }
    return tmdb_api_call(requestURL,parameters)


def main():
    api_key = "61fd3cddfd71c0c9755ea27ab9d235c4"
    upcoming_movie_list = get_upcoming_movies_by_page(api_key,1)
    data = json.loads(upcoming_movie_list)
    print(data["results"])
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	Quality of Task: Good
Productivity: More Than Expected
Comments:
He is working better day by day. Always Eager to Learn New Things. Does In-Depth Research on New Technologies, Did good job on all new technologies, Little Guidance can help him achieve all goal
Need to Improve Presentation Skills more with all learned data for Thorough Knowledge Sharing on Technologies/Product Showcases.
	