
using scikit-learn

In this notebook, we will use scikit-learn to perform a decision tree based classification of weather data.

```python

from sklearn.metrics import accuracy_score
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
```

```python
data = pd.read_csv('./weather/daily_weather.csv')
```

The file **daily_weather.csv** is a comma-separated file that contains weather data. This data comes from a weather station located in San Diego, California. The weather station is equipped with sensors that capture weather-related measurements such as air temperature, air pressure, and relative humidity. Data was collected for a period of three years, from September 2011 to September 2014, to ensure that sufficient data for different seasons and weather conditions is captured.
Let's now check all the columns in the data.

```python
data.columns
```

    Index(['number', 'air_pressure_9am', 'air_temp_9am', 'avg_wind_direction_9am',
           'avg_wind_speed_9am', 'max_wind_direction_9am', 'max_wind_speed_9am',
           'rain_accumulation_9am', 'rain_duration_9am', 'relative_humidity_9am',
           'relative_humidity_3pm'],
          dtype='object')

Each row in daily_weather.csv captures weather data for a separate day.
Sensor measurements from the weather station were captured at one-minute intervals. These measurements were then processed to generate values to describe daily weather. Since this dataset was created to classify low-humidity days vs. non-low-humidity days (that is, days with normal or high humidity), the variables included are weather measurements in the morning, with one measurement, namely relatively humidity, in the afternoon. The idea is to use the morning weather values to predict whether the day will be low-humidity or not based on the afternoon measurement of relative humidity.
Each row, or sample, consists of the following variables:

- **number:** unique number for each row
- **air_pressure_9am:** air pressure averaged over a period from 8:55am to 9:04am (_Unit: hectopascals_)
- **air_temp_9am:** air temperature averaged over a period from 8:55am to 9:04am (_Unit: degrees Fahrenheit_)
- **air_wind_direction_9am:** wind direction averaged over a period from 8:55am to 9:04am (_Unit: degrees, with 0 means coming from the North, and increasing clockwise_)
- **air_wind_speed_9am:** wind speed averaged over a period from 8:55am to 9:04am (_Unit: miles per hour_)
- ** max_wind_direction_9am:** wind gust direction averaged over a period from 8:55am to 9:10am (_Unit: degrees, with 0 being North and increasing clockwise_)
- **max_wind_speed_9am:** wind gust speed averaged over a period from 8:55am to 9:04am (_Unit: miles per hour_)
- **rain_accumulation_9am:** amount of rain accumulated in the 24 hours prior to 9am (_Unit: millimeters_)
- **rain_duration_9am:** amount of time rain was recorded in the 24 hours prior to 9am (_Unit: seconds_)
- **relative_humidity_9am:** relative humidity averaged over a period from 8:55am to 9:04am (_Unit: percent_)
- **relative_humidity_3pm:** relative humidity averaged over a period from 2:55pm to 3:04pm (_Unit: percent _)

```python

```

