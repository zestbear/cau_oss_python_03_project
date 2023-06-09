import parking_spot_manager # 해당 모듈의 함수들을 사용하기 위해 import
import file_manager         # File을 읽어와야 하므로 해당 모듈을 import

def start_process(path):
    list = file_manager.read_file(path)                         # file_manager 모듈의 read_file 함수를 이용하여 path에 있는 파일을 읽어옴
    spots = parking_spot_manager.str_list_to_class_list(list)   # parking_spot_manager 모듈의 str_list_to_class_list 함수를 이용하여 파일을 읽어와서 만든 list를 변환
    while True:
        print("---menu---")
        print("[1] print")
        print("[2] filter")
        print("[3] sort")
        print("[4] exit")
        select = int(input('type:'))
        if select == 1:
            parking_spot_manager.print_spots(spots)             # spots에 저장된 리스트를 parking_spot_manager 모듈의 print_spots 함수로 출력
            # fill this block
        elif select == 2:
            print("---filter by---")
            print("[1] name")
            print("[2] city")
            print("[3] district")
            print("[4] ptype")
            print("[5] location")
            select = int(input('type:'))
            if select == 1:
                keyword = input('type name:')
                spots = parking_spot_manager.filter_by_name(spots, keyword)         # parking_spot_manager 모듈의 filter함수를 쓴 다음, 기존의 list를 삭제하고 저장
                # fill this block
            elif select == 2:
                keyword = input('type city:')
                spots = parking_spot_manager.filter_by_city(spots, keyword)         # parking_spot_manager 모듈의 filter함수를 쓴 다음, 기존의 list를 삭제하고 저장
                # fill this block
            elif select == 3:
                keyword = input('type district:')
                spots = parking_spot_manager.filter_by_district(spots, keyword)     # parking_spot_manager 모듈의 filter함수를 쓴 다음, 기존의 list를 삭제하고 저장
                # fill this block
            elif select == 4:
                keyword = input('type ptype:')
                spots = parking_spot_manager.filter_by_ptype(spots, keyword)        # parking_spot_manager 모듈의 filter함수를 쓴 다음, 기존의 list를 삭제하고 저장
                # fill this block
            elif select == 5:
                min_lat = float(input('type min lat:'))
                max_lat = float(input('type max lat:')) 
                min_lon = float(input('type min long:'))
                max_lon = float(input('type max long:'))
                keyword = (min_lat, max_lat, min_lon, max_lon)                      # 입력 받은 값들을 tuple로 keyword에 저장
                spots = parking_spot_manager.filter_by_location(spots, keyword)     # parking_spot_manager 모듈의 filter함수를 쓴 다음, 기존의 list를 삭제하고 저장
                # fill this block
            else:
                print("invalid input")
        elif select == 3:
            keywords = ['name', 'city', 'district', 'ptype', 'latitude', 'longitude']
            print("---sort by---")
            print(keywords)
            keyword = input('type keyword:')
            if keyword in keywords:
                spots = parking_spot_manager.sort_by_keyword(spots, keyword)        # parking_spot_manager 모듈의 sort_by_keyword 함수를 쓴 다음, 기존의 list를 삭제하고 저장
                # fill this block
            else: print("invalid input")
        elif select == 4:
            print("Exit")                                        # 4번을 누르면 while문을 빠져나감
            break
            # fill this block
        else:
            print("invalid input")