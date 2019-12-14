def get_data():
    try:
     a=int(input("eneter value for a"))
     b=a-int(input("enter value for b"))
     return a,b
    except ValueError as e:
     print(e)
     return get_data()
def div(a,b):
 try:
    c=a/b
    return c
 except ZeroDivisionError as e:
     print(e)
 finally:
  print("finaly")
def main():
    try:
        a,b=get_data()
        c=div(a,b)
        print(c)
    except ZeroDivisionError as e:
        print(e)
        main()