|      | number | air_pressure_9am | air_temp_9am | avg_wind_direction_9am | avg_wind_speed_9am | max_wind_direction_9am | max_wind_speed_9am | rain_accumulation_9am | rain_duration_9am | relative_humidity_9am | relative_humidity_3pm |
| ---- | ------ | ---------------- | ------------ | ---------------------- | ------------------ | ---------------------- | ------------------ | --------------------- | ----------------- | --------------------- | --------------------- |
| 0    | 0      | 918.060000       | 74.822000    | 271.100000             | 2.080354           | 295.400000             | 2.863283           | 0.00                  | 0.0               | 42.420000             | 36.160000             |
| 1    | 1      | 917.347688       | 71.403843    | 101.935179             | 2.443009           | 140.471548             | 3.533324           | 0.00                  | 0.0               | 24.328697             | 19.426597             |
| 2    | 2      | 923.040000       | 60.638000    | 51.000000              | 17.067852          | 63.700000              | 22.100967          | 0.00                  | 20.0              | 8.900000              | 14.460000             |
| 3    | 3      | 920.502751       | 70.138895    | 198.832133             | 4.337363           | 211.203341             | 5.190045           | 0.00                  | 0.0               | 12.189102             | 12.742547             |
| 4    | 4      | 921.160000       | 44.294000    | 277.800000             | 1.856660           | 136.500000             | 2.863283           | 8.90                  | 14730.0           | 92.410000             | 76.740000             |
| 5    | 5      | 915.300000       | 78.404000    | 182.800000             | 9.932014           | 189.000000             | 10.983375          | 0.02                  | 170.0             | 35.130000             | 33.930000             |
| 6    | 6      | 915.598868       | 70.043304    | 177.875407             | 3.745587           | 186.606696             | 4.589632           | 0.00                  | 0.0               | 10.657422             | 21.385657             |
| 7    | 7      | 918.070000       | 51.710000    | 242.400000             | 2.527742           | 271.600000             | 3.646212           | 0.00                  | 0.0               | 80.470000             | 74.920000             |
| 8    | 8      | 920.080000       | 80.582000    | 40.700000              | 4.518619           | 63.000000              | 5.883152           | 0.00                  | 0.0               | 29.580000             | 24.030000             |
| 9    | 9      | 915.010000       | 47.498000    | 163.100000             | 4.943637           | 195.900000             | 6.576604           | 0.00                  | 0.0               | 88.600000             | 68.050000             |
| 10   | 10     | 919.650000       | 77.036000    | 70.600000              | 3.825167           | 85.500000              | 4.764682           | 0.00                  | 0.0               | 22.070000             | 32.130000             |
| 11   | 11     | 915.640000       | 45.716000    | 241.600000             | 5.860783           | 265.800000             | 8.030615           | 0.55                  | 1770.0            | 90.560000             | 79.090000             |
| 12   | 12     | 917.390000       | 49.784000    | 204.100000             | 1.275056           | 211.800000             | 2.013246           | 0.00                  | 0.0               | 73.150000             | 58.430000             |
| 13   | 13     | 920.820000       | 62.438000    | 213.600000             | 2.617220           | 165.700000             | 3.310671           | 0.00                  | 0.0               | 43.640000             | 27.990000             |
| 14   | 14     | 911.000000       | 86.432000    | 202.900000             | 1.207948           | 162.900000             | 1.677705           | 0.00                  | 0.0               | 15.190000             | 24.370000             |
| 15   | 15     | 922.383131       | 70.865263    | 36.174175              | 1.847278           | 58.428632              | 2.529142           | 0.00                  | 0.0               | 12.110889             | 14.801706             |
| 16   | 16     | 917.890000       | NaN          | 169.200000             | 2.192201           | 196.800000             | 2.930391           | 0.00                  | 0.0               | 48.990000             | 51.190000             |
| 17   | 17     | 916.915255       | 77.018961    | 234.539345             | 2.274725           | 229.474199             | 2.906513           | 0.00                  | 0.0               | 21.031462             | 20.755683             |
| 18   | 18     | 918.800000       | 67.082000    | 176.100000             | 4.876529           | 183.400000             | 5.569981           | 0.00                  | 0.0               | 18.900000             | 45.870000             |
| 19   | 19     | 922.040000       | 68.576000    | 58.300000              | 9.551734           | 81.900000              | 12.571603          | 0.00                  | 0.0               | 7.540000              | 7.740000              |
| 20   | 20     | 919.992262       | 62.964383    | 54.799094              | 12.680436          | 74.254223              | 15.452306          | 0.00                  | 0.0               | 18.809518             | 14.649909             |
| 21   | 21     | 917.230000       | 67.676000    | 177.800000             | 2.460634           | 93.200000              | 3.288302           | 0.00                  | 0.0               | 40.640000             | 41.340000             |
| 22   | 22     | 921.125626       | 68.818772    | 71.799092              | 2.576538           | 95.472334              | 3.487444           | 0.00                  | 0.0               | 11.742201             | 17.281161             |
| 23   | 23     | 920.350000       | 47.570000    | 192.100000             | 6.263432           | 205.700000             | 7.605596           | 0.00                  | 0.0               | 54.550000             | 66.000000             |
| 24   | 24     | 921.788229       | 71.659572    | 217.405520             | 1.946447           | 253.758003             | 2.719712           | 0.00                  | 0.0               | 11.194250             | 16.331716             |
| 25   | 25     | 918.030000       | 50.666000    | 128.900000             | 2.527742           | 117.400000             | 4.004123           | 0.00                  | 0.0               | 76.880000             | 47.030000             |
| 26   | 26     | 914.490000       | 49.892000    | 163.000000             | 4.854160           | 189.600000             | 6.733189           | 0.00                  | 0.0               | 92.100000             | 90.990000             |
| 27   | 27     | 914.900000       | 78.620000    | 203.300000             | 1.811921           | 240.000000             | 2.751436           | 0.00                  | 220.0             | 47.890000             | 43.900000             |
| 28   | 28     | 915.840000       | 40.118000    | 171.900000             | 10.535987          | 188.000000             | 12.929513          | 0.00                  | 0.0               | 86.430000             | 84.390000             |
| 29   | 29     | 916.310000       | 45.428000    | 183.100000             | 8.343786           | 194.600000             | 10.088599          | 0.00                  | 0.0               | 86.150000             | 90.580000             |
| ...  | ...    | ...              | ...          | ...                    | ...                | ...                    | ...                | ...                   | ...               | ...                   | ...                   |
| 1065 | 1065   | 915.600000       | 69.584000    | 185.500000             | 4.630466           | 198.200000             | 5.480503           | 0.00                  | 0.0               | 28.970000             | 39.370000             |
| 1066 | 1066   | 919.564869       | 73.726732    | 68.704694              | 3.551777           | 102.571616             | 4.861315           | NaN                   | 0.0               | 11.657314             | 17.331823             |
| 1067 | 1067   | 917.690000       | 64.994000    | 178.300000             | 2.975130           | 193.900000             | 3.735690           | 0.00                  | 0.0               | 54.880000             | 52.070000             |
| 1068 | 1068   | 920.330000       | 68.864000    | 122.400000             | 2.035615           | 182.000000             | 3.086977           | 0.00                  | 0.0               | 52.380000             | 62.620000             |
| 1069 | 1069   | 918.260000       | 82.220000    | 186.600000             | 1.096101           | 221.500000             | 1.722444           | 0.00                  | 0.0               | 32.460000             | 56.930000             |
| 1070 | 1070   | 911.600000       | 46.346000    | 110.200000             | 2.304048           | 96.100000              | 3.154085           | 0.00                  | 0.0               | 90.510000             | 62.490000             |
| 1071 | 1071   | 919.200000       | 70.250000    | 156.700000             | 2.013246           | 172.300000             | 2.617220           | 0.00                  | 0.0               | 42.060000             | 41.850000             |
| 1072 | 1072   | 923.100000       | 75.596000    | 178.300000             | 1.409272           | 205.200000             | 1.856660           | 0.00                  | 0.0               | 11.880000             | 19.810000             |
| 1073 | 1073   | 917.920000       | 84.650000    | 30.000000              | 4.831790           | 40.100000              | 5.838413           | 0.00                  | 0.0               | 16.220000             | 27.450000             |
| 1074 | 1074   | 913.870000       | 66.938000    | 171.900000             | 6.509495           | 182.300000             | 7.471380           | 0.00                  | 0.0               | 57.430000             | 53.380000             |
| 1075 | 1075   | 922.858110       | 64.989361    | 63.483047              | 10.261187          | 73.170504              | 11.949206          | 0.00                  | 0.0               | 14.525109             | 15.511157             |
| 1076 | 1076   | 925.550000       | 50.918000    | 32.600000              | 5.413395           | 57.500000              | 8.120092           | 0.00                  | 10.0              | 29.090000             | 23.720000             |
| 1077 | 1077   | 920.130000       | 73.292000    | 193.600000             | 4.115970           | 211.300000             | 4.966007           | 0.00                  | 0.0               | 33.520000             | 38.120000             |
| 1078 | 1078   | 924.017856       | 68.370307    | 56.304083              | 15.162800          | 76.585117              | 19.803578          | 0.00                  | 0.0               | 11.599240             | 9.373013              |
| 1079 | 1079   | 917.200000       | 65.264000    | 137.600000             | 1.767183           | 176.700000             | 2.550112           | 0.00                  | 0.0               | 58.370000             | 65.590000             |
| 1080 | 1080   | 916.260000       | 79.772000    | 185.700000             | 3.511996           | 201.500000             | 4.160708           | 0.00                  | 0.0               | 27.680000             | 20.400000             |
| 1081 | 1081   | 920.856913       | 69.884338    | 47.335966              | 12.238670          | 66.729162              | 16.067860          | 0.00                  | 0.0               | 11.956852             | 12.696233             |
| 1082 | 1082   | 916.130000       | 50.108000    | 211.400000             | 2.550112           | 231.800000             | 3.534365           | 0.00                  | 0.0               | 89.800000             | 53.860000             |
| 1083 | 1083   | 916.320000       | 48.308000    | 46.900000              | 4.854160           | 61.700000              | 5.860783           | 0.00                  | 0.0               | 91.030000             | 62.400000             |
| 1084 | 1084   | 917.130000       | 80.240000    | 183.300000             | 1.632966           | 38.500000              | 2.259309           | 0.00                  | 0.0               | 28.260000             | 34.690000             |
| 1085 | 1085   | 914.840000       | 47.354000    | 190.900000             | 3.713320           | 204.400000             | 4.652835           | 0.00                  | 0.0               | 92.300000             | 88.160000             |
| 1086 | 1086   | 921.260000       | 52.646000    | 261.900000             | 2.035615           | 260.500000             | 3.042238           | 0.00                  | 0.0               | 91.110000             | 81.890000             |
| 1087 | 1087   | 914.000000       | 66.650000    | 173.800000             | 8.366156           | 181.000000             | 9.439887           | 0.00                  | 0.0               | 30.920000             | 47.340000             |
| 1088 | 1088   | 912.900000       | 71.870000    | 129.200000             | 1.431642           | 160.000000             | 2.057985           | 0.00                  | 0.0               | 51.840000             | 55.490000             |
| 1089 | 1089   | 915.000000       | 55.040000    | 191.800000             | 5.368656           | 220.900000             | 7.068730           | 0.00                  | 0.0               | 73.550000             | 69.670000             |
| 1090 | 1090   | 918.900000       | 63.104000    | 192.900000             | 3.869906           | 207.300000             | 5.212070           | 0.00                  | 0.0               | 26.020000             | 38.180000             |
| 1091 | 1091   | 918.710000       | 49.568000    | 241.600000             | 1.811921           | 227.400000             | 2.371156           | 0.00                  | 0.0               | 90.350000             | 73.340000             |
| 1092 | 1092   | 916.600000       | 71.096000    | 189.300000             | 3.064608           | 200.800000             | 3.892276           | 0.00                  | 0.0               | 45.590000             | 52.310000             |
| 1093 | 1093   | 912.600000       | 58.406000    | 172.700000             | 3.825167           | 189.100000             | 4.764682           | 0.00                  | 0.0               | 64.840000             | 58.280000             |
| 1094 | 1094   | 921.530000       | 77.702000    | 97.100000              | 3.265932           | 125.900000             | 4.451511           | 0.00                  | 0.0               | 14.560000             | 15.100000             |

