# -*- coding: utf-8 -*-
import csv, os, re, sys
import jyutping_edit
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


def jyutping_processing(inp_file, out_file):

    start = time.time()

    count = 0
    w = open(out_file, 'w')
    global cw
    total = len(open(inp_file, 'r').readlines())
    # bar = Bar('Processing', max=len(open(inp_file, 'r').readlines()))
    f = open(inp_file, 'r')
    myReader = csv.DictReader(f, delimiter='|')

    # fieldnames = myReader.fieldnames
    fieldnames = ['chinese', 'jyutping']
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
        jpinyin = jyutping_edit.get(name)

        jpinyin_out = ""
        for jname in jpinyin:
            try:
                jname = jname.replace(u'1', u'').replace(u'2', u'').replace(
                    u'3', u'').replace(u'4', u'').replace(u'5', u'').replace(
                        u'6', u'').replace(u'7',
                                           u'').replace(u'8', u'').replace(
                                               u'9', u'').replace(u'0', u'')
                jpinyin_out += jname + " "
            except:
                jout = jname[0].replace(u'1', u'').replace(u'2', u'').replace(
                    u'3', u'').replace(u'4', u'').replace(u'5', u'').replace(
                        u'6', u'').replace(u'7',
                                           u'').replace(u'8', u'').replace(
                                               u'9', u'').replace(u'0', u'')
                jpinyin_out += jout + " "
        row['jyutping'] = jpinyin_out
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
