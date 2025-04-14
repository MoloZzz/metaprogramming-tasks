## 1. Використовуючи засоби мови python реалiзувати:
1. Клас City, який мiстить наступнi атрибути: назва, регiон, населення, перелiк адмiнiстративних районiв.
Реалiзувати управлiння атрибутами класу City за допомогою get-set-delete-дескриптора.

2. Декоратор attr_change_logger, який вiдслiдковує змiни назви, кiлькостi населення, перелiку адмiнiстра-
тивних районiв об’єктiв екземплярiв класу City та здiйснює логування цих змiн у журнальнi текстовi
файли (для кожного атрибуту окремий файл). 

3. Метаклас FixNumCreator, який керує створенням об’єктiв екземплярiв класу City дозволяючи створен-
ня фiксованої кiлькостi об’єктiв та записує iнформацiю про кожен новостворений об’єкт у журнальний
текстовий файл. 

## 2. Функція для написання
1) На вхід – число N, на вихід – словник, що визначає розклад числа  N! на множники, наприклад {2:10,3:7,5:3}
2) На вхід – словник, що визначає розклад числа N на множники, наприклад {2:10,3:7,5:3}, на вихід – саме довге число у формі рядка
3) На вхід – масив чисел, на вихід – його максимальна за довжиною зростаюча підпослідовність
4) На вхід – текст та число N, на вихід – словник (dict) з N найбільш вживаних слів у ньому разом з їх кількістю
5) На вхід – матриця, на вихід – обернена матриця.
6) На вхід – функція f(x) та межі інтегрування x0,x1, на вихід – її визначений інтеграл x0x1f(x)dx.
7) На вхід – список, що складається з трійок чисел що позначають значення і координати ненульових елементів матриці. На вихід – сама матриця.

Виконаю 2 з 7 вище описаних задач. Частина на C, Частина на Python

## first-method
Функція (на С++): на вхід – масив чисел, на вихід – його максимальна за довжиною зростаюча підпослідовність. 
Зв'язок з Python через pybind11
```
pip install pybind11
```

