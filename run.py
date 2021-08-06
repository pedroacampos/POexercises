import pandas as pd
import numpy as np
import os
import pathlib


class PO:
    def __init__(self, dir_path):
        self.__dir_path = dir_path
        self.__init()

    def by_cpf(self, cpf):
        return self.__data[int(cpf)]["name"][0], self.__data[int(cpf)]

    def max_profitmonth(self, cpf):
        cpf = int(cpf)
        p = self.__data[cpf]
        p["profit"].sort()
        max_profitmonth = p.loc[p["profit"][-1],"month"]
        return max_profitmonth

    def max_lossmonth(self, cpf):
        cpf = int(cpf)
        p = self.__data[cpf]
        p["profit"].sort()
        max_lossmonth = p.loc[p["profit"][0],"month"]
        return max_lossmonth

    def max_loss(self, cpf):
        cpf = int(cpf)
        p = self.__data[cpf]
        p["profit"].sort()
        max_loss = p["profit"][0]
        return max_loss

    def max_profit(self, cpf):
        cpf = int(cpf)
        p = self.__data[cpf]
        p["profit"].sort()
        max_profit = p["profit"][-1]
        return max_profit

    def __init(self):
        self.__data = self.__getdata()

    def __getdata(self):
        dir_files = os.listdir(self.__dir_path)
        data = dict()
        for f in dir_files:
            if not f[-4:] == "xlsx":
                continue

            with pd.ExcelFile(self.__dir_path.joinpath(f)) as xlsx:
                excel = pd.read_excel(xlsx, "profit", na_values=None, header=None)
                ind = dict()
                file_data = dict()
                for v in excel.values:
                    for i, column in enumerate(v):
                        if column == "month":
                            ind[i] = "month"
                            file_data["month"] = []

                            ind[i+1] = "name"
                            file_data["name"] = []

                            ind[i+2] = "cpf"
                            file_data["cpf"] = []

                            ind[i+3] = "profit"
                            file_data["profit"] = []

                            ind[i+4] = "taxed"
                            file_data["taxed"] = []

                            break
                        if pd.isna(column):
                            continue

                        if "month" not in file_data:
                            break
                        file_data[ind[i]].append(column)
            if not file_data:
                continue
            data[file_data["cpf"][0]] = file_data

        return data


if __name__ == '__main__':
    dir_path = pathlib.Path("C:/Users/TRABALHO/Downloads/finalProject/data/")

    po = PO(dir_path)
    print(po.by_cpf("14337315792"))