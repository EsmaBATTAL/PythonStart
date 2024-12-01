def NULL_not_found(object: any) -> int:
   try :
    print(f"Object:{object}, Type:{type(object)}")
    return 0
   except Exception as e:
     print(f"Error:{e}")
     return 1