1095 rows × 11 columns

```python
data[data.isnull().any(axis=1)]
```

|      | number | air_pressure_9am | air_temp_9am | avg_wind_direction_9am | avg_wind_speed_9am | max_wind_direction_9am | max_wind_speed_9am | rain_accumulation_9am | rain_duration_9am | relative_humidity_9am | relative_humidity_3pm |
| ---- | ------ | ---------------- | ------------ | ---------------------- | ------------------ | ---------------------- | ------------------ | --------------------- | ----------------- | --------------------- | --------------------- |
| 16   | 16     | 917.890000       | NaN          | 169.200000             | 2.192201           | 196.800000             | 2.930391           | 0.000                 | 0.000000          | 48.990000             | 51.190000             |
| 111  | 111    | 915.290000       | 58.820000    | 182.600000             | 15.613841          | 189.000000             | NaN                | 0.000                 | 0.000000          | 21.500000             | 29.690000             |
| 177  | 177    | 915.900000       | NaN          | 183.300000             | 4.719943           | 189.900000             | 5.346287           | 0.000                 | 0.000000          | 29.260000             | 46.500000             |
| 262  | 262    | 923.596607       | 58.380598    | 47.737753              | 10.636273          | 67.145843              | 13.671423          | 0.000                 | NaN               | 17.990876             | 16.461685             |
| 277  | 277    | 920.480000       | 62.600000    | 194.400000             | 2.751436           | NaN                    | 3.869906           | 0.000                 | 0.000000          | 52.580000             | 54.030000             |
| 334  | 334    | 916.230000       | 75.740000    | 149.100000             | 2.751436           | 187.500000             | 4.183078           | NaN                   | 1480.000000       | 31.880000             | 32.900000             |
| 358  | 358    | 917.440000       | 58.514000    | 55.100000              | 10.021491          | NaN                    | 12.705819          | 0.000                 | 0.000000          | 13.880000             | 25.930000             |
| 361  | 361    | 920.444946       | 65.801845    | 49.823346              | 21.520177          | 61.886944              | 25.549112          | NaN                   | 40.364018         | 12.278715             | 7.618649              |
| 381  | 381    | 918.480000       | 66.542000    | 90.900000              | 3.467257           | 89.400000              | 4.406772           | NaN                   | 0.000000          | 20.640000             | 14.350000             |
| 409  | 409    | NaN              | 67.853833    | 65.880616              | 4.328594           | 78.570923              | 5.216734           | 0.000                 | 0.000000          | 18.487385             | 20.356594             |
| 517  | 517    | 920.570000       | 53.600000    | 100.100000             | 4.697574           | NaN                    | 6.285801           | 4.712                 | 14842.000000      | 79.880000             | 84.530000             |
| 519  | 519    | 916.250000       | 55.670000    | 176.400000             | 6.666081           | 188.200000             | NaN                | 0.000                 | 0.000000          | 72.550000             | 74.390000             |
| 546  | 546    | NaN              | 42.746000    | 251.100000             | 12.929513          | 274.400000             | 17.604718          | 14.627                | 7825.000000       | 87.870000             | 70.770000             |
| 620  | 620    | 921.200000       | 56.786000    | 192.300000             | 9.551734           | 201.400000             | 11.005745          | NaN                   | 0.000000          | 59.790000             | 77.750000             |
| 625  | 625    | 912.400000       | 50.774000    | 171.600000             | NaN                | 181.400000             | 4.831790           | 0.000                 | 0.000000          | 86.840000             | 64.740000             |
| 656  | 656    | 920.830000       | 66.344000    | NaN                    | 15.457255          | 189.400000             | 16.486248          | 0.000                 | 0.000000          | 23.770000             | 51.630000             |
| 670  | 670    | 910.920000       | 48.362000    | 156.500000             | NaN                | 177.500000             | 16.128337          | 4.970                 | 10560.000000      | 80.560000             | 88.220000             |
| 672  | 672    | 922.448945       | 72.863773    | NaN                    | 3.682370           | 214.196160             | 4.849450           | 0.000                 | 0.000000          | 16.753670             | 17.804720             |
| 705  | 705    | 911.900000       | 59.072000    | 199.800000             | 1.275056           | 239.500000             | 1.834291           | NaN                   | 0.000000          | 77.630000             | 59.130000             |
| 731  | 731    | 922.970166       | 51.391847    | 33.810942              | NaN                | 59.290089              | 11.111555          | 0.000                 | 4.735034          | 34.807753             | 18.418179             |
| 737  | 737    | 917.895130       | 76.804690    | 104.771020             | 1.632705           | 97.178763              | NaN                | 0.000                 | 0.000000          | 13.771311             | 16.792455             |
| 788  | 788    | 917.923442       | 73.249717    | 42.101739              | 4.132698           | 64.284969              | 5.345258           | 0.000                 | NaN               | 6.939692              | 18.793825             |
| 840  | 840    | 918.043767       | NaN          | 181.774042             | 0.964376           | 185.618601             | 1.570007           | 0.000                 | 0.000000          | 11.911222             | 18.154358             |
| 848  | 848    | 915.250000       | 37.562000    | 246.500000             | 11.587349          | 258.700000             | NaN                | 3.171                 | 2891.000000       | 91.000000             | 90.780000             |
| 861  | 861    | 919.065408       | NaN          | 172.303728             | 2.639600           | 193.058141             | 3.326949           | 0.000                 | 0.000000          | 12.497839             | 13.438518             |
| 869  | 869    | NaN              | 45.104000    | 259.000000             | 3.265932           | 275.000000             | 4.026492           | 0.000                 | 80.000000         | 85.270000             | 90.260000             |
| 998  | 998    | 914.140000       | 71.240000    | NaN                    | 1.722444           | 232.900000             | 2.326418           | 0.000                 | 0.000000          | 24.200000             | 41.380000             |
| 1031 | 1031   | 922.669195       | NaN          | 47.946284              | 7.969686           | 65.770066              | 10.262337          | 0.000                 | 0.000000          | 18.920805             | 19.641841             |
| 1035 | 1035   | 919.670000       | 77.576000    | 171.800000             | 6.554234           | 191.000000             | 8.164831           | 0.000                 | NaN               | 56.860000             | 50.650000             |
| 1063 | 1063   | 917.300185       | 65.790001    | NaN                    | 1.879553           | 222.498226             | 2.692862           | 0.000                 | 0.000000          | 14.972668             | 20.966267             |
| 1066 | 1066   | 919.564869       | 73.726732    | 68.704694              | 3.551777           | 102.571616             | 4.861315           | NaN                   | 0.000000          | 11.657314             | 17.331823             |

