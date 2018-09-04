import requests
resp = requests.get("https://www.booking.com/searchresults.html?label=gen173nr-1FCAEoggJCAlhYSDNYBGhsiAEBmAExwgEKd2luZG93cyAxMMgBDNgBAegBAfgBApICAXmoAgM;sid=81e77819479e4dfe7673c371265767b3;checkin_month=7&checkin_monthday=22&checkin_year=2018&checkout_month=7&checkout_monthday=23&checkout_year=2018&class_interval=1&dest_id=-2102840&dest_type=city&dtdisc=0&from_sf=1&group_adults=2&group_children=0&inac=0&index_postcard=0&label_click=undef&no_rooms=1&offset=0&postcard=0&room1=A%2CA&sb_price_type=total&search_pageview_id=70ec749c734300dd&src=index&src_elem=sb&ss=ludhiana&ss_all=0&ssb=empty&sshis=0&")
data = resp.text
soup
print(data)