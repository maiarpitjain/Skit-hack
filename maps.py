def get_distance(dest):
    # importing required libraries 
    import requests, json 
    source='b2 bypass, Jaipur'
    # enter your api key here 
    api_key ='AIzaSyDHZvKpFeTiCAw5DSMh40S5ulmQscyCGto'

    # Take source as input  

    # Take destination as input 


    # url variable store url 
    url ='https://maps.googleapis.com/maps/api/distancematrix/json?units=imperial&'
    #url2=https://maps.googleapis.com/maps/api/distancematrix/json?units=imperial&origins=Washington,DC&destinations=New+York+City,NY&key=AIzaSyDHZvKpFeTiCAw5DSMh40S5ulmQscyCGto
    # Get method of requests module 
    # return response object 
    r = requests.get(url + 'origins=' + source +
                    '&destinations=' + dest +
                    '&key=' + api_key) 
                        
    # json method of response object 
    # return json format result 
    x = r.json() 

    # bydefault driving mode considered 

    # print the vale of x 
    y=x['rows'][0]['elements'][0]['duration']['text'] 

    print(y)
    l=''
    if 'hour' in y:
        #l=l+y[0]
        a=y.find('r')
        l=l+y[0:2]+y[a+2:a+4]
        return y[0:2] , y[a+2:a+4]
    else:
        return False ,y[0:2]

