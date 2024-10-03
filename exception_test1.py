l1 = [1,2,3,4,5]
print(f'{l1=}')
def func1():
    i1 = int(input('첨자를 입력하세요: '))
    print(f'l1[{i1}]={l1[i1]}')

try:
    func1()
except ValueError:
    print('인덱스는 정수를 입력하세요')
except IndexError:
    print('인덱스가 범위를 초과함')
else:
    print('인덱스가 범위를 초과하지 않음')
finally:
    print('프로그램 종료')
