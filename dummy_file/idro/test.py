# import http.cookiejar
#
# from urllib import request
# from urllib import parse
#
# cj = http.cookiejar.LWPCookieJar()

import  requests

value = {'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
 'Accept-Encoding': 'gzip,deflate,br',
 'Accept-Language': 'ko,en;q=0.9,ko-KR;q=0.8,en-US;q=0.7',
 'Connection': 'keep-alive',
 'Cookie': '_ga=GA1.3.466441023.1581308344;moodle_notice_1_3730=hide;moodle_notice_1_4154=hide;moodle_notice_1_2123=hide;moodle_notice_1_5991=hide;moodle_notice_1_6983=hide;_gid=GA1.3.312584116.1587357221;user_iid=;user_name=%EA%B3%A0%EC%A7%80%EC%95%88;send_name=%EA%B3%A0%EC%A7%80%EC%95%88;group_name=%ED%95%99%EB%B6%80%EC%83%9D;p_lang=ko;uid_seq=*9BEE17FF11FD5905B0CCF0D55CCB114030311E05;autologout=Y;user_id=00011121138150165361913111111813431000;group_id=00006649000;nuri_id=bluetoon;nuri_date=20200422195212;nuri_passwd=d85a6c086022ceaf36525cfeb5dee4e6;JSESSIONID=spFCaUOhyUr6PHqN7Jd2YeFhW28pSTubJ3G8TLCEW1dbHFhX41tIL9SEOqXj1diM.cms1_servlet_engine2;PHPSESSID=mahd60jt6pceoherneme6q18hq;MoodleSession=r4c7qte6jcsn9cvfmedp670b60',
 'DNT': '1',
 'Host': 'lms.mokpo.ac.kr',
 'If-Modified-Since': 'Sun,12Apr202007:47:59GMT',
 'If-None-Match': '"629349e3d95c5d81406bddeed33510cb5813d39e-gzip"',
 'Sec-Fetch-Dest': 'document',
 'Sec-Fetch-Mode': 'navigate',
 'Sec-Fetch-Site': 'same-origin',
 'Sec-Fetch-User': '?1',
 'Upgrade-Insecure-Requests': '1',
 'User-Agent': 'Mozilla/5.0(WindowsNT10.0;Win64;x64)AppleWebKit/537.36(KHTML,likeGecko)Chrome/81.0.4044.113Safari/537.36'
         }

for x in range(13500,12500):
    url = "https://lms.mokpo.ac.kr/pluginfile.php/"+str(x)+"/mod_ubfile/content/0/0.%eb%84%a4%ed%8a%b8%ec%9b%8c%ed%81%ac%20%ea%b8%b0%ec%b4%88.pdf?forcedownload=1"
    print(url)
    with open("test_file"+str(x)+".pdf", "wb") as file:  # open in binary mode
        response = requests.get(url, headers=value)  # get request
        if int(len(response.content)) > 37063:

            file.write(response.content)  # write to file
        else:
            pass
