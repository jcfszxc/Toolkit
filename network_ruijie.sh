line="0"
total="0"
dst="210.34.136.4"
 
function ruijie(){
	name=""
	password=""
	loginPageURL=`curl -s "http://www.google.cn/generate_204" | awk -F \' '{print $2}'`
	campus="%25E6%2595%2599%25E8%2582%25B2%25E7%25BD%2591%25E6%258E%25A5%25E5%2585%25A5"
	chinamobile="%25E7%25A7%25BB%25E5%258A%25A8%25E5%25AE%25BD%25E5%25B8%25A6%25E6%258E%25A5%25E5%2585%25A5"
	chinanet="%25E7%2594%25B5%25E4%25BF%25A1%25E5%25AE%25BD%25E5%25B8%25A6%25E6%258E%25A5%25E5%2585%25A5"
	chinaunicom="%25E8%2581%2594%25E9%2580%259A%25E5%25AE%25BD%25E5%25B8%25A6%25E6%258E%25A5%25E5%2585%25A5"
	loginURL=`echo $loginPageURL | awk -F \? '{print $1}'`
	loginURL="${loginURL/index.jsp/InterFace.do?method=login}"
	queryString=`echo $loginPageURL | awk -F \? '{print $2}'`
	queryString="${queryString//&/%2526}"
	queryString="${queryString//=/%253D}"
	authResult=`curl -s -A "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/61.0.3163.91 Safari/537.36" -e "$loginPageURL" -b "EPORTAL_COOKIE_USERNAME=; EPORTAL_COOKIE_PASSWORD=; EPORTAL_COOKIE_SERVER=; EPORTAL_COOKIE_SERVER_NAME=; EPORTAL_AUTO_LAND=; EPORTAL_USER_GROUP=%E5%AD%A6%E7%94%9F%E5%8C%85%E6%9C%88; EPORTAL_COOKIE_OPERATORPWD=;" -d "userId=$name&password=$password&service=$campus&queryString=$queryString&operatorPwd=&operatorUserId=&validcode=&passwordEncrypt=false" -H "Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8" -H "Content-Type: application/x-www-form-urlencoded; charset=UTF-8" "$loginURL"`
	echo $authResult
}


while [ 1 ]; do
	line=`ping $dst -c 1 -s 1 -W 1 | grep "100% packet loss" | wc -l`
	if [ "${line}" != "0" ]; then
		total=$((total+1))
		echo "The network is disconnected!"
		echo -e "Attempt to connect the campus network!"
		ruijie
		sleep 10
	else
		echo "The network is connected!"
	fi
	sleep 5
done
