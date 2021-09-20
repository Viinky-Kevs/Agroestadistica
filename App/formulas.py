from scipy import stats
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import plotly as ply

def T_student(request):

	file = request.FILES("myFile")

	df = pd.read_excel(file)

	names_col = []

	for col in df.columns:
		names_col.append(col)

	print(names_col)

	option_1 = input()
	option_2 = input()

	options = []

	if option_1 in names_col:
		options.append(df[option_1])

	if option_2 in names_col:
		options.append(df[option_2])


	T_test = stats.ttest_ind(options[0], options[1])
	p_value = T_test.pvalue

	if p_value < 0.05:
		print("Existe diferencia estadística significativa")
		print(f"El p valor es: {p_value}")
		print(f"{p_value} < 0.05 ")
	else:
		print(("No existe diferencia estadística significativa"))
		print(f"El p valor es: {p_value}")
		print(f"{p_value} > 0.05 ")
