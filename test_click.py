#!/usr/bin/env python3
import click

# 키-값 쌍을 파싱하는 커스텀 타입
def parse_key_value(ctx, param, value):
    kv_list = []
    for kv in value:
        if '=' in kv:
            kv_list.append(kv)
        else:
            raise click.BadParameter(f"'{kv}'는 'KEY=VALUE' 형식이 아닙니다.")
    return kv_list

@click.group(context_settings=dict(help_option_names=['-h', '--help']))
@click.option('-v', '--verbose', count=True, default=0, help='상세 모드로 실행 (다중 지정 가능)')
@click.option('-q', '--quiet', is_flag=True, help='출력을 생략하고 조용히 실행')
@click.option('-n', '--number', type=click.IntRange(1, 10), default=5, show_default=True,
              metavar='NUM', help='1부터 10 사이의 정수 지정')
@click.option('--config', required=True, type=click.Path(), help='설정 파일 경로 지정 (필수)')
@click.option('--list', type=str, metavar='ITEMS',
              help='처리할 값들의 목록(쉼표로 구분)')
@click.option('--dict', 'dict_values', multiple=True, callback=parse_key_value,
              metavar='KEY=VALUE', help='키=값 형태의 설정 추가 (다중 지정 가능)')
@click.option('--csv', 'file_format', flag_value='csv', help='CSV 파일로 처리')
@click.option('--json', 'file_format', flag_value='json', help='JSON 파일로 처리')
@click.pass_context
def cli(ctx, verbose, quiet, number, config, list, dict_values, file_format):
    """
    파일 처리 프로그램

    Usage:
      script.py [OPTIONS] COMMAND [ARGS]...
    """
    ctx.ensure_object(dict)
    ctx.obj['verbose'] = verbose
    ctx.obj['quiet'] = quiet
    ctx.obj['number'] = number
    ctx.obj['config'] = config
    ctx.obj['list'] = list.split(',') if list else None
    ctx.obj['dict'] = dict_values
    ctx.obj['file_format'] = file_format

@cli.command(help='파일을 압축합니다')
@click.argument('input_file')
@click.argument('output_file')
@click.option('--level', type=click.IntRange(1, 9), default=5, show_default=True,
              metavar='LEVEL', help='압축 레벨 지정 (1-9)')
@click.pass_context
def compress(ctx, input_file, output_file, level):
    """compress 명령 옵션:"""
    # 나머지 코드는 이전과 동일합니다.
    # ...

@cli.command(help='파일을 추출합니다')
@click.argument('input_file')
@click.argument('output_file')
@click.option('--dest', default='.', show_default=True, metavar='DEST',
              help='파일을 추출할 경로')
@click.pass_context
def extract(ctx, input_file, output_file, dest):
    """extract 명령 옵션:"""
    # 나머지 코드는 이전과 동일합니다.
    # ...

if __name__ == '__main__':
    cli(prog_name='script.py')
