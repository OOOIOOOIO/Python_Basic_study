# 객체 지향 프로그래밍(OOP) -> 코드의 재사용, 코드 중복 방지, 유지 보수 수월 등
# 규모가 큰 프로젝트(프로그램) -> 함수 중심 -> 데이터 방대 -> 복잡
# 클래스 중심 -> 데이터 중심 -> 객체로 관리

class Car() :
    """             --> java API처럼
    Car class
    Author : Kim
    Data : 2021.08.28
    """
    # 클래스 변수 영역 --> 모든 객체가 공유
    car_count = 0


    #__init__은 객체화를 위한 메서드
    def __init__(self, company, details) :
        self._company = company
        self._detail = details
        self.car_count = 10000
        Car.car_count += 1 # __init__이 호출될 때마다 실행 --> 객체화 할 때마다

    def __str__(self) : # java tostring같은 느낌 / print문으로 정보를 확인할 때
        return "str : {} - {}".format(self._company, self._detail)

    def __repr__(self) : # java tostring같은 느낌 / __str__과 비슷하지만 조금 더 타입에 엄격
        return "repr : {} - {}".format(self._company, self._detail)

    def __del__(self) :
        print("delete?")
        Car.car_count -= 1

    def details_info(self) :
        print("Current ID : {}".format(id(self)))
        print("Car Detail Inofo : {} {}".format(self._company, self._detail.get("price")))

# self __init__ 호출
car1 = Car("Ferrari", {'color' : 'white', 'horesepower' : 400, 'price' : 8000}) # 객체화 및 바로 초기화
car2 = Car("bmw", {'color' : 'black', 'horesepower' : 270, 'price' : 6000})
car3 = Car("audi", {'color' : 'silver', 'horesepower' : 300, 'price' : 5000})

# ID 확인
print(id(car1)) # 각자 고유의 값을 가지고 있음(-->self)
print(id(car2))
print(id(car3))

print(car1._company == car2._company) # 고유값이 다른 것을 확인
print(car1 is car2) # 고유값이 다른 것을 확인
print()

#dir, __dict__ 확인
print(dir(car1))
print(car1.__dict__)
print()


# Doctring # API 출력
print(Car.__doc__)
print()


# 실행
car1.details_info()
Car.details_info(car1) # 클래스 이름으로 접근할 때 --> Car클래스의 car2 객체를 볼래!
print()
car2.details_info()
Car.details_info(car2) # 같은 의미
print()

# 비교
print(car1.__class__, car2.__class__) #부모 클래스가 같아서 id가 같다
print(id(car1.__class__), id(car2.__class__)) # id가 같게 나옴
print()

# 에러
#Car.details_info() # 오류 --> 클래스 자체는 self가 없기 때문

# 클래스변수 확인
print(car1.car_count)
print(car2.car_count)
print(dir(car1)) # 클래스 변수를 확인할 때 __dict__보다는 dir이 나음
print()

# 클래스 변수에 접근
print(Car.car_count)
print(car1.car_count)
print()

# __del__ 확인
del(car2) # 사용법
print(Car.car_count)
print(car1.car_count)

# 인스턴스 네임스페이스에 없으면 상위에서 검색
# 즉, 동일한 이름으로 변수 생성 가능
# (검색 순서 : 인스턴스(자기자신) 검색 후 -> 상위(클래스 변수), 부모 클래스 변수)
