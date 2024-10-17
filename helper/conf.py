import configparser
from pathlib import Path

properties = configparser.ConfigParser()  ## 클래스 객체 생성




# 절대경로
# properties.read(r'C:\workspace\lgtm\config.ini', encoding='utf-8')  ## 파일 읽기
# 상대경로
properties.read(r'..\config.ini', encoding='utf-8')  ## 파일 읽기
# pathlib 
현위치 = Path().cwd()
print(현위치)
print(type(현위치))
ini위치 = 현위치.joinpath("config.ini")
print(ini위치)
print(type(ini위치))

properties.read(ini위치, encoding='utf-8')  ## 파일 읽기


이미지 = properties["이미지"] ## 섹션 선택
폰트 = properties["폰트"] ## 섹션 선택
사용자정보 = properties["사용자정보"] ## 섹션 선택


if __name__=="__main__" :
    print( 이미지["가로"] ) ## key-value 조회
    print( 폰트["FONT_NAME"] ) ## key-value 조회
    print( 사용자정보["운영체제"] ) ## key-value 조회

# print( int(test["test"]) )
# print( test.getint("test") )

# configparser 사용 - Set 

# properties.set("DEFAULT", "addkey", "configset")

# default = properties["DEFAULT"] 
# default.setdefault("abc", "a")

# print( default["addkey"] )
# print( default["abc"] )
 

 

# with open(filepath, "w") as f:
#     properties.write(f)


