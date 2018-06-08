```sh
$ ls
choose1or2.md        cp/                  export-chrome-history.md
iris-dataset.csv*    kmeans.pdf           kmeans.py
korean-names/        ml/                  newspapers.md
np_meshgrid.ipynb    openbox/             plot3d_iris_123.svg
plot3d_iris_124.svg  plot3d_iris_134.svg  plot3d_iris_234.svg
plot3d_iris.md       plot3d_iris.py       quadratic-programming.ipynb
README.md            remember.md          scripts/
svm-iris3d.ipynb     svm-iris3d.md        svm-iris3d.svg
$ echo plot3d_iris* svm-iris3d.*
plot3d_iris_123.svg plot3d_iris_124.svg plot3d_iris_134.svg plot3d_iris_234.svg plot3d_iris.md plot3d_iris.py svm-iris3d.ipynb svm-iris3d.md svm-iris3d.svg
$ list=`echo plot3d_iris* svm-iris3d.*`
$ echo $list
plot3d_iris_123.svg plot3d_iris_124.svg plot3d_iris_134.svg plot3d_iris_234.svg plot3d_iris.md plot3d_iris.py svm-iris3d.ipynb svm-iris3d.md svm-iris3d.svg
$ git mv $list ml/
$ for i in $list; echo $i; done
bash: syntax error near unexpected token `echo'
$ for i in $list; do echo $i; done
plot3d_iris_123.svg
plot3d_iris_124.svg
plot3d_iris_134.svg
plot3d_iris_234.svg
plot3d_iris.md
plot3d_iris.py
svm-iris3d.ipynb
svm-iris3d.md
svm-iris3d.svg
$ for i in $list; do echo ml/$i; done
ml/plot3d_iris_123.svg
ml/plot3d_iris_124.svg
ml/plot3d_iris_134.svg
ml/plot3d_iris_234.svg
ml/plot3d_iris.md
ml/plot3d_iris.py
ml/svm-iris3d.ipynb
ml/svm-iris3d.md
ml/svm-iris3d.svg
$ list2=`for i in $list; do echo ml/$i; done`
$ echo $list2
ml/plot3d_iris_123.svg ml/plot3d_iris_124.svg ml/plot3d_iris_134.svg ml/plot3d_iris_234.svg ml/plot3d_iris.md ml/plot3d_iris.py ml/svm-iris3d.ipynb ml/svm-iris3d.md ml/svm-iris3d.svg
$ git commit $list $list2 -m 'move to ml/'
[master c9aa8ad] move to ml/
 9 files changed, 0 insertions(+), 0 deletions(-)
 rename plot3d_iris.md => ml/plot3d_iris.md (100%)
 rename plot3d_iris.py => ml/plot3d_iris.py (100%)
 rename plot3d_iris_123.svg => ml/plot3d_iris_123.svg (100%)
 rename plot3d_iris_124.svg => ml/plot3d_iris_124.svg (100%)
 rename plot3d_iris_134.svg => ml/plot3d_iris_134.svg (100%)
 rename plot3d_iris_234.svg => ml/plot3d_iris_234.svg (100%)
 rename svm-iris3d.ipynb => ml/svm-iris3d.ipynb (100%)
 rename svm-iris3d.md => ml/svm-iris3d.md (100%)
 rename svm-iris3d.svg => ml/svm-iris3d.svg (100%)
```

... previously unfortunately I didn't commit paired files (mv-from mv-to)
at once, and Github thinks some files are removed and created again,
instead of being renamed.

```sh
 2660  Friday, June 08, 2018 PM03:11:52 HKT mkdir ml
 2661  Friday, June 08, 2018 PM03:12:01 HKT git mv plot3d_iris* ml/
 2662  Friday, June 08, 2018 PM03:12:05 HKT git mv svm-iris3d.* ml/
 2663  Friday, June 08, 2018 PM03:12:12 HKT rm *~
 2664  Friday, June 08, 2018 PM03:12:14 HKT git mv svm-iris3d.* ml/
 2665  Friday, June 08, 2018 PM03:12:20 HKT rm svm-iris3d.png 
 2666  Friday, June 08, 2018 PM03:12:21 HKT git mv svm-iris3d.* ml/
 2667  Friday, June 08, 2018 PM03:12:24 HKT git diff
 2668  Friday, June 08, 2018 PM03:12:28 HKT git push
 2669  Friday, June 08, 2018 PM03:12:42 HKT git push
 2670  Friday, June 08, 2018 PM03:13:52 HKT git commit ml/*
 2671  Friday, June 08, 2018 PM03:15:01 HKT git commit ml/* plot3d_iris_123.svg  plot3d_iris_124.svg  plot3d_iris_134.svg -m'move to ml/'
 2672  Friday, June 08, 2018 PM03:15:10 HKT git commit ml/* plot3d_iris_123.svg  plot3d_iris_124.svg  plot3d_iris_134.svg plot3d_iris_234.svg  plot3d_iris.md       plot3d_iris.py  -m'move to ml/'
 2673  Friday, June 08, 2018 PM03:15:18 HKT git commit plot3d_iris_234.svg  plot3d_iris.md       plot3d_iris.py
 2674  Friday, June 08, 2018 PM03:15:27 HKT git commit plot3d_iris_234.svg  plot3d_iris.md       plot3d_iris.py svm-iris3d.ipynb     svm-iris3d.md        svm-iris3d.svg
 2675  Friday, June 08, 2018 PM03:15:30 HKT git commit plot3d_iris_234.svg  plot3d_iris.md       plot3d_iris.py svm-iris3d.ipynb     svm-iris3d.md        svm-iris3d.svg
 2676  Friday, June 08, 2018 PM03:15:35 HKT git commit plot3d_iris_234.svg  plot3d_iris.md       plot3d_iris.py svm-iris3d.ipynb     svm-iris3d.md        svm-iris3d.svg -m'move to ml/'
 2677  Friday, June 08, 2018 PM03:17:30 HKT git reset --hard HEAD~1
 2678  Friday, June 08, 2018 PM03:17:34 HKT git reset --hard HEAD~1
 2679  Friday, June 08, 2018 PM03:17:37 HKT ls
 2680  Friday, June 08, 2018 PM03:17:38 HKT git log
 2681  Friday, June 08, 2018 PM03:17:41 HKT git reset --hard HEAD~1
```

