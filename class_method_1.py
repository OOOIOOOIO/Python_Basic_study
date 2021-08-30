# 객체 지향 프로그래밍(OOP) -> 코드의 재사용, 코드 중복 방지, 유지 보수 수월 등
# 규모가 큰 프로젝트(프로그램) -> 함수 중심 -> 데이터 방대 -> 복잡
# 클래스 중심 -> 데이터 중심 -> 객체로 관리



# 일반적인 코딩

# 차량1
car_company_1 = 'Ferrari'
car_detail_1 = [
    {'color' : 'white'},
    {'horesepower' : 400},
    {'price' : 8000}
]

#차량20
car_company_2 = 'BMW'
car_detail_2 = [
    {'color' : 'black'},
    {'horesepower' : 270},
    {'price' : 5000}
]

#차량3

car_company_3 = 'Audi'
car_detail_3 = [
    {'color' : 'silver'},
    {'horesepower' : 300},
    {'price' : 6000}
]


# 리스트 구조 -> 관리가 불편 , 인덱스 접근 시 실수 가능성, 삭제 불편
car_company_list = ["Ferrari", 'bmw', 'audi']
car_detail_list = [
    {'color' : 'white', 'horesepower' : 400, 'price' : 8000},
    {'color' : 'black', 'horesepower' : 270, 'price' : 5000},
    {'color' : 'silver', 'horesepower' : 300, 'price' : 6000}
]


del car_company_list[1]
del car_detail_list[1]

print(car_company_list)
print(car_detail_list)
print()
print()


# 딕셔너리 구조
# 코드 반복 지속, 중첩 문제(키), 키 조회할 때 예외 처리 등
car_dict = [
    {'car_company' : "Ferrari", "car_detail" : {'color' : 'white', 'horesepower' : 400, 'price' : 8000}},
    {'car_company' : "bmw", "car_detail" : {'color' : 'black', 'horesepower' : 270, 'price' : 5000}},
    {'car_company' : "audi", "car_detail" : {'color' : 'silver', 'horesepower' : 300, 'price' : 6000}}
]

print(car_dict)

# 삭제 pop(key, 'default')
del car_dict[1]

print(car_dict)
print()
print()

# 클래스 구조
# 구조 설계 후 재사용성 증가, 코드 반복 최소화, 메소 활용

class Car() :
    def __init__(self, company, details) :
        self._company = company
        self._detail = details

    def __str__(self) : # java tostring같은 느낌 / print문으로 정보를 확인할 때
        return "str : {} - {}".format(self._company, self._detail)

    def __repr__(self) : # java tostring같은 느낌 / __str__과 비슷하지만 조금 더 타입에 엄격
        return "repr : {} - {}".format(self._company, self._detail)


car1 = Car("Ferrari", {'color' : 'white', 'horesepower' : 400, 'price' : 8000}) # 객체화 및 바로 초기화
car2 = Car("bmw", {'color' : 'black', 'horesepower' : 270, 'price' : 6000})
car3 = Car("audi", {'color' : 'silver', 'horesepower' : 300, 'price' : 5000})

print("__str__ 확인\n")
print(car1) # 객체를 그냥 프린트하면 원래 object~~가 나오지만 def __str__(self)를 해주면 출력 가능(java tostring느낌
print(car2)
print(car3)
print()

print(car1.__dict__) # 속성들을 볼 수 있음
print(car2.__dict__)
print(car3.__dict__)
print()

# 리스트 선언
car_list = []

car_list.append(car1)
car_list.append(car2)
car_list.append(car3)

print("car_list 확인 : ", car_list)
print()

for i in car_list :
    print(i)
