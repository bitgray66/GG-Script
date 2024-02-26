from __future__ import print_function
import maya.cmds as cmds

def get_referenced_assets():
    referenced_nodes = cmds.ls(references=True)
    referenced_assets = []

    for ref_node in referenced_nodes:
        try:
            namespace = cmds.referenceQuery(ref_node, namespace=True)
            file_path = cmds.referenceQuery(ref_node, filename=True)
            nodes_in_reference = cmds.referenceQuery(ref_node, nodes=True)

            referenced_assets.append({
                'reference_node': ref_node,
                'namespace': namespace,
                'file_path': file_path,
                'nodes_in_reference': nodes_in_reference
            })
        except RuntimeError as e:
            print("Error processing reference node:", ref_node, "- Skipping. Error:", e)

    return referenced_assets

referenced_assets = get_referenced_assets()

for asset in referenced_assets:
    print("Reference Node:", asset['reference_node'])
    print("Namespace:", asset['namespace'])
    print("File Path:", asset['file_path'])
    print("Nodes in Reference:", asset['nodes_in_reference'])
    print("-" * 30)

projPath = cmds.workspace(q=True, dir=True) + 'GG.txt'
print("projPath: " + projPath)
f = open(projPath, 'w')
f.write('{0:*^50}'.format('Risultato') + '\n')
for asset in referenced_assets:
    f.write("Namespace: " + asset['namespace'] + '\n')
    f.write("-" * 30 + '\n')
f.close()
