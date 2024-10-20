from parse import *

For_Sequence = "for ("
While_Sequence = "while ("


tuned_input = "for (int row =1;row<=3;row++){for (int col = 1; col <= 5; col = g(col+1)+f(i)) { System.out.print(\"*\");            }            System.out.println()        }    }"
parsed_output = parse_text(tuned_input)

for i in range(len(parsed_output)):
    curr_element = parsed_output[i]
    if type(curr_element) == str:
        loop_body = parsed_output[i+1]
        if For_Sequence in curr_element:
            #F(curr_element, loop_body)
            #if daw need for to be in the beginning 
            print(curr_element, loop_body)
        elif While_Sequence in curr_element:
            #W(curr_element, loop_body)
            #if daw need while to be in the beginning 
            print(curr_element, loop_body)
    elif type(curr_element) == list:
        continue

    
        


