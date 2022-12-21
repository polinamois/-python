import os


def read_py(file_name):
    try:
        with open(file_name, 'r', encoding='utf-8') as infile:

            lst_lines = infile.readlines()
            for ind, line in enumerate(lst_lines):
                if line.startswith('# title'):
                    title = line.split('title ')[1].strip()
                    link = '-'.join(title.lower().split())
                    all_title = f"+ [{title}](#{link})\n"
                elif line.startswith('# description'):
                    description = line.split('description ')[1].strip()
                elif line.startswith('# ---end---'):
                    end = f"```python \n{''.join(lst_lines[ind + 2:])}```"
                    break

            all_info = f"## {title}\n\n{description}\n\n{end}"
            return all_title, all_info
    except FileNotFoundError:
        print("Ошибка! Файл не найден")
        return None, None


def read_markdown(file_name):
    try:
        with open(file_name, 'r', encoding='utf-8') as infile:
            titles = []
            for line in infile:
                if '+' in line:
                    titles.append(line.strip())
                else:
                    all_info = infile.read()
            titles = '\n'.join(titles)
            return titles, all_info
    except FileNotFoundError:
        print("Ошибка! Файл не найден")
        return None, None


def write_markdown(filename, title_from_py, all_info_from_py, title_from_md=None, all_info_from_md=None):
    with open(filename, 'w', encoding='utf-8') as outfile:
        if title_from_md is not None:
            print(title_from_md, file=outfile)
        print(title_from_py, file=outfile)
        if all_info_from_md is not None:
            print(all_info_from_md, file=outfile)
        print(all_info_from_py, file=outfile)


input_file_py = input("Введите название py файла: ")

# input_file_py = 'solution.py'
# output_file_md = 'out.md'

title_py, all_info_py = read_py(input_file_py)
if title_py is not None and all_info_py is not None:
    output_file_md = input("Введите название md файла: ")
    if os.path.exists(output_file_md) and os.path.getsize(output_file_md):
        title_md, all_info_md = read_markdown(output_file_md)
        if title_md is not None and all_info_py is not None:
            write_markdown(output_file_md, title_py, all_info_py, title_from_md=title_md, all_info_from_md=all_info_md)
    else:
        write_markdown(output_file_md, title_py, all_info_py)