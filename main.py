import requestsuu
import json

#      ПЕРВЫЕ COOKIES, PARAMS, HEADERS НУЖНО ОБНОВИТЬ ЕСЛИ ПРИ ЗАПУСКЕ КОДА ВЫШЛА ОШИБКА В СТРОКЕ С RESPONSE. 



def get_data():

    

    cookies = {
        '__lhash_': '2809cde1a9372c0806e26a054bfb585e',
        'MVID_CASCADE_CMN': 'true',
        'MVID_CHAT_VERSION': '4.16.4',
        'MVID_CITY_ID': 'CityCZ_975',
        'MVID_CREDIT_DIGITAL': 'true',
        'MVID_CREDIT_SERVICES': 'true',
        'MVID_CRITICAL_GTM_INIT_DELAY': '3000',
        'MVID_EMPLOYEE_DISCOUNT': 'true',
        'MVID_FILTER_CODES': 'true',
        'MVID_FILTER_TOOLTIP': '1',
        'MVID_FLOCKTORY_ON': 'true',
        'MVID_GEOLOCATION_NEEDED': 'true',
        'MVID_GTM_ENABLED': '011',
        'MVID_INTERVAL_DELIVERY': 'true',
        'MVID_IS_NEW_BR_WIDGET': 'true',
        'MVID_KLADR_ID': '7700000000000',
        'MVID_LAYOUT_TYPE': '1',
        'MVID_MINDBOX_DYNAMICALLY': 'true',
        'MVID_NEW_LK_CHECK_CAPTCHA': 'true',
        'MVID_NEW_LK_OTP_TIMER': 'true',
        'MVID_NEW_MBONUS_BLOCK': 'true',
        'MVID_REGION_ID': '1',
        'MVID_REGION_SHOP': 'S002',
        'MVID_SERVICES': '111',
        'MVID_SINGLE_CHECKOUT': 'true',
        'MVID_SP': 'true',
        'MVID_TIMEZONE_OFFSET': '3',
        'MVID_TYP_CHAT': 'true',
        'MVID_WEB_SBP': 'true',
        'SENTRY_ERRORS_RATE': '0.1',
        'SENTRY_TRANSACTIONS_RATE': '0.5',
        'partnerSrc': 'google',
        '__SourceTracker': 'google__organic',
        'admitad_deduplication_cookie': 'google__organic',
        '__cpatrack': 'google_organic',
        '__sourceid': 'google',
        '__allsource': 'google',
        '_ym_uid': '1697453028876369940',
        '_ym_d': '1697453028',
        'tmr_lvid': '3e8d8c198e14a866bf3bc829308e51f1',
        'tmr_lvidTS': '1697453047433',
        'flocktory-uuid': '632d8a88-b6b1-4670-a231-6239d694303f-4',
        'advcake_session_id': '7ded6104-7a95-6806-89ca-0300e1421674',
        'uxs_uid': 'f0264320-6c10-11ee-b3c4-2555340752e1',
        'afUserId': 'ab350082-5f9b-4ecb-b4ce-e86a17b06cf4-p',
        'AF_SYNC': '1697453051103',
        '_gpVisits': '{"isFirstVisitDomain":true,"idContainer":"100025D5"}',
        'advcake_track_url': 'https%3A%2F%2Fwww.mvideo.ru%2F%3Futm_source%3Dgoogle%26utm_medium%3Dorganic%26utm_campaign%3Dgoogle%26utm_referrer%3Dgoogle',
        'advcake_utm_partner': 'google',
        'advcake_utm_webmaster': '',
        'advcake_click_id': '',
        '_ga_HCF1KSW48B': 'GS1.2.1697535386.3.1.1697538241.39.0.0',
        '_ga_TY7GLH5RV3': 'GS1.2.1697535386.3.1.1697538244.36.0.0',
        '_ga': 'GA1.1.1408319527.1697453024',
        'MVID_ALFA_PODELI_NEW': 'true',
        'MVID_PODELI_PDP': 'true',
        'MVID_ENVCLOUD': 'prod2',
        'SMSError': '',
        'authError': '',
        'advcake_track_id': 'd47ef048-2e83-995e-b179-6d80c1de88c6',
        '_ym_isad': '1',
        '__js_p_': '945,1800,0,1,0',
        '__jhash_': '941',
        '__jua_': 'Mozilla%2F5.0%20%28Windows%20NT%2010.0%3B%20Win64%3B%20x64%29%20AppleWebKit%2F537.36%20%28KHTML%2C%20like%20Gecko%29%20Chrome%2F118.0.0.0%20Safari%2F537.36',
        '__hash_': 'c6afa320ed7b6970376f8cde3e7c76be',
        '_sp_ses.d61c': '*',
        '_sp_id.d61c': 'df90d611-794f-4dc7-b65a-2ce5d784b4f7.1697453028.12.1697801965.1697789804.485e0a32-d524-4f90-8ee5-132940a43ab4.656a91ce-0096-4816-84ae-e2200f14cb13.dd87d9ed-9999-47c5-9a9a-7b8142a0bdde.1697801963754.5',
        'tmr_detect': '1%7C1697801966160',
        'mindboxDeviceUUID': 'cf7e9605-055b-4844-85d3-92ec3929434b',
        'directCrm-session': '%7B%22deviceGuid%22%3A%22cf7e9605-055b-4844-85d3-92ec3929434b%22%7D',
        '_ym_visorc': 'w',
        '_gp100025D5': '{"utm":"-2e849f2c","hits":7,"vc":1,"ac":1,"a6":1}',
        'gsscgib-w-mvideo': '49LOLxCeRa4mZirdAwNr+6jbBJ2TnQMz96IrH4Js4/CmrQfAZLw7UY00B0lNViZ82qB8+3aZ/BzQS20yrGhvEwjbw8ejfQhSdjJAiHFKjgrg6G0qu0iRN4PMeINsXB9xuzI6Yzcdwb1C4t7oUNfS9rcDZb6fbuNM04OuKtBPDU/Fz0TCk8IYEfDjqPi5H/S47ZvM9CIQtG6SzXzWo54r7sL9nazEvqxLUJ+L0rgXdXahYyAOCDba8BHzli8uTgIu/H9YwM5fkSlJyQ==',
        'gsscgib-w-mvideo': '49LOLxCeRa4mZirdAwNr+6jbBJ2TnQMz96IrH4Js4/CmrQfAZLw7UY00B0lNViZ82qB8+3aZ/BzQS20yrGhvEwjbw8ejfQhSdjJAiHFKjgrg6G0qu0iRN4PMeINsXB9xuzI6Yzcdwb1C4t7oUNfS9rcDZb6fbuNM04OuKtBPDU/Fz0TCk8IYEfDjqPi5H/S47ZvM9CIQtG6SzXzWo54r7sL9nazEvqxLUJ+L0rgXdXahYyAOCDba8BHzli8uTgIu/H9YwM5fkSlJyQ==',
        'fgsscgib-w-mvideo': 'BxhC135794e081df1e3cf2881afd30c8afd8f1ed',
        'fgsscgib-w-mvideo': 'BxhC135794e081df1e3cf2881afd30c8afd8f1ed',
        'gssc218': '',
        'cfidsgib-w-mvideo': 'Q473uMDWA+kvpXXDlVqcMXA4D5SaJUBVmZNWxjmkJqqEvbNNrVnkHFO7i+RiVJHqsd1JhSIVd9Llefctg69K/WiJ4j1QM6h0TB/CvUqVF+AUR83jiQdzTgr+HKWXsJ9zvj/niR6YvvVdoRIqOjUGqSavWhwL+hGFNb5KdpA=',
        '_ga_BNX5WPP3YK': 'GS1.1.1697801345.11.1.1697802040.60.0.0',
        '_ga_CFMZTSS5FM': 'GS1.1.1697801345.11.1.1697802040.0.0.0',
    }

    headers = {
        'authority': 'www.mvideo.ru',
        'accept': 'application/json',
        'accept-language': 'ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7',
        'baggage': 'sentry-environment=production,sentry-public_key=1e9efdeb57cf4127af3f903ec9db1466,sentry-trace_id=1e2df9ae9ff94115b3016748db117861,sentry-sample_rate=0.5,sentry-transaction=%2F,sentry-sampled=false',
        # 'cookie': '__lhash_=2809cde1a9372c0806e26a054bfb585e; MVID_CASCADE_CMN=true; MVID_CHAT_VERSION=4.16.4; MVID_CITY_ID=CityCZ_975; MVID_CREDIT_DIGITAL=true; MVID_CREDIT_SERVICES=true; MVID_CRITICAL_GTM_INIT_DELAY=3000; MVID_EMPLOYEE_DISCOUNT=true; MVID_FILTER_CODES=true; MVID_FILTER_TOOLTIP=1; MVID_FLOCKTORY_ON=true; MVID_GEOLOCATION_NEEDED=true; MVID_GTM_ENABLED=011; MVID_INTERVAL_DELIVERY=true; MVID_IS_NEW_BR_WIDGET=true; MVID_KLADR_ID=7700000000000; MVID_LAYOUT_TYPE=1; MVID_MINDBOX_DYNAMICALLY=true; MVID_NEW_LK_CHECK_CAPTCHA=true; MVID_NEW_LK_OTP_TIMER=true; MVID_NEW_MBONUS_BLOCK=true; MVID_REGION_ID=1; MVID_REGION_SHOP=S002; MVID_SERVICES=111; MVID_SINGLE_CHECKOUT=true; MVID_SP=true; MVID_TIMEZONE_OFFSET=3; MVID_TYP_CHAT=true; MVID_WEB_SBP=true; SENTRY_ERRORS_RATE=0.1; SENTRY_TRANSACTIONS_RATE=0.5; partnerSrc=google; __SourceTracker=google__organic; admitad_deduplication_cookie=google__organic; __cpatrack=google_organic; __sourceid=google; __allsource=google; _ym_uid=1697453028876369940; _ym_d=1697453028; tmr_lvid=3e8d8c198e14a866bf3bc829308e51f1; tmr_lvidTS=1697453047433; flocktory-uuid=632d8a88-b6b1-4670-a231-6239d694303f-4; advcake_session_id=7ded6104-7a95-6806-89ca-0300e1421674; uxs_uid=f0264320-6c10-11ee-b3c4-2555340752e1; afUserId=ab350082-5f9b-4ecb-b4ce-e86a17b06cf4-p; AF_SYNC=1697453051103; _gpVisits={"isFirstVisitDomain":true,"idContainer":"100025D5"}; advcake_track_url=https%3A%2F%2Fwww.mvideo.ru%2F%3Futm_source%3Dgoogle%26utm_medium%3Dorganic%26utm_campaign%3Dgoogle%26utm_referrer%3Dgoogle; advcake_utm_partner=google; advcake_utm_webmaster=; advcake_click_id=; _ga_HCF1KSW48B=GS1.2.1697535386.3.1.1697538241.39.0.0; _ga_TY7GLH5RV3=GS1.2.1697535386.3.1.1697538244.36.0.0; _ga=GA1.1.1408319527.1697453024; MVID_ALFA_PODELI_NEW=true; MVID_PODELI_PDP=true; MVID_ENVCLOUD=prod2; SMSError=; authError=; advcake_track_id=d47ef048-2e83-995e-b179-6d80c1de88c6; _ym_isad=1; __js_p_=945,1800,0,1,0; __jhash_=941; __jua_=Mozilla%2F5.0%20%28Windows%20NT%2010.0%3B%20Win64%3B%20x64%29%20AppleWebKit%2F537.36%20%28KHTML%2C%20like%20Gecko%29%20Chrome%2F118.0.0.0%20Safari%2F537.36; __hash_=c6afa320ed7b6970376f8cde3e7c76be; _sp_ses.d61c=*; _sp_id.d61c=df90d611-794f-4dc7-b65a-2ce5d784b4f7.1697453028.12.1697801965.1697789804.485e0a32-d524-4f90-8ee5-132940a43ab4.656a91ce-0096-4816-84ae-e2200f14cb13.dd87d9ed-9999-47c5-9a9a-7b8142a0bdde.1697801963754.5; tmr_detect=1%7C1697801966160; mindboxDeviceUUID=cf7e9605-055b-4844-85d3-92ec3929434b; directCrm-session=%7B%22deviceGuid%22%3A%22cf7e9605-055b-4844-85d3-92ec3929434b%22%7D; _ym_visorc=w; _gp100025D5={"utm":"-2e849f2c","hits":7,"vc":1,"ac":1,"a6":1}; gsscgib-w-mvideo=49LOLxCeRa4mZirdAwNr+6jbBJ2TnQMz96IrH4Js4/CmrQfAZLw7UY00B0lNViZ82qB8+3aZ/BzQS20yrGhvEwjbw8ejfQhSdjJAiHFKjgrg6G0qu0iRN4PMeINsXB9xuzI6Yzcdwb1C4t7oUNfS9rcDZb6fbuNM04OuKtBPDU/Fz0TCk8IYEfDjqPi5H/S47ZvM9CIQtG6SzXzWo54r7sL9nazEvqxLUJ+L0rgXdXahYyAOCDba8BHzli8uTgIu/H9YwM5fkSlJyQ==; gsscgib-w-mvideo=49LOLxCeRa4mZirdAwNr+6jbBJ2TnQMz96IrH4Js4/CmrQfAZLw7UY00B0lNViZ82qB8+3aZ/BzQS20yrGhvEwjbw8ejfQhSdjJAiHFKjgrg6G0qu0iRN4PMeINsXB9xuzI6Yzcdwb1C4t7oUNfS9rcDZb6fbuNM04OuKtBPDU/Fz0TCk8IYEfDjqPi5H/S47ZvM9CIQtG6SzXzWo54r7sL9nazEvqxLUJ+L0rgXdXahYyAOCDba8BHzli8uTgIu/H9YwM5fkSlJyQ==; fgsscgib-w-mvideo=BxhC135794e081df1e3cf2881afd30c8afd8f1ed; fgsscgib-w-mvideo=BxhC135794e081df1e3cf2881afd30c8afd8f1ed; gssc218=; cfidsgib-w-mvideo=Q473uMDWA+kvpXXDlVqcMXA4D5SaJUBVmZNWxjmkJqqEvbNNrVnkHFO7i+RiVJHqsd1JhSIVd9Llefctg69K/WiJ4j1QM6h0TB/CvUqVF+AUR83jiQdzTgr+HKWXsJ9zvj/niR6YvvVdoRIqOjUGqSavWhwL+hGFNb5KdpA=; _ga_BNX5WPP3YK=GS1.1.1697801345.11.1.1697802040.60.0.0; _ga_CFMZTSS5FM=GS1.1.1697801345.11.1.1697802040.0.0.0',
        'referer': 'https://www.mvideo.ru/product-list-page/f/skidka=da/tolko-v-nalichii=da?q=%D0%BF%D0%BB%D0%B0%D0%BD%D1%88%D0%B5%D1%82&category=planshety-195',
        'sec-ch-ua': '"Chromium";v="118", "Google Chrome";v="118", "Not=A?Brand";v="99"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
        'sec-fetch-dest': 'empty',
        'sec-fetch-mode': 'cors',
        'sec-fetch-site': 'same-origin',
        'sentry-trace': '1e2df9ae9ff94115b3016748db117861-bf7daa6491c17a18-0',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/118.0.0.0 Safari/537.36',
        'x-kl-ajax-request': 'Ajax_Request',
        'x-set-application-id': '32ee18fe-4a69-45bf-8b61-a1aabb7f5567',
    }

    params = {
        'query': 'планшет',
        'categoryId': '195',
        'offset': '0',
        'limit': '24',
        'filterParams': [
            'WyJza2lka2EiLCIiLCJkYSJd',
            'WyJ0b2xrby12LW5hbGljaGlpIiwiIiwiZGEiXQ==',
        ],
        'doTranslit': 'true',
        'context': 'eyJxdWVyeSI6ItC_0LvQsNC90YjQtdGCIiwic2hvcElkcyI6WyJTMDAyIl0sInN0cmF0ZWd5SWQiOiJzdGVwMSIsImhpZGRlbkZpcnN0R3JvdXAiOltdLCJmaXJzdEdyb3VwIjpbIjE5NSJdLCJmaXJzdEdyb3VwU3RhZ2UiOiJESUNUIiwicmVzcG9uc2VUeXBlIjoicGxhaW4iLCJiaVN0YXRzIjp7IjE5NSI6MTAwMCwiMTE4IjoxNywiMjA1IjoxNSwiMjgwIjoxNSwiMjAyIjo1LCI2NSI6NCwiMjg3Ijo0LCIzMDA3IjozLCI0MDMiOjIsIjI0MzgiOjJ9fQ==',
    }

    response = requests.get('https://www.mvideo.ru/bff/products/search', params=params, cookies=cookies, headers=headers).json()
    
    product_ids = response.get('body').get('products')

    with open('1_products_ids.json', 'w', encoding='utf-8') as file:
        json.dump(product_ids, file, indent=4, ensure_ascii=False)
    # print(product_ids)

    json_data = {
        'productIds': product_ids,
        'mediaTypes': [
            'images',
        ],
        'category': True,
        'status': True,
        'brand': True,
        'propertyTypes': [
            'KEY',
        ],
        'propertiesConfig': {
            'propertiesPortionSize': 5,
        },
        'multioffer': False,
    }

    response = requests.post('https://www.mvideo.ru/bff/product-details/list', cookies=cookies, headers=headers, json=json_data).json()

    with open('2_products_items.json', 'w', encoding='utf-8') as items_file:
        json.dump(response, items_file, indent=4, ensure_ascii=False)

    
    product_ids_str = ','.join(product_ids)

    params = {
    'productIds': product_ids_str,
    'addBonusRubles': 'true',
    'isPromoApplied': 'true',
    }

    response = requests.get('https://www.mvideo.ru/bff/products/prices', params=params, cookies=cookies, headers=headers).json()

    with open('3_prices.json', 'w', encoding='utf-8') as price_file:
        json.dump(response, price_file, indent=4, ensure_ascii=False)

    
    item_prices = {}

    material_prices = response.get('body').get('materialPrices')

    for item in material_prices:
        item_id = item.get('productId')
        item_base_price = item.get('price').get('basePrice')
        item_sale_price = item.get('price').get('salePrice')
        item_bonus = item.get('bonusRubles').get('total')

        item_prices[item_id] = {
            'item_basePrice': item_base_price,
            'item_salePrice': item_sale_price,
            'item_bonus': item_bonus
        }

    with open('4_prices.json', 'w', encoding='utf-8') as file_4:
        json.dump(item_prices, file_4, indent=4, ensure_ascii=False)

def get_result():

    with open('2_products_items.json', encoding='utf-8') as file:
        products_data = json.load(file)

    with open('4_prices.json', encoding='utf-8') as file:
        products_prices = json.load(file)

    products_data = products_data.get('body').get('products')

    for item in products_data:
        product_id = item.get('productId')

        if product_id in products_prices:
            prices = products_prices[product_id]

            item['item_basePrice'] = prices.get('item_basePrice')
            item['item_salePrice'] = prices.get('item_salePrice')
            item['item_bonus'] = prices.get('item_bonus')

    with open('final.json', 'w', encoding='utf-8') as file:
        json.dump(products_data, file, indent=4, ensure_ascii=False)

    





def main():
    get_data()
    get_result()


if __name__ == '__main__':
    main()
    