We will not need to number for each row so we can clean it.

```python
del data['number']
```

Now let's drop null values using the _pandas dropna_ function.

```python
before_rows = data.shape[0]
print(before_rows)
```

    1095

```python
data = data.dropna()
```

```python
after_rows = data.shape[0]
print(after_rows)
```

    1064

How many rows dropped due to cleaning?

```python
before_rows - after_rows
```

    31

Binarize the relative_humidity_3pm to 0 or 1.

```python
clean_data = data.copy()
clean_data['high_humidity_label'] = (clean_data['relative_humidity_3pm'] > 24.99)*1
print(clean_data['high_humidity_label'])
```

    0       1
    1       0
    2       0
    3       0
    4       1
    5       1
    6       0
    7       1
    8       0
    9       1
    10      1
    11      1
    12      1
    13      1
    14      0
    15      0
    16      1
    17      0
    18      1
    19      0
    20      0
    21      1
    22      0
    23      1
    24      0
    25      1
    26      1
    27      1
    28      1
    29      1
           ..
    1065    1
    1066    0
    1067    1
    1068    1
    1069    1
    1070    1
    1071    1
    1072    0
    1073    1
    1074    1
    1075    0
    1076    0
    1077    1
    1078    0
    1079    1
    1080    0
    1081    0
    1082    1
    1083    1
    1084    1
    1085    1
    1086    1
    1087    1
    1088    1
    1089    1
    1090    1
    1091    1
    1092    1
    1093    1
    1094    0
    Name: high_humidity_label, Length: 1095, dtype: int64

