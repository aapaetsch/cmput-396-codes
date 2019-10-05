
import math


#returns a list of the first 10 found digits of the lcg 
def lcg(a, b, m, r0):
    
    r = []
    for i in range(10):
        Rn = ((a*r0)+b)%m 
        r.append(Rn)
        r0 = Rn
    return r


# --- Below is for Testing purposes---
def main():
    a = 22695477
    b = 1
    m = 2**32
    r0 = 42
    
    output1 = lcg(a, b, m, r0)
    print(output1)
    if output1 == [953210035, 3724055312, 1961185873, 1409857734, 3384186111,
            3302525644, 1389814845, 444192418, 2979187595, 2537979336]:
        print("Outputs match")
    else:
        print("Outputs do not match")


if __name__ == "__main__":
    main()
