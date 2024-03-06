import bpy

# Assicurati di usare il nome corretto dell'operazione per lo scambio dei collegamenti dei nodi
# Esempio ipotetico: bpy.ops.node.nw_swap_links()
bpy.ops.node.nw_swap_links()

# Correggi la definizione della lista dei file
files = [
    {"name": "MM_PRP_AlarmClock_A_A_DIF.png"},
    {"name": "MM_PRP_AlarmClock_A_A_NRM.png"},
    {"name": "MM_PRP_AlarmClock_A_A_RGH.png"}
]

# Aggiungi i percorsi dei file correttamente
bpy.ops.node.nw_add_textures_for_principled(
    filepath="R:\\Melody_Momon\\Production\\Assets\\Models\\PRP\\A\\MM_PRP_AlarmClock_A_A\\Tx\\Hi\\MM_PRP_AlarmClock_A_A_DIF.png",
    directory="R:\\Melody_Momon\\Production\\Assets\\Models\\PRP\\A\\MM_PRP_AlarmClock_A_A\\Tx\\Hi\\",
    files=files
)

