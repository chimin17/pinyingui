# -*- coding: utf-8 -*-
import os, re, sys
import jyutping_edit
import pandas as pd
import time

# from progress.bar import Bar
import re, string


def progress(count, total, status=''):
    bar_len = 60
    filled_len = int(round(bar_len * count / float(total)))

    percents = round(100.0 * count / float(total), 1)
    bar = '=' * filled_len + '-' * (bar_len - filled_len)

    sys.stdout.write('progress[%s] %s%s ...%s\r' % (bar, percents, '%',
                                                    status))
    sys.stdout.flush()
    # return '[%s] %s%s ...%s\r' % (bar, percents, '%', status)


class Jyutping_Core:
    def __init__(self, input_name):
        self


def jyutping_processing(inp_file, out_file):

    start = time.time()

    count = 0
    df = pd.read_csv(inp_file, delimiter='|')
    inputdata = df.loc[:, ['chinese']].squeeze()
    total = len(inputdata)
    ouputdata = []

    for name in inputdata:

        progress(count, total)
        name = re.sub('[%s]' % re.escape(string.punctuation), '', name)

        newName = ''
        for ch in name:

            ch = ch.replace(u'1', u'一').replace(u'2', u'二').replace(
                u'3', u'三').replace(u'4', u'四').replace(u'5', u'五').replace(
                    u'6', u'六').replace(u'7',
                                        u'七').replace(u'8', u'八').replace(
                                            u'9', u'九').replace(u'0', u'零')
            ch = ch.replace(u'ㄟ', u'a').replace(u'ㄉ', u'de').replace(
                u'の', u'de').replace(u'ㄚ', u'a').replace(u'ㄠ', u'ao')

            newName += ch

        jpinyin = jyutping_edit.get(newName)
        jpinyin_out = ""
        jcount = -1
        jerror = ""

        for jname in jpinyin:
            jcount = jcount + 1
            try:
                if isinstance(jname, str):
                    jname = jname.replace(u'1', u'').replace(
                        u'2', u'').replace(u'3', u'').replace(
                            u'4', u'').replace(u'5', u'').replace(
                                u'6', u'').replace(u'7', u'').replace(
                                    u'8', u'').replace(u'9', u'').replace(
                                        u'0', u'')
                    jpinyin_out += jname + " "
                else:
                    jout = jname[0].replace(u'1', u'').replace(
                        u'2', u'').replace(u'3', u'').replace(
                            u'4', u'').replace(u'5', u'').replace(
                                u'6', u'').replace(u'7', u'').replace(
                                    u'8', u'').replace(u'9', u'').replace(
                                        u'0', u'')
                    jpinyin_out += jout + " "

            except:
                #英文
                if newName[jcount].isalpha():
                    jpinyin_out += newName[jcount] + "  "
                else:
                    jerror += name[jcount] + " "
        # 過濾英文空格
        r = re.compile(u'[A-Za-z]{1}\s{2}', re.U)
        findjpinyin_out = r.findall(jpinyin_out)  # utf-8

        if len(findjpinyin_out) > 0:
            newfindjpinyin_out = "".join(findjpinyin_out)

            jpinyin_out = jpinyin_out.replace(
                newfindjpinyin_out,
                newfindjpinyin_out.replace('  ', '') + " ")

        log = ""
        if jerror.strip() != "":
            log = "error in:" + jerror
        ouputdata.append({
            "chinese":
            name,
            "jyutping":
            jpinyin_out.lower().replace("  ", " ").strip(),
            "log":
            log
        })
        count = count + 1
        # if count > 5000:
        #     break
    # if done!
    out_df = pd.DataFrame(ouputdata)
    out_df.reindex(columns=["chinese", "jyutping", "log"]).to_csv(
        out_file, index=False)
    progress(total, total, "Done!")

    # bar.finish()
    end = time.time()
    elapsed = end - start
    return "Time taken: ", '%.3f' % elapsed, "seconds."
