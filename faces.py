def convert (n):
    n=str (n)
    n=n.replace (":)", "🙂") .replace (":(", "🙁")
    return n

def main (n):
    return convert (n)

n=input ()
print (main (n))
