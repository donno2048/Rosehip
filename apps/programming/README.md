to write code in this program just open the language you need,

to execute the code you wrote just press the ENTER key,

since ENTER is used to execute the code use | to separate lines.

# examples:


## bat:

```bat
@echo hi
@echo off
@echo hi again
@echo on
@echo hi there
```

## c#:

```csharp
using System;

namespace HelloWorld
{
  class Program
  {
    static void Main(string[] args)
    {
      Console.WriteLine("Hi");    
    }
  }
}
```

## html:
```html
<html>
  <body>
    <h1> hi there </h1>
  </body>
</html>
```

## javascript:
```js
document.write("Hello World!")
```

## powerhell:

```powershell
$l1=@(1,2,3)+@(4,5,6)
$l2=$l1 | Measure-Object
$l=$l1,$l2
Write-Output $l
```

## python:

```python3
for i in range(42):print('42\n')
```

## visual basic script:

```vbs
MsgBox "hi you"
```
