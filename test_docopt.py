#!/usr/bin/env python3
"""
파일 처리 프로그램

Usage:
  script.py [OPTIONS] compress <input_file> <output_file>
  script.py [OPTIONS] extract <input_file> <output_file>

Options:
  -h, --help                 도움말을 출력합니다.
  -v, --verbose              상세 모드로 실행 (다중 지정 가능)
  -q, --quiet                출력을 생략하고 조용히 실행
  -n NUM, --number NUM       1부터 10 사이의 정수 지정 [기본값: 5]
  --config CONFIG            설정 파일 경로 지정 (필수)
  --list ITEMS               처리할 값들의 목록(쉼표로 구분)
  --dict KEY=VALUE           키=값 형태의 설정 추가 (다중 지정 가능)
  --csv                      CSV 파일로 처리
  --json                     JSON 파일로 처리

Commands:
  compress                   파일을 압축합니다
  extract                    파일을 추출합니다

compress 명령 옵션:
  --level LEVEL              압축 레벨 지정 (1-9) [기본값: 5]

extract 명령 옵션:
  --dest DEST                파일을 추출할 경로 [기본값: 현재 디렉터리]
"""

from docopt import docopt

def main():
    args = docopt(__doc__, options_first=False)

    # 나머지 코드는 이전과 동일합니다.
    # ...

if __name__ == '__main__':
    main()

    # 전역 옵션 처리
    verbose = args['--verbose']
    quiet = args['--quiet']
    number = int(args['--number'])
    config = args['--config']
    if not config:
        print("에러: --config 옵션은 필수입니다.")
        exit(1)
    list_items = args['--list'].split(',') if args['--list'] else None
    dict_values = args['--dict']
    if dict_values:
        if isinstance(dict_values, str):
            dict_values = [dict_values]
    else:
        dict_values = []
    csv = args['--csv']
    json = args['--json']
    file_format = 'csv' if csv else 'json' if json else None

    # 명령어와 인자 처리
    command = 'compress' if args['compress'] else 'extract'
    input_file = args['<input_file>']
    output_file = args['<output_file>']

    if not quiet:
        print(f"입력 파일: {input_file}")
        print(f"출력 파일: {output_file}")
        print(f"설정 파일: {config}")
        print(f"선택된 숫자: {number}")

        if list_items:
            print("목록 인자:")
            for item in list_items:
                print(f"- {item}")

        if dict_values:
            print("키-값 쌍 인자:")
            for kv in dict_values:
                if '=' in kv:
                    key, value = kv.split('=', 1)
                    print(f"{key} = {value}")
                else:
                    print(f"잘못된 형식: {kv}")

    if command == 'compress':
        level = int(args['--level'])
        if not quiet:
            print(f"압축을 시작합니다. 레벨: {level}")
    elif command == 'extract':
        dest = args['--dest']
        if not quiet:
            print(f"파일을 '{dest}' 경로로 추출합니다.")

    # 파일 형식 처리
    if not quiet:
        if file_format == 'csv':
            print("CSV 파일로 처리합니다.")
        elif file_format == 'json':
            print("JSON 파일로 처리합니다.")
        else:
            print("기본 파일 형식으로 처리합니다.")

if __name__ == '__main__':
    main()