Target is stored in 'y'.

```python
y=clean_data[['high_humidity_label']].copy()
#y
```

```python
clean_data['relative_humidity_3pm'].head()
```

    0    36.160000
    1    19.426597
    2    14.460000
    3    12.742547
    4    76.740000
    Name: relative_humidity_3pm, dtype: float64

```python
y.head()
```

|     | high_humidity_label |
| --- | ------------------- |
| 0   | 1                   |
| 1   | 0                   |
| 2   | 0                   |
| 3   | 0                   |
| 4   | 1                   |

Use 9am Sensor Signals as Features to Predict Humidity at 3pm

```python
morning_features = ['air_pressure_9am','air_temp_9am','avg_wind_direction_9am','avg_wind_speed_9am',
'max_wind_direction_9am','max_wind_speed_9am','rain_accumulation_9am',
'rain_duration_9am']
```

```python
X = clean_data[morning_features].copy()
```

```python
X.columns
```

    Index(['air_pressure_9am', 'air_temp_9am', 'avg_wind_direction_9am',
           'avg_wind_speed_9am', 'max_wind_direction_9am', 'max_wind_speed_9am',
           'rain_accumulation_9am', 'rain_duration_9am'],
          dtype='object')

```python
y.columns
```

    Index(['high_humidity_label'], dtype='object')

