import traceback
def main():
    try:
        first_prompt = "What happened today? "
        next_prompt = "What else? "
        prompt = first_prompt

        with open("diary.txt", "a") as diary:
            while True:
                line = input(prompt)

                if line == "done for now":
                    diary.write(line + "\n")
                    break

                diary.write(line + "\n")

                prompt = next_prompt

    except Exception as e:
        trace_back = traceback.extract_tb(e.__traceback__)
        stack_trace = list()
        for trace in trace_back:
            stack_trace.append(
                f'File : {trace[0]} , Line : {trace[1]}, Func.Name : {trace[2]}, Message : {trace[3]}'
            )
        print(f"Exception type: {type(e).__name__}")
        message = str(e)
        if message:
            print(f"Exception message: {message}")
        print(f"Stack trace: {stack_trace}")


if __name__ == "__main__":
    main()
