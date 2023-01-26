##############################IMPORT SECTION#######################################
import pandas as pd


##############################IMPLEMENT SECTION#######################################
def listed_binary(n: int):
    """Liệt kê tất cả các chuỗi nhị phân có độ dài bằng n

    Args:
        n (int): length of binary string

    Yields:
        str: binary string that has length of n
    """
    if n == 0:
        yield ""
    else:
        for bit in ('0', '1'):
            yield from (sbit+bit for sbit in listed_binary(n-1))


def bin2dec(n: str):
    """Converting binary to decimals

    Args:
        n (str): Binary input string

    Returns:
        int: Decimal
    """
    return sum(map(lambda x: x[1]*(2**x[0]), enumerate(map(int, str(n))[::-1])))


def truthtable2df(truthtable):
    """Converting truth table to Pandas dataframe

    Args:
        truthtable (pyeda.boolalg.table.TruthTable): PyEDA truth table

    Returns:
        pandas.DataFrame: truthtable with only lines that has output 1 (edge in graph)
    """
    strtruthtable = str(truthtable)
    rows = strtruthtable.split('\n')
    vals = []
    
    for i in range(1, len(rows)-1):
        if rows[i][-1] == '1':
            obtained_str = rows[i][:-3]
            obtained_str = obtained_str.strip().split(' ')
            obtained_str = list(filter(None, obtained_str))
            vals.append(obtained_str)

    return pd.DataFrame(vals).astype(int)