## REMINDER: Training Phase

In the **training phase**, the learning algorithm uses the training data to adjust the model’s parameters to minimize errors. At the end of the training phase, you get the trained model.
_[Image: Training vs Testing Comparison - file not found]_

In the **testing phase**, the trained model is applied to test data. Test data is separate from the training data, and is previously unseen by the model. The model is then evaluated on how it performs on the test data. The goal in building a classifier model is to have the model perform well on training as well as test data.

```python
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.33, random_state=324)
```

```python
#type(X_train)
#type(X_test)
#type(y_train)
#type(y_test)
#X_train.head()
#y_train.describe()
```

## Fit on Train Set

```python
humidity_classifier = DecisionTreeClassifier(max_leaf_nodes=10, random_state=0)
humidity_classifier.fit(X_train, y_train)
```

    DecisionTreeClassifier(class_weight=None, criterion='gini', max_depth=None,
                max_features=None, max_leaf_nodes=10,
                min_impurity_decrease=0.0, min_impurity_split=None,
                min_samples_leaf=1, min_samples_split=2,
                min_weight_fraction_leaf=0.0, presort=False, random_state=0,
                splitter='best')

```python
type(humidity_classifier)
```

    sklearn.tree.tree.DecisionTreeClassifier

## Predict on Test Set

```python
predictions = humidity_classifier.predict(X_test)
```

```python
predictions[:10]
```

    array([0, 0, 1, 1, 1, 1, 0, 0, 0, 1])

```python
y_test['high_humidity_label'][:10]
```

    456     0
    845     0
    693     1
    259     1
    723     1
    224     1
    300     1
    442     0
    585     1
    1057    1
    Name: high_humidity_label, dtype: int64

```python
accuracy_score(y_true = y_test, y_pred = predictions)
```

    0.8153409090909091

```python

```
