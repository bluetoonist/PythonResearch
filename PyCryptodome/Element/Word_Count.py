def frequency_analysis(msg):
    fa = {}
    for c in msg:
        if c in fa:
            fa[c] += 1
        else:
            fa[c] = 1

    print(sorted(fa.items(), key=lambda x:x[1], reverse=True))

if __name__ == '__main__':
    msg = '214!@#!@$2142421!@#@!$!@5213213!@#@!3'
    frequency_analysis(msg)
