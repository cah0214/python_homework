import csv
import traceback
import sys
import os
import custom_module
from datetime import datetime


def read_employees():
    try:
        result = {}
        rows = []

        with open("../csv/employees.csv", newline="") as f:
            reader = csv.reader(f)

            for index, row in enumerate(reader):
                if index == 0:
                    result["fields"] = row
                else:
                    rows.append(row)

        result["rows"] = rows
        return result

    except Exception as e:
        trace_back = traceback.extract_tb(e.__traceback__)
        stack_trace = []
        for trace in trace_back:
            stack_trace.append(
                f'File : {trace[0]} , Line : {trace[1]}, Func.Name : {trace[2]}, Message : {trace[3]}'
            )
        print(f"Exception type: {type(e).__name__}")
        message = str(e)
        if message:
            print(f"Exception message: {message}")
        print(f"Stack trace: {stack_trace}")
        sys.exit(1)

def _read_minutes_file(path):
    try:
        result = {}
        rows = []

        with open(path, newline="") as f:
            reader = csv.reader(f)

            for index, row in enumerate(reader):
                if index == 0:
                    result["fields"] = row
                else:
                    # store rows as tuples
                    rows.append(tuple(row))

        result["rows"] = rows
        return result

    except Exception as e:
        trace_back = traceback.extract_tb(e.__traceback__)
        stack_trace = []
        for trace in trace_back:
            stack_trace.append(
                f'File : {trace[0]} , Line : {trace[1]}, Func.Name : {trace[2]}, Message : {trace[3]}'
            )
        print(f"Exception type: {type(e).__name__}")
        message = str(e)
        if message:
            print(f"Exception message: {message}")
        print(f"Stack trace: {stack_trace}")
        sys.exit(1)
def read_minutes():
    try:
        minutes1 = _read_minutes_file("../csv/minutes1.csv")
        minutes2 = _read_minutes_file("../csv/minutes2.csv")
        return minutes1, minutes2

    except Exception as e:
        trace_back = traceback.extract_tb(e.__traceback__)
        stack_trace = []
        for trace in trace_back:
            stack_trace.append(
                f'File : {trace[0]} , Line : {trace[1]}, Func.Name : {trace[2]}, Message : {trace[3]}'
            )
        print(f"Exception type: {type(e).__name__}")
        message = str(e)
        if message:
            print(f"Exception message: {message}")
        print(f"Stack trace: {stack_trace}")
        sys.exit(1)


def column_index(column_name):
    try:
        fields = employees["fields"]
        return fields.index(column_name)

    except Exception as e:
        trace_back = traceback.extract_tb(e.__traceback__)
        stack_trace = []
        for trace in trace_back:
            stack_trace.append(
                f'File : {trace[0]} , Line : {trace[1]}, Func.Name : {trace[2]}, Message : {trace[3]}'
            )
        print(f"Exception type: {type(e).__name__}")
        message = str(e)
        if message:
            print(f"Exception message: {message}")
        print(f"Stack trace: {stack_trace}")
        sys.exit(1)
def first_name(row_number):
    try:
        # which column is first_name?
        first_name_col = column_index("first_name")

        # get the row from employees["rows"]
        row = employees["rows"][row_number]

        # return that value
        return row[first_name_col]

    except Exception as e:
        trace_back = traceback.extract_tb(e.__traceback__)
        stack_trace = []
        for trace in trace_back:
            stack_trace.append(
                f'File : {trace[0]} , Line : {trace[1]}, Func.Name : {trace[2]}, Message : {trace[3]}'
            )
        print(f"Exception type: {type(e).__name__}")
        message = str(e)
        if message:
            print(f"Exception message: {message}")
        print(f"Stack trace: {stack_trace}")
        sys.exit(1)

def employee_find(employee_id):
    try:
        def employee_match(row):
            return int(row[employee_id_column]) == employee_id

        matches = list(filter(employee_match, employees["rows"]))
        return matches

    except Exception as e:
        trace_back = traceback.extract_tb(e.__traceback__)
        stack_trace = []
        for trace in trace_back:
            stack_trace.append(
                f'File : {trace[0]} , Line : {trace[1]}, Func.Name : {trace[2]}, Message : {trace[3]}'
            )
        print(f"Exception type: {type(e).__name__}")
        message = str(e)
        if message:
            print(f"Exception message: {message}")
        print(f"Stack trace: {stack_trace}")
        sys.exit(1)        

def employee_find_2(employee_id):
    try:
        matches = list(
            filter(
                lambda row: int(row[employee_id_column]) == employee_id,
                employees["rows"]
            )
        )
        return matches

    except Exception as e:
        trace_back = traceback.extract_tb(e.__traceback__)
        stack_trace = []
        for trace in trace_back:
            stack_trace.append(
                f'File : {trace[0]} , Line : {trace[1]}, Func.Name : {trace[2]}, Message : {trace[3]}'
            )
        print(f"Exception type: {type(e).__name__}")
        message = str(e)
        if message:
            print(f"Exception message: {message}")
        print(f"Stack trace: {stack_trace}")
        sys.exit(1)

def sort_by_last_name():
    try:
        last_name_col = column_index("last_name")

        employees["rows"].sort(key=lambda row: row[last_name_col])

        return employees["rows"]

    except Exception as e:
        trace_back = traceback.extract_tb(e.__traceback__)
        stack_trace = []
        for trace in trace_back:
            stack_trace.append(
                f'File : {trace[0]} , Line : {trace[1]}, Func.Name : {trace[2]}, Message : {trace[3]}'
            )
        print(f"Exception type: {type(e).__name__}")
        message = str(e)
        if message:
            print(f"Exception message: {message}")
        print(f"Stack trace: {stack_trace}")
        sys.exit(1)
