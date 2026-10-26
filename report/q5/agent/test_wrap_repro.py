import importlib.util, sys
spec = importlib.util.spec_from_file_location("tw", sys.argv[1])
tw = importlib.util.module_from_spec(spec); spec.loader.exec_module(tw)
import textwrap as std
cases = [("aaa bbb",7),("aaa bbb",6),("hello world",11),("a b c d e",3),("The quick brown fox jumps over the lazy dog",10),("abcdefghij",5),("  x y",4)]
ok=True
for t,w in cases:
    a=tw.wrap(t,width=w); b=std.wrap(t,width=w)
    print(repr(t),w,a,"OK" if a==b else "MISMATCH std=%r"%b); ok&=a==b
print("ALL PASS" if ok else "FAIL")
