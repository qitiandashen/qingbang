import requests
from urllib.parse import urlencode
def get_index_page(page,keyword):
    data={
        "page": page,
        "per_page": "40",
        "keyword": keyword,
        "entity_type":"post",
        "sort": "date",
        "_": "1552967347865"
    }
    headers={"User-Agent":"Mozilla/5.0(WindowsNT6.3;Win64;x64)AppleWebKit/537.36(KHTML,likeGecko)Chrome/68.0.3440.106Safari/537.36"
        }

    try:
        url='https://36kr.com/api//search/entity-search?'+urlencode(data)
        response=requests.get(url,headers=headers)
        if response.status_code==200:
            return response.text
        return None
    except Exception as e:
        print(e)
        return None
def main():
    html=get_index_page(1,'工商财税')
    print(html)
if __name__=='__main__':
    main()