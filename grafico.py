import plotly.graph_objects as go

# Nodos del diagrama
labels = [
    "Paneles FV (4000 W)",   # 0
    "Inversor (3800 W)",     # 1
    "Cargas (1120 W)",       # 2
    "Excedente (2680 W)",    # 3
    "Pérdidas (200 W)"       # 4
]

# Conexiones (source → target)
sources = [0, 1, 1, 0]   # desde
targets = [1, 2, 3, 4]   # hacia
values  = [4000, 1120, 2680, 200]

# Crear Sankey
fig = go.Figure(data=[go.Sankey(
    node=dict(
        pad=20, thickness=20,
        line=dict(color="black", width=0.5),
        label=labels,
        color=["#66b3ff", "#99ccff", "#99ff99", "#ccffcc", "#ff9999"]
    ),
    link=dict(
        source=sources,
        target=targets,
        value=values
    )
)])

# Configuración
fig.update_layout(
    title_text="Flujo de potencia: Paneles → Inversor → Sistema",
    font_size=12
)

# Mostrar en ventana interactiva (navegador)
fig.show()

# Guardar como imagen (requiere instalar "kaleido": pip install kaleido)
fig.write_image("sankey_potencia.png", scale=2)
