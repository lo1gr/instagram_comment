# https://curl.trillworks.com/
import requests
from login_insta import authenticate_with_login
from user_password import user_password
import json

import requests


headers = {
    'x-ig-www-claim': 'hmac.AR3cVaOKHUd5kYx1a_TOynNnklt-KY52aedVIJSgziTsznFz',
    'x-ig-app-id': '936619743392459',
    'referer': 'https://www.instagram.com/p/CFeTbuHnNiNaoIsTqcyVRZps1EhbBfY3YBU-bc0/',
    'cookie': 'ig_did=8B477954-0710-4119-9B31-CF5DA0794597; mid=YFXYgQAEAAE6TkiAXbP0KgJzc1nd; fbm_124024574287414=base_domain=.instagram.com; shbid=3971; shbts=1621715041.486275; rur=NAO; fbsr_124024574287414=rwe2ul8o4B9koBB1kNqTCg0X6T20l4RjH_RrA_-XFeM.eyJ1c2VyX2lkIjoiMTAwMDAyNzE5MzUwMDgyIiwiY29kZSI6IkFRQTE5QkY2cW5jbzZ2dWRTX0RqQWJKc2hsZXFyS0pEMm9xS1htbEVfeGdaRFQ4c2wtR1FEZnluWWxraFNOWlZsR0RXMi1vdDlfbXQzZHFQZ01sdkhfaXEwTHVOeGFvTjVDLWJQVkYwRk9MZVQ1NGNMVGVCQmdZLV8zTU9yWUMwbFNFbnFaaG5nQ3BCanNpbUwxT3ljYjV2N2Y5RlQyVDNscVl0czVwSWxXUVhYNUVjZldHRTFVbE9xZmJKZW55TGxLS1J2MENPTnQtRExFQ1NQczNQSlozWF9aVF9hYlM1Uk4wY3ExeVNGSHIzbTRKb2FkS0NqSWhhSVA4RFdPQThvUUJJU21WMHFReTZsbmp5MXlWdERWcWJ3b1A2ZVlZUE5UYUlJSTE1WXJiX2RMTF9saU96eFNaR1JRWHNEWmp2U3NmUl9qdEZMT1NoS3VXRjBndWtoX0ZBIiwib2F1dGhfdG9rZW4iOiJFQUFCd3pMaXhuallCQUxTQjFEZ3h5R3RaQ1NvYnZCeFIwM3IwSDJtaHhyZExGMklLanRpM0kxOXhINkU1bTZXYThBZDAxbDNraVdHN3IzVzVSRXVjT1pDc2JRazB3emVhdmFnQjVaQmV3UEdnc2RYUURVWkJubmlpOU8wU1g3WkExRzZRRnJqcDRiVnJxMDlkQUhtWVFaQVBMZGcydFBkZDc2dWtpOEl0cjB4aURVbUNyUXVzckYiLCJhbGdvcml0aG0iOiJITUFDLVNIQTI1NiIsImlzc3VlZF9hdCI6MTYyMTg4MDQ5MH0; fbsr_124024574287414=rwe2ul8o4B9koBB1kNqTCg0X6T20l4RjH_RrA_-XFeM.eyJ1c2VyX2lkIjoiMTAwMDAyNzE5MzUwMDgyIiwiY29kZSI6IkFRQTE5QkY2cW5jbzZ2dWRTX0RqQWJKc2hsZXFyS0pEMm9xS1htbEVfeGdaRFQ4c2wtR1FEZnluWWxraFNOWlZsR0RXMi1vdDlfbXQzZHFQZ01sdkhfaXEwTHVOeGFvTjVDLWJQVkYwRk9MZVQ1NGNMVGVCQmdZLV8zTU9yWUMwbFNFbnFaaG5nQ3BCanNpbUwxT3ljYjV2N2Y5RlQyVDNscVl0czVwSWxXUVhYNUVjZldHRTFVbE9xZmJKZW55TGxLS1J2MENPTnQtRExFQ1NQczNQSlozWF9aVF9hYlM1Uk4wY3ExeVNGSHIzbTRKb2FkS0NqSWhhSVA4RFdPQThvUUJJU21WMHFReTZsbmp5MXlWdERWcWJ3b1A2ZVlZUE5UYUlJSTE1WXJiX2RMTF9saU96eFNaR1JRWHNEWmp2U3NmUl9qdEZMT1NoS3VXRjBndWtoX0ZBIiwib2F1dGhfdG9rZW4iOiJFQUFCd3pMaXhuallCQUxTQjFEZ3h5R3RaQ1NvYnZCeFIwM3IwSDJtaHhyZExGMklLanRpM0kxOXhINkU1bTZXYThBZDAxbDNraVdHN3IzVzVSRXVjT1pDc2JRazB3emVhdmFnQjVaQmV3UEdnc2RYUURVWkJubmlpOU8wU1g3WkExRzZRRnJqcDRiVnJxMDlkQUhtWVFaQVBMZGcydFBkZDc2dWtpOEl0cjB4aURVbUNyUXVzckYiLCJhbGdvcml0aG0iOiJITUFDLVNIQTI1NiIsImlzc3VlZF9hdCI6MTYyMTg4MDQ5MH0; ds_user_id=1464713842; sessionid=1464713842%3AmpfPRDGEgblzMk%3A22; csrftoken=HoHLcsWlkyL2zFcgZXrufGlngxRwC0VS',
}

