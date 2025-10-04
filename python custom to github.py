#handling path and the requests
import requests
import os

#defining the function
def custom_search(query=None):
    #see if there's a query or not
    if query==None:
        query = input("Put your query")
    #path
    path = os.path.join("path/to/directory")
    #url
    url = "https://www.googleapis.com/customsearch/v1"
    api_key = open(f"{path}\\Apikey","r").read()#the api_key to custom search
    custom_search_id = open(f"{path}\\Customsearch","r").read()#the custom search id, to see which one is using it
    #see if the person using wants images or not
    if input("Do you want to retrive images?(Y/N)").lower() == "y":
        #params for yes
        params = {
            "q":query,
            "key":api_key,
            "cx":custom_search_id,
            "searchType":"image"
        }
    else:
        #params for no
        params = {
            "q":query,
            "key":api_key,
            "cx":custom_search_id
        }
    #error handling
    try:
        #get response and files
        response = requests.get(url, params=params)
        response.raise_for_status()
        results = response.json()
        #if there are no items then it raise an exception
        if "items" not in results:
            raise Exception("No items")
        else:
            return results
    except Exception as e:
        print(e)

#if you are running this program then it runs the custom search
if __name__ == "__main__":
    print(custom_search())
    


