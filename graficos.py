import pandas as pd
import matplotlib.pyplot as plt
from matplotlib import cm
from mpl_toolkits.mplot3d import Axes3D
import numpy as np

df = pd.read_csv("successful_educations.csv")
grouped = df.groupby(["Degree", "Field"]).size().reset_index(name='Count')
education_levels = grouped['Degree'].unique()
fields = grouped['Field'].unique()

# Mapeo de indices
edu_to_idx = {edu: i for i, edu in enumerate(education_levels)}
field_to_idx = {fld: i for i, fld in enumerate(fields)}

#La magia
x = [edu_to_idx[edu] for edu in grouped['Degree']]
y = [field_to_idx[fld] for fld in grouped['Field']]
z = np.zeros(len(grouped))  # base de las barras
dx = dy = 0.5
dz = grouped['Count']

#Se crea el grafico
fig = plt.figure(figsize=(16, 12))
ax = fig.add_subplot(111, projection='3d')

norm = plt.Normalize(min(dz), max(dz))
colors = cm.viridis(norm(dz))

ax.bar3d(x, y, z, dx, dy, dz, shade=True, color=colors)

#Etiqueta ejes
top_edu = df['Degree'].value_counts().nlargest(5).index.tolist()
xtick_labels = [degree if degree in top_edu else '' for degree in edu_to_idx.keys()]
ax.set_xticks(list(edu_to_idx.values()))
ax.set_xticklabels(xtick_labels, rotation=45, ha='right', fontsize=8)

top_fields = df['Field'].value_counts().nlargest(5).index.tolist()
ytick_labels = [field if field in top_fields else '' for field in field_to_idx.keys()]
ax.set_yticks(list(field_to_idx.values()))
ax.set_yticklabels(ytick_labels, fontsize=8)

ax.set_zlabel('Cantidad')
ax.set_xlabel('Grado Educacional')
ax.set_ylabel('Campo')
ax.set_title('Distribución de niveles educativos por campo profesional')


plt.tight_layout()
plt.show()

#Top Grados
top_educations = df['Degree'].value_counts().sort_values(ascending=False)
print("\nNiveles educativos más comunes:")
for grado, cantidad in top_educations.head(10).items():
    print(f"Grado: {grado} - Cantidad: {cantidad}")
#Nivel x campo solo 3 
print("\nNiveles educativos más comunes por campo:")
for field in df['Field'].unique():
    counts = df[df['Field'] == field]['Degree'].value_counts().head(3)
    print(f"\nCampo: {field}")
    for grado, cantidad in counts.items():
        print(f"  Grado: {grado} - Cantidad: {cantidad}")
