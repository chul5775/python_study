'''-------------------------------------------------------
------------------------- 함수  ----------------------------
----------------------------------------------------------
<개요> 함수의 특징
        - 재활용을 목표로 반복소스를 단순화
        - 함수의 이름은 주소를 기억하고 있다.(함수는 객체의 주소를 기억하고 있다.)
        
==========================================================



------------------- (1) 내장 함수 --------------------------'''
print('\n--<실습1>--')
print(sum([3,5,7]))
print(bin(8))
print(int(1.7), float(3), str(5) + '오')

'''----------------- (1-1) 수학을 위한 내장 함수  ---------------'''
print('\n--<실습2>--')
import math
print(math.ceil(1.2), math.ceil(1.7))
print(math.floor(1.2), math.floor(1.7))

'''----------------- (1-2) boolean 내장 함수 ----------------'''
print('\n--<실습3>--')
aa = [1,3,2,5,6,7]
result = all(a < 10 for a in aa)
print('모든 숫자가 10 미만이냐?', result)
result = any(a < 3 for a in aa)
print('숫자 중에서 3 미만이 있냐?', result)
#...

'''----------------- (1-3) globals 내장함수  -------------------
    - globals()를 사용하면 현재 사용중인 객체들을 알  수 있다.
    
    - Tip) dir(__builtins__)로 전역변수 까지 모두 확인 가능하다.
    - 근데, eclipse에서 사용 안됨. 확인을 원하면 Python 3.7 program으로 확인.
    
'''
print('**' * 20)
print('\n--<실습4>--')
print('현재 파일의 객체 목록 :', globals())
print('**' * 20)

'''=======================================================



-------------------- (2) 사용자 정의 함수 ---------------------'''
print('\n--<실습5>--')

def DoFunc1():
    print('DoFunc1 처리')

DoFunc1()

'''----------------- (2-1) 사용자 함수를 이용한 덧셈 --------------'''
print('\n--<실습6>--')
def DoFunc2(arg1, arg2):
    DoFunc3()
    return arg1 + arg2
    
def DoFunc3():
    print('다른 함수 호출');
print()

aa = DoFunc2(1,2)
print(aa)

aa = DoFunc2("대한", "민국")
print(aa)

print('사용자 함수가 현재 사용 하고 있는 주소:',id(DoFunc2))

'''----------------- (2-2) 함수를 이용한 데이터 SWAP ------------'''
print('\n--<실습7>--')
def swap(a, b):
    return b, a

a = 10; b = 20;

print(swap(a, b))

'''---------------- (2-3) if조건에 함수 사용 (홀수만 뽑아보기) ----------
    <설명>
        - 함수를 가지고 
        - 이곳에서는 dict타입으로 뽑아본다. (Key: Value)
'''
print('\n--<실습8>--')
def isOdd(arg):
    return arg % 2 == 1

mydict = {x:x*x for x in range(11) if isOdd(x)}
print(mydict)

'''========================================================='''
