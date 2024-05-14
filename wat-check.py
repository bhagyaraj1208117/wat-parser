string_a="""

  (import "env" "getNumArguments" (func (;0;) (type 5)))

  (import "env" "getArgument" (func (;1;) (type 2)))

  (import "env" "bigIntAdd" (func (;2;) (type 6)))

  (import "env" "signalError" (func (;3;) (type 7)))

  (import "env" "int64getArgument" (func (;4;) (type 8)))

  (import "env" "bigIntNew" (func (;5;) (type 9)))

  (import "env" "bigIntGetUnsignedArgument" (func (;6;) (type 7)))

  (import "env" "getCaller" (func (;7;) (type 0)))

  (import "env" "bigIntStorageLoadUnsigned" (func (;8;) (type 1)))

  (import "env" "bigIntStorageStoreUnsigned" (func (;9;) (type 1)))

  (import "env" "bigIntGetCallValue" (func (;10;) (type 0)))

  (import "env" "bigIntCmp" (func (;11;) (type 2)))

  (import "env" "finish" (func (;12;) (type 7)))

  (import "env" "bigIntFinishUnsigned" (func (;13;) (type 0)))

  (import "env" "bigIntSetUnsignedBytes" (func (;14;) (type 6)))

  (import "env" "storageStore" (func (;15;) (type 10)))

  (import "env" "getBlockNonce" (func (;16;) (type 11)))

  (import "env" "int64storageStore" (func (;17;) (type 12)))

  (import "env" "int64storageLoad" (func (;18;) (type 13)))

  (import "env" "bigIntMul" (func (;19;) (type 6)))

  (import "env" "bigIntTDiv" (func (;20;) (type 6)))

  (import "env" "storageLoadLength" (func (;21;) (type 2)))

  (import "env" "getSCAddress" (func (;22;) (type 0)))

  (import "env" "bigIntGetExternalBalance" (func (;23;) (type 7)))

  (import "env" "storageLoad" (func (;24;) (type 1)))

  (import "env" "transferValue" (func (;25;) (type 10)))

  (import "env" "bigIntUnsignedByteLength" (func (;26;) (type 4)))

  (import "env" "bigIntGetUnsignedBytes" (func (;27;) (type 2)))

  (import "env" "asyncCall" (func (;28;) (type 3)))

  (import "env" "getArgumentLength" (func (;29;) (type 4)))

  (import "env" "writeLog" (func (;30;) (type 3)))

  (import "env" "bigIntSub" (func (;31;) (type 6)))"""
list_x=string_a.split() 
index=0
result=[]
for i in list_x:
    
       
    if i=='"env"':
        print("its working")   
        string_with_quotes = list_x[index+1]
        cleaned_string = string_with_quotes.replace('"', '').replace("'", '')
        print("iiiiiiiiiiiiiiiiiiiiiii",cleaned_string)
        result.append(cleaned_string)  
    index=index+1    
result.sort()
print(result)
