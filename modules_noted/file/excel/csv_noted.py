# -*- coding: utf-8 -*-
# @Author: admin
# @Date:   2018-03-19 08:20:59
# @Last Modified by:   admin
# @Last Modified time: 2018-03-19 11:23:43
import csv, codecs, cStringIO

# 增加对中文字符的支持
class UTF8Recoder:
    """
    Iterator that reads an encoded stream and reencodes the input to UTF-8
    """
    def __init__(self, f, encoding):
        self.reader = codecs.getreader(encoding)(f)

    def __iter__(self):
        return self

    def next(self):
        return self.reader.next().encode("utf-8")

class UnicodeReader:
    """
    A CSV reader which will iterate over lines in the CSV file "f",
    which is encoded in the given encoding.
    """

    def __init__(self, f, dialect=csv.excel, encoding="utf-8", **kwds):
        f = UTF8Recoder(f, encoding)
        self.reader = csv.reader(f, dialect=dialect, **kwds)

    def next(self):
        row = self.reader.next()
        return [unicode(s, "utf-8") for s in row]

    def __iter__(self):
        return self

class UnicodeWriter:
    """
    A CSV writer which will write rows to CSV file "f",
    which is encoded in the given encoding.
    """

    def __init__(self, f, dialect=csv.excel, encoding="utf-8", **kwds):
        # Redirect output to a queue
        self.queue = cStringIO.StringIO()
        self.writer = csv.writer(self.queue, dialect=dialect, **kwds)
        self.stream = f
        self.encoder = codecs.getincrementalencoder(encoding)()

    def writerow(self, row):
        self.writer.writerow([s.encode("utf-8") for s in row])
        # Fetch UTF-8 output from the queue ...
        data = self.queue.getvalue()
        data = data.decode("utf-8")
        # ... and reencode it into the target encoding
        data = self.encoder.encode(data)
        # write to the target stream
        self.stream.write(data)
        # empty queue
        self.queue.truncate(0)

    def writerows(self, rows):
        for row in rows:
            self.writerow(row)




def reader_csv(filename):
	# 这个函数用来处理如何读取csv文件
	with open(filename,"rb") as csvfile:
		spamreader=csv.reader(csvfile,delimiter=" ",quotechar="|")
		for line in spamreader:
			print "-->".join(line)

def writen_csv(filename):
	# 这个函数用来处理如何将数据写入csv文件
	with open(filename,"wb") as w_csvfile:
		# spamwrite=csv.writer(w_csvfile,delimiter=",",quotechar="|",quoting=csv.QUOTE_MINIMAL)
		spamwrite=UnicodeWriter(w_csvfile,encoding="utf-8")
		spamwrite.writerow([u"球队",u"主教练",u"东西部分区"])
		spamwrite.writerow([u"勇士",u"史蒂夫科尔",u"西部分区"])
		spamwrite.writerow([u"马刺",u"波波维奇",u"西部分区"])
		spamwrite.writerow([u"火箭",u"德安东尼",u"西部分区"])


def writen_bask(f_obj):
	# 获取到传入的文本列表，然后写入csv文件中


if __name__ == '__main__':
	# reader_csv()
	# writen_csv("w_data.csv")
	# reader_csv("data.csv")
