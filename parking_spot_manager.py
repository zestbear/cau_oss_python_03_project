class parking_spot:
    # you have to implement 'constructor(생성자)' and 'get' method
    def __init__(self, name, city, district, ptype, longitude, latitude):   # name, city, district, ptype, longitude, latitude를 포함하는 생성자를 만듦
        self.__item = {'name':name, 'city':city, 'district':district, 'ptype':ptype, 'longitude':longitude, 'latitude':latitude}

    def __str__(self):
        item = self.__item
        s  = f"[{item['name']}({item['ptype']})] "
        s += f"{item['city']} {item['district']}"
        s += f"(lat:{item['latitude']}, long:{item['longitude']})"
        return s
    
    def get(self, keyword = 'name'):                                      # keyword를 매개변수로 받으며 기본인수가 name인 함수 get
        ret = self.__item.get(keyword)
        return ret                                                          # __item[keyword]를 반환


def str_list_to_class_list(str_list):                                       # str_list를 매개변수로 받아, parking_spot 클래스 객체의 리스트로 변환 후 반환
    for i in range(len(str_list)):                                          # 모든 줄에 대해
        temp = str_list[i].split(',')                                       # ,를 구분자로 하여 나눈 것을 temp에 저장 
        str_list[i] = parking_spot(temp[1], temp[2], temp[3], temp[4], temp[5], temp[6])    # 각각의 6가지 요소들을 생성자를 이용하여 클래스 객체의 리스트로 변환
    return str_list                                                         # 변환한 리스트를 반환
    

def print_spots(spots):                                                     # 출력에 대한 함수
    print(f"---print elements({len(spots)})---")
    for i in range(len(spots)):
        print(str(spots[i]))


def filter_by_name(spots, name):                                                # name으로 filter하는 함수
    arg = [spots[i] for i in range(len(spots)) if name in spots[i].get('name')] # 리스트 함축 기능을 이용하여 필터링한 후, arg 리스트에 넣기
    return arg                                                                  # arg 반환

def filter_by_city(spots, city):                                                # city로 filter하는 함수
    arg = [spots[i] for i in range(len(spots)) if city in spots[i].get('city')] # 리스트 함축 기능을 이용하여 필터링한 후, arg 리스트에 넣기
    return arg                                                                  # arg 반환

def filter_by_district(spots, district):                                                # district로 filter하는 함수
    arg = [spots[i] for i in range(len(spots)) if district in spots[i].get('district')] # 리스트 함축 기능을 이용하여 필터링한 후, arg 리스트에 넣기
    return arg                                                                          # arg 반환

def filter_by_ptype(spots, ptype):                                                      # ptype으로 filter하는 함수
    arg = [spots[i] for i in range(len(spots)) if ptype in spots[i].get('ptype')]       # 리스트 함축 기능을 이용하여 필터링한 후, arg 리스트에 넣기
    return arg                                                                          # arg 반환

def filter_by_location(spots, locations):                                                                               # location으로 filter하는 함수
    arg = [spots[i] for i in range(len(spots)) if locations[0] < float(spots[i].get('latitude')) < locations[1] and     # 리스트 함축 기능을 이용하여 필터링한 후, arg 리스트에 넣기
                                                locations[2] < float(spots[i].get('longitude')) < locations[3]]         # 조건문을 이용하여 범위 설정
    return arg                                                                                                          # arg 반환


def sort_by_keyword(spots, keyword):                                    # 정렬 함수
    sorted_list = sorted(spots, key = lambda x: x.get(keyword))         # lambda와 sorted를 이용하여 정렬한 것을 sorted_list 리스트에 저장
    return sorted_list                                                  # sorted_list 반환


# 각 단계별로 테스트 (테스트할때 주석해제 후 사용)
if __name__ == '__main__':
    print("Testing the module...")
    # version#2
    # import file_manager
    # str_list = file_manager.read_file("./input/free_parking_spot.csv")
    # spots = str_list_to_class_list(str_list)
    # print_spots(spots)

    # version#3
    # spots = filter_by_district(spots, '동작')
    # print_spots(spots)
    
    # version#4
    # spots = sort_by_keyword(spots, 'name')
    # print_spots(spots)