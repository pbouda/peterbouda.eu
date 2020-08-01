Title: Major progress in AI!
Date: 2020-08-01 09:15
Tags: AI

```
  File "/data/home/pbouda/yolov3/utils/utils.py", line 45, in load_classes
    names = f.read().split('\n')
  File "/data/anaconda/envs/py35/lib/python3.5/encodings/ascii.py", line 26, in decode
    return codecs.ascii_decode(input, self.errors)[0]
UnicodeDecodeError: 'ascii' codec can't decode byte 0xc4 in position 157: ordinal not in range(128)
```

Well, it can recognize objects in videos but no non-ASCII characters in object
names. We'll have to wait until computers get faster and better ;)
