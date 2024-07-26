#  MMS_Master_study
โปรแกรม diff_check.py สำหรับตรวจสอบค่าพิกัด GNSS ที่วัดได้จากในสนาม
input เป็น GCPs.csv 
เมื่อเราคำนวณมาแล้วจะได้ผลลัพธ์ตามตารางนี้
|    |     dE |     dN |        dH |      dE2 |      dN2 |      dH2 |
|---:|-------:|-------:|----------:|---------:|---------:|---------:|
|  0 |  0.005 |  0.007 | -0.002000 | 0.000025 | 0.000049 | 4e-06    |
|  1 |  0.001 | -0.002 |  0.002000 | 0.000001 | 0.000004 | 4e-06    |
|  2 |  0.000 |  0.000 | -0.006000 | 0.000000 | 0.000000 | 3.6e-05  |
|  3 |  0.000 |  0.003 |  0.001000 | 0.000000 | 0.000009 | 1e-06    |
|  4 |  0.002 |  0.002 | -0.002000 | 0.000004 | 0.000004 | 4e-06    |
|  5 | -0.006 | -0.003 | -0.009000 | 0.000036 | 0.000009 | 8.1e-05  |
|  6 |  0.000 |  0.003 | -0.009000 | 0.000000 | 0.000009 | 8.1e-05  |
|  7 | -0.003 |  0.000 | -0.005000 | 0.000009 | 0.000000 | 2.5e-05  |
|  8 |  0.002 |  0.000 |  0.001000 | 0.000004 | 0.000000 | 1e-06    |
|  9 | -0.004 |  0.002 |  0.003000 | 0.000016 | 0.000004 | 9e-06    |
| 10 |  0.000 |  0.003 | -0.013000 | 0.000000 | 0.000009 | 0.000169 |
| 11 |  0.007 |  0.003 |  0.004000 | 0.000049 | 0.000009 | 1.6e-05  |
| 12 | -0.007 | -0.001 | -0.008000 | 0.000049 | 0.000001 | 6.4e-05  |
| 13 |  0.001 |  0.006 | -0.004000 | 0.000001 | 0.000036 | 1.6e-05  |
| 14 |  0.000 | -0.004 | -0.015000 | 0.000000 | 0.000016 | 0.000225 |
| 15 | -0.004 |  0.000 | -0.013000 | 0.000016 | 0.000000 | 0.000169 |

|RMSE_H | = 0.015 |
|RMSE_V | = 0.008 |

โปรแกรม MMS_RMSE_validation.py สำหรับตรวจสอบค่าพิกัดที่ได้จาก Point Cloud เทียบกับ RTK ที่วัดในสนาม
input เป็น GCP_Measure_edit5_speed_30_60.csv
จงกำหนดวิธีการใช้งาน อย่างเช่น เลือกความเร็วที่สนใจ
เมื่อเราคำนวณมาแล้วจะได้ผลลัพธ์ตามตารางนี้
ตัวอย่างของการคิดความเร็ว 30 km/hr
|    |   NO | Strip                   |   Speed |      E_MMS |       N_MMS |   h_MMS |      E_RTK |       N_RTK |   h_RTK |     dE |     dN |     dh |
|---:|-----:|:------------------------|--------:|-----------:|------------:|--------:|-----------:|------------:|--------:|-------:|-------:|-------:|
|  0 |   14 | 009+300_010+000_FWD.las |      30 | 678411.560 | 1527288.550 | -29.360 | 678411.533 | 1527288.589 | -29.350 |  0.027 | -0.039 | -0.010 |
|  1 |   15 | 009+300_010+000_FWD.las |      30 | 678679.559 | 1527097.680 | -28.810 | 678679.553 | 1527097.762 | -28.840 |  0.006 | -0.082 |  0.030 |
|  2 |   13 | 009+300_010+000_REV.las |      30 | 678666.340 | 1527065.860 | -28.870 | 678666.393 | 1527065.835 | -28.890 | -0.053 |  0.025 |  0.020 |
|  3 |   12 | 009+300_010+000_REV.las |      30 | 678391.410 | 1527259.310 | -29.600 | 678391.341 | 1527259.305 | -29.590 |  0.069 |  0.005 | -0.010 |
|  4 |   16 | 010+000_011+000_FWD.las |      30 | 679087.550 | 1527055.600 | -28.660 | 679087.575 | 1527055.660 | -28.680 | -0.025 | -0.060 |  0.020 |
|  5 |    1 | 010+000_011+000_FWD.las |      30 | 679471.850 | 1527234.360 | -28.230 | 679471.777 | 1527234.408 | -28.270 |  0.073 | -0.048 |  0.040 |
|  6 |    2 | 010+000_011+000_FWD.las |      30 | 679886.000 | 1527384.780 | -28.450 | 679885.955 | 1527384.827 | -28.480 |  0.045 | -0.047 |  0.030 |
|  7 |   11 | 010+000_011+000_REV.las |      30 | 679096.000 | 1527033.110 | -28.720 | 679095.989 | 1527033.098 | -28.730 |  0.011 |  0.012 |  0.010 |
|  8 |   10 | 010+000_011+000_REV.las |      30 | 679468.460 | 1527205.690 | -28.330 | 679468.435 | 1527205.682 | -28.320 |  0.025 |  0.008 | -0.010 |
|  9 |    9 | 010+000_011+000_REV.las |      30 | 679883.570 | 1527356.870 | -28.450 | 679883.581 | 1527356.883 | -28.440 | -0.011 | -0.013 | -0.010 |
| 10 |    3 | 011+000_012+000_FWD.las |      30 | 680265.209 | 1527515.070 | -28.690 | 680265.197 | 1527515.106 | -28.700 |  0.012 | -0.036 |  0.010 |
| 11 |    4 | 011+000_012+000_FWD.las |      30 | 680677.410 | 1527698.020 | -28.480 | 680677.419 | 1527698.100 | -28.490 | -0.009 | -0.080 |  0.010 |
| 12 |    8 | 011+000_012+000_REV.las |      30 | 680268.140 | 1527490.340 | -28.690 | 680268.134 | 1527490.313 | -28.700 |  0.006 |  0.027 |  0.010 |
| 13 |    7 | 011+000_012+000_REV.las |      30 | 680734.200 | 1527597.940 | -28.470 | 680734.242 | 1527597.892 | -28.460 | -0.042 |  0.048 | -0.010 |
| 14 |    5 | 012+000_012+419_FWD.las |      30 | 681193.950 | 1527766.530 | -28.400 | 681193.957 | 1527766.597 | -28.410 | -0.007 | -0.067 |  0.010 |
| 15 |    6 | 012+000_012+407_REV.las |      30 | 681222.890 | 1527696.770 | -28.550 | 681222.923 | 1527696.746 | -28.560 | -0.033 |  0.024 |  0.010 |

|RMSE_H  |= 0.058|
|RMSE_V  |= 0.018|
|RMSE_3d |= 0.061|


