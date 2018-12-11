import re
from w2n import text2int
import collections
from datetime import datetime

dic = {"oh":0, "zero":0, "one":1, "two":2, "three":3, "four":4, "five":5, "six":6, "seven":7, "eight":8, "nine":9, "ten":10, "eleven":11, "twelve":12, "thirteen"
        :13, "fourteen":14, "fifteen":15, "sixteen":16, "seventeen":17, "eighteen":18, "nineteen":19 , "first":1, "second":2, "third":3, "fif":5, "eigh":8}

date = {"jan":1, "january":1, "feb":2, "february":2, "march":3, "mar":3, "april":4, "apr":4, "may":5, "june":6, "jun":6, "july":7, "jul":6 ,"aug":8, "august":8, "sep":9, "september":9, "oct":
        10, "october":10, "nov":11, "november":11, "dec":12, "december":12}

def word2number(line):
        sent = line.split()
        joint_num_flag, joint_num_flag1, okflag = True, True, True
        flag_date = [0 for word in sent if word in date]
        fd = True
        dic_word = [0 for word in sent if word in dic]
        duplicate = [item for item, count in collections.Counter(sent).items() if count > 1]
        if all(flag_date) is False:
            for i in range(len(sent)):
                try:
                    if sent[i] in date and fd:
                        month = date[sent[i]]
                        month_index = i
                        fd = False
                        date_list = sent[i+1:i+8]
                        for i in range(1, len(date_list)):
                            
                            if date_list[i] == "thousand":
                                year_list = text2int(" ".join(date_list[i-1:]))
                                year_index = i-1
                                day = text2int(" ".join(date_list[month_index:year_index]))
                                break

                            elif date_list[i] == "hundred":
                                year_list = text2int(" ".join(date_list[i-1:]))
                                year_index = i-1
                                day = text2int(" ".join(date_list[month_index:year_index]))
                                break
                        else:
                                year_list = dic[date_list[-3]]
                                year_list = [str(year_list)] + [str(text2int(" ".join(date_list[-2:])))]
                                year_list = "".join(year_list)
                                year_index = -3
                                day = text2int(" ".join(date_list[month_index:year_index]))
                except IndexError:
                        print("index not found")
                dat = str(month) + "/" + str(day) + "/" + str(year_list)
                return dat

        elif all(dic_word) is False and len(dic_word) == len(sent):
            for word in sent:
                try:
                    if word in dic:
                        line = re.sub(r'\b%s\b' %word, str(dic[word]), line)
                except KeyError:
                    print("element not found")
            okflag = False
        else:
            line = text2int(line)

        if okflag is False:
            line = re.sub('(?<=\d)\s+(?=\d)', '', line)
        return line
