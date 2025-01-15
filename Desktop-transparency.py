from os import system, listdir, path, rename, getcwd


def main(suffix):
    str_data = ' '  # 此处不是空格而是透明字符, 对Win 生效, Linux 没有尝试过.
    file_list = listdir()

    for i in file_list:
        file_name, file_suffix = path.splitext(i)
        if file_suffix == suffix:
            src = path.join(getcwd(), i)
            rename(src=path.join(getcwd(), i), dst=path.join(getcwd(), f'{str_data}{file_suffix}'))
            str_data += ' '
            print(f'{path.join(getcwd(), i)} -->[ {file_suffix}]')


if __name__ == '__main__':
    print("将本脚本放置Windows桌面环境中运行.")
    print("将会把所有lnk后缀变为透明字符.")

    print()

    print("Place this script to run in a Windows desktop environment.")
    print("Will turn all lnk suffixes into transparent characters.")

    print()

    print('请输入需要变为透明的后缀, 如不输入则是文件夹')
    print('例如:\n.lnk\n.ico\n什么也不输入.')

    print()

    print('Please enter the suffix that needs to be transparent, or folder if not entered.')
    print('For example :\n.lnk\n.ico\nType nothing.')

    print()

    suffix = str(input("\aPlease enter/请输入:"))
    main(suffix)
    system('pause')