data = {
  '$comment_text': 'Statement\\u0021',
  'replied_to_comment_id': ''
}

response = requests.post('https://www.instagram.com/web/comments/2404444718891849869/add/', headers=headers, data=data)



user_agent = "Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.212 Mobile Safari/537.36"
headers = {
    'authority': 'www.instagram.com',
    'sec-ch-ua': '" Not A;Brand";v="99", "Chromium";v="90", "Google Chrome";v="90"',
    'x-ig-www-claim': 'hmac.AR3cVaOKHUd5kYx1a_TOynNnklt-KY52aedVIJSgziTszjR7',
    'sec-ch-ua-mobile': '?1',
    'x-instagram-ajax': 'eb23e8952baa',
    'content-type': 'application/x-www-form-urlencoded',
    'accept': '*/*',
    'x-requested-with': 'XMLHttpRequest',
    'user-agent': 'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.212 Mobile Safari/537.36',
    # 'x-csrftoken': 'XgWFewMLGdoXNtSq1gOIc92oSQ3VNvL0',
    'x-ig-app-id': '936619743392459',
    'origin': 'https://www.instagram.com',
    'sec-fetch-site': 'same-origin',
    'sec-fetch-mode': 'cors',
    'sec-fetch-dest': 'empty',
    # 'referer': 'https://www.instagram.com/p/CPKKWkJAS6_/',
    'accept-language': 'en-US,en;q=0.9,es;q=0.8,fr;q=0.7',
    # 'cookie': 'ig_did=8B477954-0710-4119-9B31-CF5DA0794597; mid=YFXYgQAEAAE6TkiAXbP0KgJzc1nd; fbm_124024574287414=base_domain=.instagram.com; ds_user_id=43153248460; csrftoken=XgWFewMLGdoXNtSq1gOIc92oSQ3VNvL0; sessionid=43153248460%3AfGDPiMZCMDbMH3%3A7; shbid=3971; shbts=1621715041.486275; rur=NAO; fbsr_124024574287414=g-8GFzniLNup16Od-WyObijEIZZVyFAdcimzFi_KcmU.eyJ1c2VyX2lkIjoiMTAwMDAyNzE5MzUwMDgyIiwiY29kZSI6IkFRQm9QamZGMm1rNzV0bURZVTlzV09tZ2R3NkhxS09fWTNiTlVTOC00UGs0ZkJFUjFWUjNBd2p0RndaTUs2cW9qbUN2bWhSNTM0QUJnSDdNMlVJR0t1elVJMEV3amVSSmI4eGZRb19JVG0yeUhPYk0ydnphVnp3QlhrVTlCOTZSaVF5X0J5RWlnbXZnd2s2OG1IMks0endRRVdRTWtlMWJUTVpULVZ0QU1HcGFBLVQ3STcwZGRDRVhyY1R2SkxKa1NPeWFtdG1WNk1fWnR4VEd1aGNfbGhtMmx4V3lXRGhvMWd0Qm5GcFZmRVZSX3JZWkdHRHBjMlV5ZXBDM3k5S19GSmgwQlMydWxfTlFxc0RENVhOOEJpSjNUTWYyOVY5d2pzZTR5OXlaWHoxMFVlelVwZkdmdHZaOXQyQ2VGMWljOGpvOEstOFJIOHhiTloyQllNeDRwTkU1Iiwib2F1dGhfdG9rZW4iOiJFQUFCd3pMaXhuallCQUNnUTh4TnpTaEduejVDcTZaQTNIdzFVNWJjMmwxY0JmdllKeFB6YWtTQlk4eWV2eHplaXdjUjdqc3BxRXhjTGdIRFQ0ODc5UkI4akdaQzBGQ1hRaWRtQWhibndvMFZQMnp0a2VaQmM4Q1cxY29aQndPa25NZk9ZQmoyUUNVdEV6OEVnYVdjM0Y1TjFvN01PMnI3SmVwTWJMQlRZd1lieE1KcDlaQURPciIsImFsZ29yaXRobSI6IkhNQUMtU0hBMjU2IiwiaXNzdWVkX2F0IjoxNjIxNzE2MTM2fQ',
}

data = {
  '$comment_text': 'Repetition is key',
  'replied_to_comment_id': ''
}

def main():
    key = list(user_password)[2]
    value = user_password[key]
    session = requests.session()
    session, cookies = authenticate_with_login(key,value, user_agent)
    headers['x-csrftoken'] = cookies['csrftoken']
    headers['cookie'] = 'ds_user_id=43153248460; csrftoken=' + cookies['csrftoken'] + ';'
    headers['referer'] = 'https://www.instagram.com/p/CPBEs-4gKfD/'    #not needed?

    # 'cookie': 'ig_did=; mid= fbm_124024574287414=base_domain=.instagram.com; ds_user_id=; csrftoken=; sessionid=; shbid=; shbts=; rur=; fbsr_124024574287414=',

    # problem is - does not detect the user

    cookies = {
    # "sessionid": cookies['sessionid'],
    "csrftoken": cookies['csrftoken']
    }

    result = session.post('https://www.instagram.com/web/comments/2576361145195603907/add/', headers=headers, data=data, cookies=cookies)
    print(result.status_code)
    print(result.history)
    for resp in result.history:
        print(result.status_code, result.url)
    # print(result.text[:500])


if __name__ == '__main__':
    main()
