import re
from w2n import text2int
import collections
dic = {"oh":0, "zero":0, "one":1, "two":2, "three":3, "four":4, "five":5, "six":6, "seven":7, "eight":8, "nine":9, "ten":10, "eleven":11, "twelve":12, "thirteen"
        :13, "fourteen":14, "fifteen":15, "sixteen":16, "seventeen":17, "eighteen":18, "nineteen":19 , "first":1, "second":2, "third":3, "fif":5, "eigh":8}

date = {"jan":1, "january":1, "feb":2, "february":2, "march":3, "mar":3, "april":4, "apr":4, "may":5, "june":6, "jun":6, "july":7, "jul":6 ,"aug":8, "august":8, "sep":9, "september":9, "oct":
        10, "october":10, "nov":11, "november":11, "dec":12, "december":12}

joint_num = {"twenty":20, "thirty":30, "forty":40, "fifty":50, "sixty":60, "seventy":70, "eighty":80, "ninety":90, "hundred":100, "thousand":1000}

one_digit = {"one":1, "two":2, "three":3, "four":4, "five":5, "six":6, "seven":7, "eight":8, "nine":9}

def word2number(line):
        sent = line.split()
        # print(text2int(line))
        joint_num_flag, joint_num_flag1, okflag = True, True, True
        flag_date = [0 for word in sent if word in date]
        # flag_plain_num = [0 for word in sent if word not in joint_num]
        dic_word = [0 for word in sent if word in dic]
        duplicate = [item for item, count in collections.Counter(sent).items() if count > 1]
        print(flag_date)
        print(dic_word)
        if all(flag_date) is False:
            for i in range(len(sent)):
                try:
                    if sent[i] in date:
                        print(1)
                        line = re.sub(r'\b%s\b' %sent[i], str(date[sent[i]]), line)

                    elif sent[i] in dic and joint_num_flag:
                        print(2)
                        line = re.sub(r'\b%s\b' %sent[i], str(dic[sent[i]]), line)

                    elif sent[i] in joint_num and (sent[i+1] in one_digit):
                        print(3)
                        line = re.sub(r'\b%s\b' %sent[i], (str(joint_num[sent[i]]).rstrip("0")).strip(), line)
                        joint_num_flag = False

                    elif sent[i] in joint_num and (sent[i+1] not in one_digit):
                        print(3)
                        line = re.sub(r'\b%s\b' %sent[i], (str(joint_num[sent[i]])).strip(), line)
                        joint_num_flag1 = False

                    elif sent[i] in dic and not joint_num_flag:
                        line = re.sub(r'\b%s\b' %sent[i], str(dic[sent[i]]), line)
                        try:
                            if duplicate[0]:
                                line = re.sub(r'\b%s\b' %dic[duplicate[0]], str(dic[sent[i]]), line)
                        except IndexError:
                            print("no index found")

                    elif sent[i] in dic and not joint_num_flag1:
                        line = re.sub(r'\b%s\b' %sent[i], dic[sent[i]], line)
                        try:
                            if duplicate[0]:
                                line = re.sub(r'\b%s\b' %dic[duplicate[0]], str(va), line)
                        except IndexError:
                            print("no index found")
                except KeyError:
                    print("elment not found")
        elif all(dic_word) is False and len(dic_word) == len(sent):
            for word in sent:
                try:
                    if word in dic:
                        line = re.sub(r'\b%s\b' %word, str(dic[word]), line)
                except KeyError:
                    print("elment not found")
            okflag = False
        else:
            line = text2int(line)
        if all(flag_date) is False:
            line = re.sub('(?<=\d) (?=\d)', '/', line)
            line = re.sub('(?<=\d)\s+(?=\d)', '', line)
            a = re.findall(r'\b\d+\b', line)
            print(a)
            if len(a) == 4:
                sub = a[0] + "/" + a[1] + "/" + "".join(a[2:])
                st = a[0] + "/" + a[1] + "/" + a[2] + "/" + a[3]
                line = re.sub(st, sub, line)
            else:
                sub = a[0] + "/" + a[1] + "/" +"".join(a[2:])
                st = a[0] + "/" + a[1] + "/" + a[2] + "/" + a[3] +"/" + a[4]
                line = re.sub(st, sub, line)
        if okflag is False:
            line = re.sub('(?<=\d)\s+(?=\d)', '', line)

        #     line = re.sub(r'(\d)\s+(d)\s+(\d)\s+(\d)\s+', r'\1///\2\3\4', line)
            #line = re.sub(r'(\d)\s(\d)\s(\d)\s(\d)\s(\d)\s(\d)', r'\1\2\3\4\5\6', line)
        return line
