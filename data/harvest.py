'''
2024.01.20
한국은행 통계시스템 ECOS 자료를 api를 사용하여
데이터를 다운로드하고 원하는 DataFrame 형태로 가공하기 위한 API 접근 라이브러리
'''

from .work import API_WORK
from .classes import api_request_param
from .form import SERVICE_DICT



def main(site=None, service=None, sub_service=None, *, savefile=None):
    site = site or input(f"오픈데이터 시스템을 선택하세요 : ")
    service = service or input(f"원하는 서비스를 입력하세요 : ")
    sub_service = sub_service or input(f"하위 서비스를 입력하세요 : ")
    savefile = savefile or input(f"데이터를 저장할 파일명을 입력하세요 : ")
    if not savefile.endswith(".xlsx"): savefile += ".xlsx"
    filepath = f'./storage/{savefile}'

    # # 현재는 임시로 요청 저장이 있지만 원래 계획은 main() 에는 GUI class를 로드해서 사용할 예정
    params = api_request_param()
    params.service = SERVICE_DICT.get(site).get(service).get("service_name")  
    site_res = API_WORK(site, params=params)
    df = site_res.api_service(service=service, sub_service=sub_service, trans_colname=False)
    try:
        df.to_excel(filepath)
        print(f"Save to {filepath}")
    except:
        print("Failed")



if __name__=="__main__":
    main()
