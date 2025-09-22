
```
python3 project_code.py 
  utm_source  user_id
0      email      255
1   facebook      504
2     google      680
3    twitter      215

  utm_source  is_click  user_id
0      email     False      175
1      email      True       80
2   facebook     False      324
3   facebook      True      180
4     google     False      441
5     google      True      239
6    twitter     False      149
7    twitter      True       66

is_click utm_source  False  True
0             email    175    80
1          facebook    324   180
2            google    441   239
3           twitter    149    66

is_click utm_source  False  True  percent_clicked
0             email    175    80         0.313725
1          facebook    324   180         0.357143
2            google    441   239         0.351471
3           twitter    149    66         0.306977

  experimental_group  user_id
0                  A      827
1                  B      827

  experimental_group  is_click  user_id
0                  A     False      517
1                  A      True      310
2                  B     False      572
3                  B      True      255

is_click experimental_group  False  True
0                         A    517   310
1                         B    572   255

is_click experimental_group  False  True  percent_clicked
0                         A    517   310         0.374849
1                         B    572   255         0.308343

is_click            day  False  True  percent_clicked
0            1 - Monday     70    43         0.380531
1           2 - Tuesday     76    43         0.361345
2         3 - Wednesday     86    38         0.306452
3          4 - Thursday     69    47         0.405172
4            5 - Friday     77    51         0.398438
5          6 - Saturday     73    45         0.381356
6            7 - Sunday     66    43         0.394495

is_click            day  False  True  percent_clicked
0            1 - Monday     81    32         0.283186
1           2 - Tuesday     74    45         0.378151
2         3 - Wednesday     89    35         0.282258
3          4 - Thursday     87    29         0.250000
4            5 - Friday     90    38         0.296875
5          6 - Saturday     76    42         0.355932
6            7 - Sunday     75    34         0.311927

Based on the weekly click rates, we recommend Ad A because it preformed better over Ad B
```
