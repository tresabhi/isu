import bpy
import json

# Output file path
output_file = "mesh_data.json"

mesh_data = []

# Iterate through all objects in the scene
for obj in bpy.context.scene.objects:
    if obj.type == "MESH":
        mesh_obj = {}
        mesh_obj["name"] = obj.name
        mesh_obj["vertices"] = []
        mesh_obj["indices"] = []

        obdata = obj.data

        # Extract vertices info
        for v in obdata.vertices:
            mesh_obj["vertices"].append([v.co.x, v.co.y, v.co.z])

        # Extract edge indices info and convert to continuous path
        visited = set()
        for e in obdata.edges:
            if e.index not in visited:
                visited.add(e.index)
                mesh_obj["indices"].append(e.vertices[0])
                current_vertex = e.vertices[1]
                while True:
                    next_edge = [
                        edge
                        for edge in obdata.edges
                        if current_vertex in edge.vertices and edge.index not in visited
                    ]
                    if not next_edge:
                        break
                    next_edge = next_edge[0]
                    visited.add(next_edge.index)
                    mesh_obj["indices"].append(current_vertex)
                    current_vertex = (
                        next_edge.vertices[1]
                        if next_edge.vertices[0] == current_vertex
                        else next_edge.vertices[0]
                    )

        mesh_data.append(mesh_obj)

# Write mesh data to JSON file
with open(output_file, "w") as file:
    json.dump(mesh_data, file, indent=4)

print("Mesh data saved to:", output_file)