```
$ python setup.py build_ext --inplace
running build_ext
building 'lis' extension
"C:\Program Files\Microsoft Visual Studio\2022\Community\VC\Tools\MSVC\14.40.33807\bin\HostX86\x64\cl.exe" /c /nologo /O2 /W3 /GL /DNDEBUG /MD -IC:\Users\megao\AppData\Local\Packages\PythonSoftwareFoundation.Python.3.11_qbz5n2kfra8p0\LocalCache\local-packages\Python311\site-packages\pybind11\include "-IC:\Program Files\WindowsApps\PythonSoftwareFoundation.Python.3.11_3.11.2544.0_x64__qbz5n2kfra8p0\include" "-IC:\Program Files\WindowsApps\PythonSoftwareFoundation.Python.3.11_3.11.2544.0_x64__qbz5n2kfra8p0\Include" "-IC:\Program Files\Microsoft Visual Studio\2022\Community\VC\Tools\MSVC\14.40.33807\include" "-IC:\Program Files\Microsoft Visual Studio\2022\Community\VC\Tools\MSVC\14.40.33807\ATLMFC\include" "-IC:\Program Files\Microsoft Visual Studio\2022\Community\VC\Auxiliary\VS\include" "-IC:\Program Files (x86)\Windows Kits\10\include\10.0.26100.0\ucrt" "-IC:\Program Files (x86)\Windows Kits\10\\include\10.0.26100.0\\um" "-IC:\Program Files (x86)\Windows Kits\10\\include\10.0.26100.0\\shared" "-IC:\Program Files (x86)\Windows Kits\10\\include\10.0.26100.0\\winrt" "-IC:\Program Files (x86)\Windows Kits\10\\include\10.0.26100.0\\cppwinrt" /EHsc /Tplis.cpp /Fobuild\temp.win-amd64-cpython-311\Release\lis.obj -std=c++11
cl : Command line warning D9002 : ignoring unknown option '-std=c++11'
lis.cpp
lis.cpp(17): warning C4267: '=': conversion from 'size_t' to '_Ty', possible loss of data
        with
        [
            _Ty=int
        ]
lis.cpp(22): warning C4267: '=': conversion from 'size_t' to 'int', possible loss of data
creating C:\Users\megao\Desktop\Projects\metaprogramming-tasks\python-interacts-with-c\first-method\build\lib.win-amd64-cpython-311
"C:\Program Files\Microsoft Visual Studio\2022\Community\VC\Tools\MSVC\14.40.33807\bin\HostX86\x64\link.exe" /nologo /INCREMENTAL:NO /LTCG /DLL /MANIFEST:EMBED,ID=2 /MANIFESTUAC:NO "/LIBPATH:C:\Program Files\WindowsApps\PythonSoftwareFoundation.Python.3.11_3.11.2544.0_x64__qbz5n2kfra8p0\libs" "/LIBPATH:C:\Program Files\WindowsApps\PythonSoftwareFoundation.Python.3.11_3.11.2544.0_x64__qbz5n2kfra8p0" "/LIBPATH:C:\Program Files\WindowsApps\PythonSoftwareFoundation.Python.3.11_3.11.2544.0_x64__qbz5n2kfra8p0\PCbuild\amd64" "/LIBPATH:C:\Program Files\Microsoft Visual Studio\2022\Community\VC\Tools\MSVC\14.40.33807\ATLMFC\lib\x64" "/LIBPATH:C:\Program Files\Microsoft Visual Studio\2022\Community\VC\Tools\MSVC\14.40.33807\lib\x64" "/LIBPATH:C:\Program Files (x86)\Windows Kits\10\lib\10.0.26100.0\ucrt\x64" "/LIBPATH:C:\Program Files (x86)\Windows Kits\10\\lib\10.0.26100.0\\um\x64" /EXPORT:PyInit_lis build\temp.win-amd64-cpython-311\Release\lis.obj /OUT:build\lib.win-amd64-cpython-311\lis.cp311-win_amd64.pyd /IMPLIB:build\temp.win-amd64-cpython-311\Release\lis.cp311-win_amd64.lib
   Creating library build\temp.win-amd64-cpython-311\Release\lis.cp311-win_amd64.lib and object build\temp.win-amd64-cpython-311\Release\lis.cp311-win_amd64.exp
Generating code
Finished generating code
copying build\lib.win-amd64-cpython-311\lis.cp311-win_amd64.pyd -> 
```
### Output
```
$ python test.py
Input array: [10, 22, 9, 33, 21, 50, 41, 60, 80]
Longest increasing subsequence: [10, 22, 33, 50, 60, 80]
```

