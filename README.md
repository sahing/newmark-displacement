
Newmark Sliding Block Analysis - Sample Dataset and Instructions
================================================================

1. File: acceleration_sample.csv
--------------------------------
This file contains a sample acceleration time history in two columns:
- Time (in seconds)
- Acceleration (in g units, where 1g = 9.81 m/s²)

2. How to Use:
--------------
Use this CSV file as input to a Python script performing Newmark’s Sliding Block analysis.

The script will:
- Subtract a user-defined yield acceleration (a_y in g)
- Convert the remaining acceleration to m/s²
- Integrate to get velocity and displacement
- Output total permanent displacement

3. Example Python Call:
-----------------------
Assuming a_y = 0.06 g,

```python
df_result = newmark_displacement('acceleration_sample.csv', yield_acc_g=0.06)
```

4. Notes:
---------
- Make sure you have pandas and matplotlib installed.
- The data here is artificial and for demonstration only.
# newmark-displacement
