import requests


url = "https://webhacking.kr/challenge/web-03/index.php?"

QueryString2=""

for x in range(16777255, 16877255):
    Querystring = str(bin(x))[2::]
    print(len(Querystring))
    for y in range(0,25):
        QueryString2 += "_"+str(y)  +"="+Querystring[y]+"&"

    request_ = url+QueryString2+"&_answer="+Querystring
    response = requests.get(request_)
    print(response.text.split("\n")[-1] , x)
