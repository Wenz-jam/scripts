#!/usr/bin/python3
import argparse
from docx import Document
from docx.enum.text import WD_PARAGRAPH_ALIGNMENT
from docx.shared import Pt,Cm
import random
"""
用法：
    python oral-arithmetic.py [-h] [-p PAGES] [-n NR_DOCS] [-l LIMIT]
    ./oral-arithmetic.py [-h] [-p PAGES] [-n NR_DOCS] [-l LIMIT]

描述：
    生成口算练习题 每页100题 不生成答案

选项：
    -h, --help              显示帮助消息并退出.
    -p PAGES, --pages PAGES
                            每个文档的页数(默认值:20).
    -n NR_DOCS, --nr-doc NR_DOCS
                            要生成的文档数量(默认值:1).
    -l LIMIT, --limit LIMIT
                            口算题的最大值(默认值:100).

示例：
    1. 使用默认设置生成口算题：
        python arithmetic_problem_generator.py

    2. 使用自定义设置生成口算题：
        python arithmetic_problem_generator.py -p 30 -n 2 -l 50
效率: i7-12700H
    time ./oral-arithmetic.py -p 40 -n 10 -l 20
    ________________________________________________________
    Executed in   16.72 secs    fish           external
    usr time      16.65 secs    31.31 millis   16.62 secs
    sys time      0.06 secs     2.55  millis   0.06 secs

"""
def generate(limit, size=100):
    operators = ['+', '-', '*', '/']
    questions = []
    for _ in range(size):
        num1 = random.randint(1, limit)
        num2 = random.randint(1, limit)
        operator = operators[random.randint(0, 1)]
        question = f"{num1} {operator} {num2}"
        val = eval(question)
        if not (0 < val < limit):
            continue
        questions.append(f"{question} = ____")
    return questions


def create_word_document(filename, limit=20, pages=10):
    document = Document()
    document.styles['Normal'].font.size = Pt(11)
    document.sections[0].page_width = Cm(21)  # A4纸宽度
    document.sections[0].page_height = Cm(29.7)  # A4纸宽度
    questions = []
    for page_num in range(pages):
        table = document.add_table(rows=25, cols=4)
        table.alignment = WD_PARAGRAPH_ALIGNMENT.CENTER
        for row in table.rows:
            for idx, cell in enumerate(row.cells):
                if len(questions) == 0:
                    questions = generate(limit=limit, size=100)
                cell.text = questions.pop()
        document.add_page_break()
    document.save(filename)


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Process some integers.')
    parser.add_argument('-p', '--pages', dest='pages', type=int, default=20, help='page number')
    parser.add_argument('-n', '--nr-doc', dest='nr_docs', type=int, default=1, help='number of docs')
    parser.add_argument('-l', '--limit', dest='limit', type=int, default=100, help='limit number')

    args = parser.parse_args()
    pages = args.pages
    limit = args.limit
    nr_docs = args.nr_docs
    for i in range(nr_docs):
        create_word_document(f"{limit}以内口算{'' if i == 0  else i}.docx", limit=limit, pages=pages)
