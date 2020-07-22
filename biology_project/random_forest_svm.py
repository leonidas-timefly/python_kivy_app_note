from random import seed
from random import randint
from openpyxl import load_workbook

def split_train_test(dataset, ratio=0.2):
    ratio = 0.2  # 取百分之二十的数据当做测试数据
    num = len(dataset)
    print(len(dataset))
    train_num = int((1-ratio) * num)
    print(train_num)
    k = 0
    dataset_copy = list()
    while k < len(dataset):
        dataset_copy.append(dataset[k])
        k += 1
    train_data = list()
    while len(train_data) < train_num:
        index = randint(0, len(dataset_copy) - 1)
        train_data.append(dataset_copy.pop(index))

    testdata = dataset_copy
    return train_data, testdata

if __name__ == '__main__':
    seed(1)   #每一次执行本文件时都能产生同一个随机数
    datafile = load_workbook(u'D:/python_project/minder/biology_project/random_forest_data.xlsx')
    booksheet = datafile.active
    rows = booksheet.rows
    columns = booksheet.columns
    dataset = list()
    temp = list()
    i = 0
    for row in rows:
        k = 0
        i = i + 1
        line = [col.value for col in row]
        col_sum = 6
        temp = list()
        while k < col_sum:
            cell_data = booksheet.cell(row=i, column=k + 1).value
            temp.append(cell_data)
            k = k + 1
            print(temp)
        dataset.append(temp)
    print(dataset)
    print(dataset[0][:-1])
    train_data, test_data = split_train_test(dataset, ratio=0.6)

    with open('D:/python_project/minder/biology_project/random_forest_svm_train.txt', 'w') as f:
        for k in range(len(train_data)):
            if train_data[k][5] == "RLH":
                f.write(str("1 "))
            elif train_data[k][5] == "Lymphoma":
                f.write(str("2 "))
            for x in range(len(train_data[k]) - 1):
                f.write(str(x + 1) + ":" + str(train_data[k][x]) + " ")
            f.write("\n")

    with open('D:/python_project/minder/biology_project/random_forest_svm_test.txt', 'w') as f:
        for k in range(len(test_data)):
            if test_data[k][5] == "RLH":
                f.write(str("1 "))
            elif test_data[k][5] == "Lymphoma":
                f.write(str("2 "))
            for x in range(len(test_data[k]) - 1):
                f.write(str(x + 1) + ":" + str(test_data[k][x]) + " ")
            f.write("\n")





