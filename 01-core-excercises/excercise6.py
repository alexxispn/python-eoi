e = 2.71828
'2.718'
'2.718280'
'    2.72'  # 4 espacios en blanco
'2.718280e+00'
'00002.7183'
'            2.71828'  # 12 espacios en blanco
print(f"{e}")
print(f"{e:.3f}")
print(f"{e:.6f}")
print(f"{e:8.2f}")
print(f"{e:e}")
print(f"0000{e:.4f}")
print(f"{e:19.5f}")

curso = "EOI CURSO DE PYTHON"
print(f"{curso = }")
print(f"{curso:=^30}")
print(f"{curso:=>30}")
print(f"{curso:=<30}")
print(f"{curso: ^30}")
print(f"{curso: >30}")
print(f"{curso: <30}")
print(f"{curso: ^20.10s}")