def employee_dict(row):
    try:
        result = {}

        # skip employee_id (index 0)
        fields = employees["fields"][1:]
        values = row[1:]

        for key, value in zip(fields, values):
            result[key] = value

        return result

    except Exception as e:
        trace_back = traceback.extract_tb(e.__traceback__)
        stack_trace = []
        for trace in trace_back:
            stack_trace.append(
                f'File : {trace[0]} , Line : {trace[1]}, Func.Name : {trace[2]}, Message : {trace[3]}'
            )
        print(f"Exception type: {type(e).__name__}")
        message = str(e)
        if message:
            print(f"Exception message: {message}")
        print(f"Stack trace: {stack_trace}")
        sys.exit(1)
def all_employees_dict():
    try:
        result = {}

        for row in employees["rows"]:
            emp_id = row[employee_id_column]
            result[emp_id] = employee_dict(row)

        return result

    except Exception as e:
        trace_back = traceback.extract_tb(e.__traceback__)
        stack_trace = []
        for trace in trace_back:
            stack_trace.append(
                f'File : {trace[0]} , Line : {trace[1]}, Func.Name : {trace[2]}, Message : {trace[3]}'
            )
        print(f"Exception type: {type(e).__name__}")
        message = str(e)
        if message:
            print(f"Exception message: {message}")
        print(f"Stack trace: {stack_trace}")
        sys.exit(1)

def get_this_value():
    try:
        return os.getenv("THISVALUE")

    except Exception as e:
        trace_back = traceback.extract_tb(e.__traceback__)
        stack_trace = []
        for trace in trace_back:
            stack_trace.append(
                f'File : {trace[0]} , Line : {trace[1]}, Func.Name : {trace[2]}, Message : {trace[3]}'
            )
        print(f"Exception type: {type(e).__name__}")
        message = str(e)
        if message:
            print(f"Exception message: {message}")
        print(f"Stack trace: {stack_trace}")
        sys.exit(1)

def set_that_secret(new_secret):
    try:
        custom_module.set_secret(new_secret)

    except Exception as e:
        trace_back = traceback.extract_tb(e.__traceback__)
        stack_trace = []
        for trace in trace_back:
            stack_trace.append(
                f'File : {trace[0]} , Line : {trace[1]}, Func.Name : {trace[2]}, Message : {trace[3]}'
            )
        print(f"Exception type: {type(e).__name__}")
        message = str(e)
        if message:
            print(f"Exception message: {message}")
        print(f"Stack trace: {stack_trace}")
        sys.exit(1)

def create_minutes_set():
    try:
        # create sets from the rows of minutes1 and minutes2
        set1 = set(minutes1["rows"])
        set2 = set(minutes2["rows"])

        # combine into one set (union)
        combined = set1.union(set2)

        return combined

    except Exception as e:
        trace_back = traceback.extract_tb(e.__traceback__)
        stack_trace = []
        for trace in trace_back:
            stack_trace.append(
                f'File : {trace[0]} , Line : {trace[1]}, Func.Name : {trace[2]}, Message : {trace[3]}'
            )
        print(f"Exception type: {type(e).__name__}")
        message = str(e)
        if message:
            print(f"Exception message: {message}")
        print(f"Stack trace: {stack_trace}")
        sys.exit(1)

def create_minutes_list():
    try:
        minutes_list_local = list(minutes_set)

        converted = list(
            map(
                lambda x: (x[0], datetime.strptime(x[1], "%B %d, %Y")),
                minutes_list_local,
            )
        )

        return converted

    except Exception as e:
        trace_back = traceback.extract_tb(e.__traceback__)
        stack_trace = []
        for trace in trace_back:
            for trace in trace_back:
                stack_trace.append(
                    f'File : {trace[0]} , Line : {trace[1]}, Func.Name : {trace[2]}, Message : {trace[3]}'
                )
        print(f"Exception type: {type(e).__name__}")
        message = str(e)
        if message:
            print(f"Exception message: {message}")
        print(f"Stack trace: {stack_trace}")
        sys.exit(1)
def write_sorted_list():
    try:
        minutes_sorted = list(minutes_list)

        minutes_sorted.sort(key=lambda x: x[1])

        converted = list(
            map(
                lambda x: (x[0], x[1].strftime("%B %d, %Y")),
                minutes_sorted,
            )
        )

        with open("minutes.csv", "w", newline="") as f:
            writer = csv.writer(f)
            writer.writerow(minutes1["fields"])
            for row in converted:
                writer.writerow(row)

        return converted

    except Exception as e:
        trace_back = traceback.extract_tb(e.__traceback__)
        stack_trace = []
        for trace in trace_back:
            stack_trace.append(
                f'File : {trace[0]} , Line : {trace[1]}, Func.Name : {trace[2]}, Message : {trace[3]}'
            )
        print(f"Exception type: {type(e).__name__}")
        message = str(e)
        if message:
            print(f"Exception message: {message}")
        print(f"Stack trace: {stack_trace}")
        sys.exit(1)



# ---- GLOBALS FOR TESTS ----
employees = read_employees()
employee_id_column = column_index("employee_id")

print(employees)
print(employee_id_column)

all_employees = all_employees_dict()
print(all_employees)

minutes1, minutes2 = read_minutes()
print(minutes1)
print(minutes2)

minutes_set = create_minutes_set()
print(minutes_set)

minutes_list = create_minutes_list()
print(minutes_list)

