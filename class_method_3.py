# 객체 지향 프로그래밍(OOP) -> 코드의 재사용, 코드 중복 방지, 유지 보수 수월 등
# 규모가 큰 프로젝트(프로그램) -> 함수 중심 -> 데이터 방대 -> 복잡
# 클래스 중심 -> 데이터 중심 -> 객체로 관리

class Car() :
    """             --> java API처럼
    Car class
    Author : Kim
    Data : 2021.08.29
    Description : Class, Static, Instance Method
    """
    # 클래스 변수 영역 --> 모든 객체(인스턴스)가 공유
    price_per_raise = 1.0


    #__init__은 객체화를 위한 메서드
    def __init__(self, company, details) :
        self._company = company
        self._detail = details
        self.car_count = 10000

    # Instance Method
    # Self : 객체의 고유한 속성 값을 사용
    def __str__(self) : # java tostring같은 느낌 / print문으로 정보를 확인할 때
        return "str : {} - {}".format(self._company, self._detail)

    def __repr__(self) : # java tostring같은 느낌 / __str__과 비슷하지만 조금 더 타입에 엄격
        return "repr : {} - {}".format(self._company, self._detail)

    def details_info(self) :
        print("Current ID : {}".format(id(self)))
        print("Car Detail Inofo : {} {}".format(self._company, self._detail.get("price")))

    def get_price(self) :
        return "Befor Car Price --> company : {}, price : {}".format(self._company, self._detail.get('price'))

    def get_price_culc(self) :
        return "After Car Price --> company : {}, price : {}".format(self._company, self._detail.get('price') * Car.price_per_raise)


    # Class Method
    @classmethod # 데코레이터 써줘야됨
    def raise_price(cls, per) : # cls == Car(클래스),  cls.price_per_raise == Car.price_per_raise
        if per <= 1 :
            print("Please enter 1 or more")
            return # 함수를 중단시키고 빠져나간다는 의미
        cls.price_per_raise = per
        print("Succeed! price increased.")


    # Static Method
    @staticmethod
    def is_bmw(inst) : # 매개변수만 있고 self, cls 같은 것은 없음
        if inst._company == "bmw" :
            return "This car is {}".format(inst._company)
        return "Sorry, This car is not {}".format(inst._company)


# self, __init__ 호출
car1 = Car("Ferrari", {'color' : 'white', 'horesepower' : 400, 'price' : 8000}) # 객체화 및 바로 초기화
car2 = Car("bmw", {'color' : 'black', 'horesepower' : 270, 'price' : 6000})

# 전채정보 출력
car1.details_info()
car2.details_info()
print()

# 가격정보 출력(객체로 직접 접근)
print(car1._detail.get('price'))
print(car1._detail['price'])
print()

# 가격정보(인상 전)
print(Car.price_per_raise)
print(car1.get_price())
print(car2.get_price())
print()

# 가격 인상(직접 접근)
Car.price_per_raise = 1.4

# 가격정보(인상 후)
print(Car.price_per_raise)
print(car1.get_price_culc())
print(car2.get_price_culc())
print()
#가격 인상(클래스 메소드 사용)
Car.raise_price(1.6)

# 가격정보(인상 후)
print(Car.price_per_raise)
print(car1.get_price_culc())
print(car2.get_price_culc())
print()

# Staticmethod 확인
print(Car.is_bmw(car1)) # 클래스로 호풀
print(Car.is_bmw(car2))
print()
print(car1.is_bmw(car1)) # 인스턴스로 호출
print(car2.is_bmw(car2))