## second-method
```
Функція на С: на вхід – текст та число N, на вихід – словник (dict) з N найбільш вживаних слів у ньому разом з їх кількістю.
Зв'язок через Cython
```
```
pip install cython
```
```
second-method/
│
├── wordfreq_core.c           ← C-файл з логікою (можна згенерувати окремо)
├── wordfreq_core.h           ← Заголовочний файл з деклараціями
├── wordfreq.pyx              ← Python/Cython-файл, який викликає функції C
├── setup.py                  ← Скрипт для компіляції Cython
└── example.py                ← Python-скрипт для запуску та перевірки
```
```
$ python setup.py build_ext --inplace
Compiling wordfreq.pyx because it changed.
[1/1] Cythonizing wordfreq.pyx
running build_ext
building 'wordfreq' extension
creating build
creating build\temp.win-amd64-cpython-311
creating build\temp.win-amd64-cpython-311\Release
"C:\Program Files\Microsoft Visual Studio\2022\Community\VC\Tools\MSVC\14.40.33807\bin\HostX86\x64\cl.exe" /c /nologo /O2 /W3 /GL /DNDEBUG /MD "-IC:\Program Files\WindowsApps\PythonSoftwareFoundation.Python.3.11_3.11.2544.0_x64__qbz5n2kfra8p0\include" "-IC:\Program Files\WindowsApps\PythonSoftwareFoundation.Python.3.11_3.11.2544.0_x64__qbz5n2kfra8p0\Include" "-IC:\Program Files\Microsoft Visual Studio\2022\Community\VC\Tools\MSVC\14.40.33807\include" "-IC:\Program Files\Microsoft Visual Studio\2022\Community\VC\Tools\MSVC\14.40.33807\ATLMFC\include" "-IC:\Program Files\Microsoft Visual Studio\2022\Community\VC\Auxiliary\VS\include" "-IC:\Program Files (x86)\Windows Kits\10\include\10.0.26100.0\ucrt" "-IC:\Program Files (x86)\Windows Kits\10\\include\10.0.26100.0\\um" "-IC:\Program Files (x86)\Windows Kits\10\\include\10.0.26100.0\\shared" "-IC:\Program Files (x86)\Windows Kits\10\\include\10.0.26100.0\\winrt" "-IC:\Program Files (x86)\Windows Kits\10\\include\10.0.26100.0\\cppwinrt" /Tcwordfreq.c /Fobuild\temp.win-amd64-cpython-311\Release\wordfreq.obj
wordfreq.c
"C:\Program Files\Microsoft Visual Studio\2022\Community\VC\Tools\MSVC\14.40.33807\bin\HostX86\x64\cl.exe" /c /nologo /O2 /W3 /GL /DNDEBUG /MD "-IC:\Program Files\WindowsApps\PythonSoftwareFoundation.Python.3.11_3.11.2544.0_x64__qbz5n2kfra8p0\include" "-IC:\Program Files\WindowsApps\PythonSoftwareFoundation.Python.3.11_3.11.2544.0_x64__qbz5n2kfra8p0\Include" "-IC:\Program Files\Microsoft Visual Studio\2022\Community\VC\Tools\MSVC\14.40.33807\include" "-IC:\Program Files\Microsoft Visual Studio\2022\Community\VC\Tools\MSVC\14.40.33807\ATLMFC\include" "-IC:\Program Files\Microsoft Visual Studio\2022\Community\VC\Auxiliary\VS\include" "-IC:\Program Files (x86)\Windows Kits\10\include\10.0.26100.0\ucrt" "-IC:\Program Files (x86)\Windows Kits\10\\include\10.0.26100.0\\um" "-IC:\Program Files (x86)\Windows Kits\10\\include\10.0.26100.0\\shared" "-IC:\Program Files (x86)\Windows Kits\10\\include\10.0.26100.0\\winrt" "-IC:\Program Files (x86)\Windows Kits\10\\include\10.0.26100.0\\cppwinrt" /Tcwordfreq_core.c /Fobuild\temp.win-amd64-cpython-311\Release\wordfreq_core.obj
wordfreq_core.c
creating C:\Users\megao\Desktop\Projects\metaprogramming-tasks\python-interacts-with-c\second-method1\build\lib.win-amd64-cpython-311
"C:\Program Files\Microsoft Visual Studio\2022\Community\VC\Tools\MSVC\14.40.33807\bin\HostX86\x64\link.exe" /nologo /INCREMENTAL:NO /LTCG /DLL /MANIFEST:EMBED,ID=2 /MANIFESTUAC:NO "/LIBPATH:C:\Program Files\WindowsApps\PythonSoftwareFoundation.Python.3.11_3.11.2544.0_x64__qbz5n2kfra8p0\libs" "/LIBPATH:C:\Program Files\WindowsApps\PythonSoftwareFoundation.Python.3.11_3.11.2544.0_x64__qbz5n2kfra8p0" "/LIBPATH:C:\Program Files\WindowsApps\PythonSoftwareFoundation.Python.3.11_3.11.2544.0_x64__qbz5n2kfra8p0\PCbuild\amd64" "/LIBPATH:C:\Program Files\Microsoft Visual Studio\2022\Community\VC\Tools\MSVC\14.40.33807\ATLMFC\lib\x64" "/LIBPATH:C:\Program Files\Microsoft Visual Studio\2022\Community\VC\Tools\MSVC\14.40.33807\lib\x64" "/LIBPATH:C:\Program Files (x86)\Windows Kits\10\lib\10.0.26100.0\ucrt\x64" "/LIBPATH:C:\Program Files (x86)\Windows Kits\10\\lib\10.0.26100.0\\um\x64" /EXPORT:PyInit_wordfreq build\temp.win-amd64-cpython-311\Release\wordfreq.obj build\temp.win-amd64-cpython-311\Release\wordfreq_core.obj /OUT:build\lib.win-amd64-cpython-311\wordfreq.cp311-win_amd64.pyd /IMPLIB:build\temp.win-amd64-cpython-311\Release\wordfreq.cp311-win_amd64.lib
   Creating library build\temp.win-amd64-cpython-311\Release\wordfreq.cp311-win_amd64.lib and object build\temp.win-amd64-cpython-311\Release\worordfreq.cp311-win_amd64.exp
Generating code
Finished generating code
copying build\lib.win-amd64-cpython-311\wordfreq.cp311-win_amd64.pyd ->
```
```
$ python example.py
Input text: This is a sample text. This text contains some words.
Some words are repeated in this sample text!
Top 3 frequent words: {'text': 3, 'this': 3, 'sample': 2}
```
```
$ python example.py
Input text: This is a sample text. This text contains some words.
Some words are repeated in this sample text!
Some more text to test the word frequency.
This is a test text to check the word frequency.
Top 10 frequent words: {'text': 5, 'this': 4, 'some': 3, 'a': 2, 'frequency': 2, 'is': 2, 'sample': 2, 'test': 2, 'the': 2, 'to': 2}
```

