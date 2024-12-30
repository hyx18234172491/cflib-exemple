from decimal import Decimal, getcontext

# 设置小数精度
getcontext().prec = 20

def process_file(file_path):
    try:
        with open(file_path, 'r') as file:
            for line in file:
                # Strip any whitespace and split the line by comma
                tRound1, tReply1 = map(int, line.strip().split(','))

                # 使用 Decimal 进行高精度计算
                diff = tRound1 - tReply1
                multiple = Decimal(tRound1) / Decimal(tReply1)

                # 输出结果，倍数保留高精度
                print(f"diff:{tRound1},{tReply1} 差值:{diff} 倍数:{multiple}")
    except FileNotFoundError:
        print("The specified file was not found.")
    except Exception as e:
        print(f"An error occurred: {e}")

# Example usage
process_file('200ms.txt')
