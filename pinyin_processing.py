# -*- coding: utf-8 -*-
import csv, os, re, sys
from pypinyin import pinyin, lazy_pinyin, Style
import time

# from progress.bar import Bar


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
    w = open(out_file, 'w')
    global cw
    total = len(open(inp_file, 'r').readlines())
    # bar = Bar('Processing', max=len(open(inp_file, 'r').readlines()))
    f = open(inp_file, 'r')
    myReader = csv.DictReader(f, delimiter='|')

    # fieldnames = myReader.fieldnames
    fieldnames = ['chinese', 'pinyin']
    cw = csv.DictWriter(
        w, delimiter='|', lineterminator='\n', fieldnames=fieldnames)

    cw.writeheader()
    for row in myReader:

        progress(count, total)

        name = row['chinese'].decode("utf-8")
        newName = ''
        for ch in name:

            ch = ch.replace(u'ㄟ', u'a').replace(u'ㄉ', u'de').replace(
                u'の', u'de').replace(u'ㄚ', 'a').replace(u'ㄠ', u'ao')
            newName += ch
        cpinyin = lazy_pinyin(newName, strict=False)
        cpinyin_out = ""
        for cname in cpinyin:
            try:
                cpinyin_out += cname + " "
            except:
                cpinyin_out += cname[0] + " "
        row['pinyin'] = cpinyin_out
        cw.writerow(row)
        count = count + 1
        # if count > 5000:
        #     break
    # if done!
    progress(total, total, "Done!")

    w.close()
    f.close()
    # bar.finish()
    end = time.time()
    elapsed = end - start
    return "Time taken: ", '%.3f' % elapsed, "seconds."