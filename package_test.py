print("\n*************************************ex5*************************************")
# 패키지 만들기 실습(package_test.py 파일 및 my_package 패키지 생성 후 실습)
# from 패키지 import 모듈 (ex. from my_package import sum)


# from 패키지.모듈 import 함수, 클래스 (ex. from my_package.sum import sum_ab)

# __name__ ? => 현재 모듈의 이름을 담고 있는 내장 변수

from my_package import sum

x = sum.sum_ab(1, 2)
print(x)

from my_package.sum import sum_ab, Calculator, print_name

test_x = sum_ab(4, 6)
print(test_x)



# 생성자에서 1,3으로 초기화 하겠다 라는 의미
c = Calculator(1,3)
# 객체 c 안에 있는 sum을 호출
print(f"c.sum() : {c.sum()}")
# __name__ => 현재 모듈의 이름을 담고 있는 내장 변수
# 특정 파일을 실행했을 때 __name__이  __main__ 으로 되어있어서
# if로 __name__이 맞을 때 출력하도록 코딩해서 확인해봄봄if __name__ == '__main__':
if __name__ == '__main__':
    test_x = sum_ab(4, 6)
    print(test_x)
    print("test of __name__ stmt")
    print(f"my_package.py 모듈의 __name__: {__name__}")
    print_name()