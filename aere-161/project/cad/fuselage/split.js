import { writeFile } from "fs/promises";
import meshData from "./mesh_data.json" assert { type: "json" };

/**
 * 31: self intersections
 * 40: self intersections
 *
 * 5: self intersections
 * 10: self intersections
 */

console.log(meshData);

meshData.forEach((mesh, meshIndex) => {
  const vertices = mesh.indices.map((index) => mesh.vertices[index]);
  let lines = vertices
    // .sort((a, b) => Math.atan2(a[1], a[2]) - Math.atan2(b[1], b[2]))
    .map((v) => `${v.join(",")}`)
    .filter((value, index, array) => array.indexOf(value) === index);
  lines = [...lines, lines[0]];

  writeFile(`proj1/fuselage/generated/${meshIndex}.txt`, lines.join("\n"));
});
