import csv
import os

def file_coercer(input_file, output_file):
    out = "var exp_lists = ["
    with open(input_file) as csv_file:
        csv_reader = csv.reader(csv_file, delimiter = ",")
        for line in csv_reader:
            if line[0] == "stm":
                out = out
            elif line[1] != "215" and line[12] == "2":
                out = out + "{\"audio\": \"" + line[7] + "\", \"criticality\": \"" + line[8] + "\", \"condition\": \"" + line[11] + "\", \"exp_list\": \"" + line[15] + "\", \"image_left_type\": \""
                if line[13] == "Left":
                    out = out + "Target\", \"img_right_type\": \"Distractor\", \"img_left\": \"" + line[2] + "\", \"img_right\": \"" + line[3] + "\"}," 
                else:
                    out = out + "Target\", \"img_right_type\": \"Distractor\", \"img_left\": \"" + line[3] + "\", \"img_right\": \"" + line[2] + "\"}," 
            elif line[1] == "215" and line[12] == "2":
                out = out + "{\"audio\": \"" + line[7] + "\", \"criticality\": \"" + line[8] + "\", \"condition\": \"" + line[11] + "\", \"exp_list\": \"" + line[15] + "\", \"image_left_type\": \""
                if line[13] == "Left":
                    out = out + "Target\", \"img_right_type\": \"Distractor\", \"img_left\": \"" + line[2] + "\", \"img_right\": \"" + line[3] + "\"}]" 
                else:
                    out = out + "Target\", \"img_right_type\": \"Distractor\", \"img_left\": \"" + line[3] + "\", \"img_right\": \"" + line[2] + "\"}]"  
            else:
                out = out
    new_file = open(output_file, "w")
    new_file.write(out)
    new_file.close()



file_in_question = "./2AFC VWP STIM/Randomization/ListA1_PhonoComp_FINAL.csv"

output_file = "./eyetracking_template-master/js/exp_files/exp_lists.js"

file_coercer(file_in_question, output_file)
