#the cells hold 8 bit ints internally but are converted where/when needed.
def get_all_loops(bf_input_code):
    loops = []
    for __ in range(0, len(bf_input_code)):
        if bf_input_code[__] == "[" or bf_input_code[__] == "]":
            loops.append(__)
    return(loops)

def extract_code_from_file_and_run(bf_input_code_path, enter_to_exit=False, return_output=False):
    with open(bf_input_code_path, "r") as input_code:
        interpreter(input_code.read(), enter_to_exit, return_output)
        input_code.close()

def interpreter(bf_input_code, enter_to_exit=False, return_output=False):

    loops = get_all_loops(bf_input_code)
#    print(loops)
    current_loop_list_item = -1
    bf_code_len = len(bf_input_code)
    data_pointer = 0
    data_list = []
    cells = 100001
    done_loop = None
    # inst_pointer always gets 1 added to it every loop. so on loop 0, the inst_pointer will be 0 because -1 + 1 = 0
    inst_pointer = -1
    printed_output = ""
    print("\n\n== START OF BRAINFUCK PROGRAM == \n")
    for _ in range(0, cells):
        data_list.append(0)
    while not done_loop:
#        print(data_pointer)
        inst_pointer = inst_pointer + 1
        match bf_input_code[inst_pointer]:
            case ".":
#                print(".")
                calued_data = chr(data_list[data_pointer])
                printed_output = calued_data
                print(calued_data, end="")
            case "+":
#                print(data_pointer)
                data_list[data_pointer] = data_list[data_pointer] + 1
                if data_list[data_pointer] > 255:
                    data_list[data_pointer] = 0
            case "-":
                data_list[data_pointer] = data_list[data_pointer] - 1
                if data_list[data_pointer] < 0:
                    data_list[data_pointer] = 255
            case ">":
                data_pointer = data_pointer + 1
                if data_pointer >= cells:
                    data_pointer = 0
            case "<":
                data_pointer = data_pointer - 1
                if data_pointer <= 0:
                    data_pointer = cells
            case ",":
                data_list[data_pointer] = int(input("").encode(), 16)
            case "[":   
                current_loop_list_item = current_loop_list_item + 1
#                current_loop_list_item = current_loop_list_item + 1
                if data_list[data_pointer] == 0:
                    current_loop_list_item = current_loop_list_item + 1
                    inst_pointer = loops[current_loop_list_item]
##                    print("exit loop, data at pointer is 0")
            case "]":
#                current_loop_list_item = current_loop_list_item + 1
                if data_list[data_pointer] != 0:
                    inst_pointer = loops[current_loop_list_item]
##                    print("L")
##                    print(loops[current_loop_list_item])
##                    print(inst_pointer)
                elif data_list[data_pointer] == 0:
                    current_loop_list_item = current_loop_list_item + 1
#                    inst_pointer = inst_pointer + 1
        if (inst_pointer + 1) == bf_code_len:
            print("\n\n== the program has ended. ==")
            if enter_to_exit:
                input("press enter to exit")
            if return_output:
                return printed_output
            return
if __name__ == "__main__":
    extract_code_from_file_and_run(input("input file: "), enter_to_exit=True)