## third-task
```
Функція: На вхід – матриця, на вихід – обернена матриця.
Зв'язок: CFFI 
```
```
pip install cffi
```
```
$ python build_matrix_inverse.py
generating .\_matrix_inverse.c
the current directory is 'C:\\Users\\megao\\Desktop\\Projects\\metaprogramming-tasks\\python-interacts-with-c\\third-method'
running build_ext
building '_matrix_inverse' extension
creating Release
"C:\Program Files\Microsoft Visual Studio\2022\Community\VC\Tools\MSVC\14.40.33807\bin\HostX86\x64\cl.exe" /c /nologo /O2 /W3 /GL /DNDEBUG /MD -IC:\Users\megao\Desktop\Projects\metaprogramming-tasks\python-interacts-with-c\third-method "-IC:\Program Files\WindowsApps\PythonSoftwareFoundation.Python.3.11_3.11.2544.0_x64__qbz5n2kfra8p0\include" "-IC:\Program Files\WindowsApps\PythonSoftwareFoundation.Python.3.11_3.11.2544.0_x64__qbz5n2kfra8p0\Include" "-IC:\Program Files\Microsoft Visual Studio\2022\Community\VC\Tools\MSVC\14.40.33807\include" "-IC:\Program Files\Microsoft Visual Studio\2022\Community\VC\Tools\MSVC\14.40.33807\ATLMFC\include" "-IC:\Program Files\Microsoft Visual Studio\2022\Community\VC\Auxiliary\VS\include" "-IC:\Program Files (x86)\Windows Kits\10\include\10.0.26100.0\ucrt" "-IC:\Program Files (x86)\Windows Kits\10\\include\10.0.26100.0\\um" "-IC:\Program Files (x86)\Windows Kits\10\\include\10.0.26100.0\\shared" "-IC:\Program Files (x86)\Windows Kits\10\\include\10.0.26100.0\\winrt" "-IC:\Program Files (x86)\Windows Kits\10\\include\10.0.26100.0\\cppwinrt" /Tc_matrix_inverse.c /Fo.\Release\_matrix_inverse.obj
_matrix_inverse.c
_matrix_inverse.c(595): warning C4013: 'allocate_matrix' undefined; assuming extern returning int
_matrix_inverse.c(595): warning C4047: 'return': 'double *' differs in levels of indirection from 'int'
_matrix_inverse.c(611): warning C4047: '=': 'double *' differs in levels of indirection from 'int'
_matrix_inverse.c(625): warning C4013: 'free_matrix' undefined; assuming extern returning int
_matrix_inverse.c(661): warning C4013: 'inverse_matrix' undefined; assuming extern returning int
"C:\Program Files\Microsoft Visual Studio\2022\Community\VC\Tools\MSVC\14.40.33807\bin\HostX86\x64\cl.exe" /c /nologo /O2 /W3 /GL /DNDEBUG /MD -IC:\Users\megao\Desktop\Projects\metaprogramming-tasks\python-interacts-with-c\third-method "-IC:\Program Files\WindowsApps\PythonSoftwareFoundation.Python.3.11_3.11.2544.0_x64__qbz5n2kfra8p0\include" "-IC:\Program Files\WindowsApps\PythonSoftwareFoundation.Python.3.11_3.11.2544.0_x64__qbz5n2kfra8p0\Include" "-IC:\Program Files\Microsoft Visual Studio\2022\Community\VC\Tools\MSVC\14.40.33807\include" "-IC:\Program Files\Microsoft Visual Studio\2022\Community\VC\Tools\MSVC\14.40.33807\ATLMFC\include" "-IC:\Program Files\Microsoft Visual Studio\2022\Community\VC\Auxiliary\VS\include" "-IC:\Program Files (x86)\Windows Kits\10\include\10.0.26100.0\ucrt" "-IC:\Program Files (x86)\Windows Kits\10\\include\10.0.26100.0\\um" "-IC:\Program Files (x86)\Windows Kits\10\\include\10.0.26100.0\\shared" "-IC:\Program Files (x86)\Windows Kits\10\\include\10.0.26100.0\\winrt" "-IC:\Program Files (x86)\Windows Kits\10\\include\10.0.26100.0\\cppwinrt" /Tcmatrix_inverse.c /Fo.\Release\matrix_inverse.obj
matrix_inverse.c
"C:\Program Files\Microsoft Visual Studio\2022\Community\VC\Tools\MSVC\14.40.33807\bin\HostX86\x64\link.exe" /nologo /INCREMENTAL:NO /LTCG /DLL /MANIFEST:EMBED,ID=2 /MANIFESTUAC:NO "/LIBPATH:C:\Program Files\WindowsApps\PythonSoftwareFoundation.Python.3.11_3.11.2544.0_x64__qbz5n2kfra8p0\libs" "/LIBPATH:C:\Program Files\WindowsApps\PythonSoftwareFoundation.Python.3.11_3.11.2544.0_x64__qbz5n2kfra8p0" "/LIBPATH:C:\Program Files\WindowsApps\PythonSoftwareFoundation.Python.3.11_3.11.2544.0_x64__qbz5n2kfra8p0\PCbuild\amd64" "/LIBPATH:C:\Program Files\Microsoft Visual Studio\2022\Community\VC\Tools\MSVC\14.40.33807\ATLMFC\lib\x64" "/LIBPATH:C:\Program Files\Microsoft Visual Studio\2022\Community\VC\Tools\MSVC\14.40.33807\lib\x64" "/LIBPATH:C:\Program Files (x86)\Windows Kits\10\lib\10.0.26100.0\ucrt\x64" "/LIBPATH:C:\Program Files (x86)\Windows Kits\10\\lib\10.0.26100.0\\um\x64" /EXPORT:PyInit__matrix_inverse .\Release\_matrix_inverse.obj .\Release\matrix_inverse.obj /OUT:.\_matrix_inverse.cp311-win_amd64.pyd /IMPLIB:.\Release\_matrix_inverse.cp311-win_amd64.lib
   Creating library .\Release\_matrix_inverse.cp311-win_amd64.lib and object .\Release\_matrix_inverse.cp311-win_amd64.exp
Generating code
Finished generating code
```
### output
```
$ python example.py
Input matrix:
[[4 7 2]
 [3 6 1]
 [2 1 5]]
Matrix size n: 3
Input matrix data: [4. 7. 2. 3. 6. 1. 2. 1. 5.]
Allocated matrix at 00000263440638D0, size 3 x 3
Output matrix address (hex): 0x263440638d0
Input pointer: <cdata 'double *' 0x0000026344063150>
Output pointer: <cdata 'double *' 0x00000263440638D0>
Starting inverse_matrix with n=3, input=0000026344063150, output=00000263440638D0
Allocated matrix at 0000026344063920, size 3 x 3
Copying matrix from 0000026344063150 to 0000026344063920
Setting identity matrix at 00000263440638D0
Scaling row 0 with pivot 4.000000
Eliminating column 0, row 1 with factor 3.000000
Eliminating column 0, row 2 with factor 2.000000
Swapping rows 1 and 2
Scaling row 1 with pivot -2.500000
Eliminating column 1, row 0 with factor 1.750000
Eliminating column 1, row 2 with factor 0.750000
Scaling row 2 with pivot 0.700000
Eliminating column 2, row 0 with factor 3.300000
Eliminating column 2, row 1 with factor -1.600000
Freeing matrix at 0000026344063920
Inverse matrix computed successfully
Freeing matrix at 00000263440638D0

Inverse matrix:
[[ 4.14285714 -4.71428571 -0.71428571]
 [-1.85714286  2.28571429  0.28571429]
 [-1.28571429  1.42857143  0.42857143]]

Verification (A * A^-1):
[[ 1.00000000e+00 -1.77635684e-15 -2.22044605e-16]
 [ 2.44249065e-15  1.00000000e+00 -5.55111512e-17]
 [ 1.11022302e-15 -1.55431223e-15  1.00000000e+00]]
```