# 命令行
import click

@click.command()
@click.option("--count", default=1, help="number")
@click.option("--name", prompt="your name")
def hello(count, name):
    for _ in range(count):
        click.echo(f"hello, {name}!")

# if __name__ == '__main__':
    # hello()


# 文件读取
# with open  -- with 状态打开文件，处理完逻辑后自动关闭文件处理器
with open("test/fixture_mini.tsv", 'r', encoding="utf-8") as fin:
    content = fin.readline()

    for line in fin:
        print(line)


# 序列化与反序列化