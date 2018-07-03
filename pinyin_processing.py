# -*- coding: utf-8 -*-
# -*- coding: py36 -*-
import os, re, sys
import pandas as pd
from pypinyin import pinyin, lazy_pinyin, Style, load_phrases_dict, load_single_dict
import time
load_phrases_dict({u'銀行': [[u'yin'], [u'hang']]})
load_phrases_dict({u'車行': [[u'che'], [u'hang']]})
load_phrases_dict({u'總行': [[u'zong'], [u'hang']]})
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


def pinyin_processing(inp_file, out_file):

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
        cpinyin = lazy_pinyin(newName, strict=False)
        cpinyin_out = ""
        for cname in cpinyin:
            try:
                cpinyin_out += cname + " "
            except:
                cpinyin_out += cname[0] + " "
        ouputdata.append({"name": name, "pinyin": cpinyin_out})
        count = count + 1
        # if count > 5000:
        #     break
    # if done!
    progress(total, total, "Done!")

    out_df = pd.DataFrame(ouputdata)

    #out_df.drop(['index'], axis=1)
    out_df.to_csv(out_file, index=False)
    # bar.finish()
    end = time.time()
    elapsed = end - start
    return "Time taken: ", '%.3f' % elapsed, "seconds."
