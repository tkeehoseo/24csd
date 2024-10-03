#!/usr/bin/env python3
import argparse

def main():
    parser = argparse.ArgumentParser(
        prog='script.py',
        description='파일 처리 프로그램',
        formatter_class=argparse.RawTextHelpFormatter
    )

    # 전역 옵션
    parser.add_argument('-v', '--verbose', action='count', default=0,
                        help='상세 모드로 실행 (다중 지정 가능)')
    parser.add_argument('-q', '--quiet', action='store_true',
                        help='출력을 생략하고 조용히 실행')
    parser.add_argument('-n', '--number', type=int, choices=range(1, 11), default=5,
                        metavar='NUM', help='1부터 10 사이의 정수 지정 [기본값: 5]')
    parser.add_argument('--config', required=True, help='설정 파일 경로 지정 (필수)')
    parser.add_argument('--list', type=str, metavar='ITEMS',
                        help='처리할 값들의 목록(쉼표로 구분)')
    parser.add_argument('--dict', action='append', metavar='KEY=VALUE',
                        help='키=값 형태의 설정 추가 (다중 지정 가능)')
    group = parser.add_mutually_exclusive_group()
    group.add_argument('--csv', action='store_true', help='CSV 파일로 처리')
    group.add_argument('--json', action='store_true', help='JSON 파일로 처리')

    # 서브 커맨드용 서브 파서
    subparsers = parser.add_subparsers(dest='command', required=True, metavar='COMMAND',
                                       help='사용할 명령을 지정하세요')

    # compress 서브 커맨드
    parser_compress = subparsers.add_parser('compress', help='파일을 압축합니다')
    parser_compress.add_argument('input_file', help='입력 파일 경로')
    parser_compress.add_argument('output_file', help='출력 파일 경로')
    parser_compress.add_argument('--level', type=int, choices=range(1, 10), default=5,
                                 metavar='LEVEL', help='압축 레벨 지정 (1-9) [기본값: 5]')

    # extract 서브 커맨드
    parser_extract = subparsers.add_parser('extract', help='파일을 추출합니다')
    parser_extract.add_argument('input_file', help='입력 파일 경로')
    parser_extract.add_argument('output_file', help='출력 파일 경로')
    parser_extract.add_argument('--dest', default='.', metavar='DEST',
                                help='파일을 추출할 경로 [기본값: 현재 디렉터리]')

    args = parser.parse_args()

    # 나머지 코드는 이전과 동일합니다.
    # ...

if __name__ == '__main__':
    main()
