import argparse,re

parser = argparse.ArgumentParser()

parser.add_argument("infile", type = str)

args = parser.parse_args()

edited_text = ""

with open(args.infile,"r") as infile:
    text = infile.readlines()
    # infile.seek(0)
    line = 0
    edited_text = ""
    skip_str = ""
    while(line<len(text)):
        index1,index2 = text[line].find('"""'),text[line].find("'''")
        if skip_str=="" and index1!=-1:
            skip_str = '"""'
            edited_text+=text[line][:index1]
            i,LENGTH = 0,len(text[line])
            index4 = -1
            while(i<LENGTH):
                index3 = text[line].find('"""',index1+2)
                if index3!=-1 and skip_str!="":
                    skip_str,index4 = "",index3+3
                elif skip_str == "" and index1 != -1 and index4!=-1:
                    text[line] = text[line][index4:index3]
                else:
                    break
                i+=1
        elif skip_str=="" and index2!=-1:
            skip_str = "'''"
            edited_text+=text[line][:index2]
            i,LENGTH = 0,len(text[line])
            index4 = -1
            while(i<LENGTH):
                index3 = text[line].find("'''",index2+2)
                if index3!=-1 and skip_str!="":
                    skip_str,index4 = "",index3+3
                elif skip_str == "" and index2 != -1 and index4!=-1:
                    text[line] = text[line][index4:index3]
                else:
                    break
                i+=1
        elif skip_str=='"""' and index1!=-1:
            skip_str = ""
            text[line] = text[line][index1+3:]
        elif skip_str=="'''" and index2!=-1:
            skip_str = ""
            text[line] = text[line][index2+3:]

        if not skip_str:
            index = text[line].find("#")
            if text[line].strip().startswith('#'):
                pass
            elif index!=-1:
                # print(index,text[line].find('"'),text[line][::-1].find('"'))
                if index-1>=0 and text[line][index-1] == " ":
                    index-=1
                while(index>=0):
                    if text[line][index] == " ":
                        index-=1
                    else:
                        index+=1
                        break
                index_f,index_l = text[line].find('"'),text[line][::-1].find('"')
                if index_f!= -1 and index_f!=index_l and not index_l >= index >= index_f:
                    index_f,index_l = text[line].find("'"),text[line][::-1].find("'")
                    if index_f!= -1 and index_f!=index_l and not index_l >= index >= index_f:
                        edited_text+=text[line][0:index]+["\n",""][edited_text.endswith("\n")]
                else:
                    edited_text+=text[line][0:index]+["\n",""][edited_text.endswith("\n")]
                    
            else:
                edited_text+=text[line]+["\n",""][edited_text.endswith("\n")]
        line+=1
    # print(edited_text)

    # infile.truncate(0)

    # infile.write(edited_text)

with open(args.infile,"w") as outfile:
    outfile.write(edited_text)