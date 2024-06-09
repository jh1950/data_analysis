'''
2024.01.20
한국은행 통계시스템 ECOS 자료를 api를 사용하여
데이터를 다운로드하고 원하는 DataFrame 형태로 가공하기 위한 API 접근 라이브러리
'''
import pandas as pd

from .work import API_WORK
from .classes import api_request_param
from .pipline import Pipeline
from .form import SERVICE_DICT



class Harvest:
    # data_provider의 pipline 클라스를 통해서 필요한 factor를 가져옴.
    def __init__(self, site, service, sub_service) -> None:
        self.__set_host = site
        self.__service = service
        self.__sub_service = sub_service
        self.__pipe = Pipeline()
        self.__factors = self.__pipe.load_select_factor(self.__service)
        self.__params = api_request_param()
        self.__result = self.do_it()

    def do_it(self):
        df = pd.DataFrame()
        site_res = API_WORK(self.__set_host, params=self.__params)

        for i in self.__factors.index:
            data = self.__factors.loc[i]
            var = data["Variable"]
            self.__params.stats_code = str(data["stats_code"])
            self.__params.Cycle = str(data["Cycle"])
            self.__params.Start_date = str(data["Start_date"])
            self.__params.End_date = str(data["End_date"])
            self.__params.Item_code_1 = str(data["Item_code_1"])
            self.__params.Item_code_2 = str(data["Item_code_2"])

            print(f"num fac: {int(i)+1}")
            print(f"Variable: {var}, stats_code: {self.__params.stats_code}")
            print(f"Variable: {var}, Cycle: {self.__params.Cycle}")
            print(f"Variable: {var}, Start_date: {self.__params.Start_date}")
            print(f"Variable: {var}, End_date: {self.__params.End_date}")

            site_res.set_params(self.__params)
            res = site_res.api_service(service=self.__service, sub_service=self.__sub_service, trans_colname=False)
            if isinstance(res, pd.DataFrame):
                try:
                    df = pd.concat([df, res[['TIME', 'DATA_VALUE']]], axis=1)
                except:
                    print("TIME, DATA_VALUE 값이 존재하지 않는 자료임")
                    return
            else:
                print(res)
        return dfs

    def save(self, save_path):
        self.__pipe.data_save(save_path, self.__result)



def main(site=None, service=None, sub_service=None, *, savefile=None):
    site = site or input(f"오픈데이터 시스템을 선택하세요 : ")
    service = service or input(f"원하는 서비스를 입력하세요 : ")
    sub_service = sub_service or input(f"하위 서비스를 입력하세요 : ")
    savefile = savefile or input(f"데이터를 저장할 파일명을 입력하세요 : ")
    if not savefile.endswith(".xlsx"): savefile += ".xlsx"
    filepath = f'./storage/excel/{savefile}'

    # 현재는 임시로 요청 저장이 있지만 원래 계획은 main() 에는 GUI class를 로드해서 사용할 예정
    params = api_request_param()
    params.service = SERVICE_DICT.get(site).get(service).get("service_name")  
    site_res = API_WORK(site, params=params)
    df = site_res.api_service(service=service, sub_service=sub_service, trans_colname=False)
    try:
        df.to_excel(filepath)
        print(f"Save to {filepath}")
    except:
        print("Failed")

    # harvest = Harvest(site, service, sub_service)
    # harvest.save(filepath)



if __name__=="__main__":
    main()
