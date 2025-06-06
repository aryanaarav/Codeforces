import os
import sys
from io import BytesIO, IOBase


def main():
    pass


# region fastio

BUFSIZE = 8192


class FastIO(IOBase):
    newlines = 0

    def __init__(self, file):
        self._file = file
        self._fd = file.fileno()
        self.buffer = BytesIO()
        self.writable = "x" in file.mode or "r" not in file.mode
        self.write = self.buffer.write if self.writable else None

    def read(self):
        while True:
            b = os.read(self._fd, max(os.fstat(self._fd).st_size, BUFSIZE))
            if not b:
                break
            ptr = self.buffer.tell()
            self.buffer.seek(0, 2), self.buffer.write(b), self.buffer.seek(ptr)
        self.newlines = 0
        return self.buffer.read()

    def readline(self):
        while self.newlines == 0:
            b = os.read(self._fd, max(os.fstat(self._fd).st_size, BUFSIZE))
            self.newlines = b.count(b"\n") + (not b)
            ptr = self.buffer.tell()
            self.buffer.seek(0, 2), self.buffer.write(b), self.buffer.seek(ptr)
        self.newlines -= 1
        return self.buffer.readline()

    def flush(self):
        if self.writable:
            os.write(self._fd, self.buffer.getvalue())
            self.buffer.truncate(0), self.buffer.seek(0)


class IOWrapper(IOBase):
    def __init__(self, file):
        self.buffer = FastIO(file)
        self.flush = self.buffer.flush
        self.writable = self.buffer.writable
        self.write = lambda s: self.buffer.write(s.encode("ascii"))
        self.read = lambda: self.buffer.read().decode("ascii")
        self.readline = lambda: self.buffer.readline().decode("ascii")


sys.stdin, sys.stdout = IOWrapper(sys.stdin), IOWrapper(sys.stdout)
input = lambda: sys.stdin.readline().rstrip("\r\n")

# endregion

if __name__ == "__main__":
    main()




import sys
sys.stdout = open('C/output.txt', 'w')
sys.stdin = open('C/input.txt', 'r')

t = int(input())
while t:
    n, m, k = map(int,input().split())
    l1 = set(list(map(int, input().split()[:n])))
    l2 = set(list(map(int, input().split()[:m])))
    c1 = 0
    c2 = 0
    c = 0
    for i in range(1,k+1):
        if i in l1  and i not in l2:
            c1 += 1
        elif i in l2 and i not in l1:
            c2 += 1
        elif i in l1 and i in l2:
            c += 1
    if (c1 == c2 and k-(c1+c2) == c):
        print("YES")
    elif abs(c1-c2)!=0 and abs(c2-c1) == c:
        print("YES")
    elif c1 > k//2 or c2 > k//2:
        print("NO")
    else:
        print("NO")
    t -= 1