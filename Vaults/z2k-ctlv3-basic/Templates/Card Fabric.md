---
z2k_template_type: block-template
z2k_template_author: "Z2K Studios, LLC"
FabricMentalModel: "{{FabricMentalModel}}"
FabricContextual: "{{FabricContextual}}"
FabricReference: "{{FabricReference}}"
FabricGeoContext: "{{FabricGeoContext}}"
---
{{fieldInfo FabricMentalModel "Mental models relevant to this card?" type="text"}}
{{fieldInfo FabricContextual "Contextual connections?" type="text"}}
{{fieldInfo FabricReference "Reference links?" type="text"}}
{{fieldInfo FabricGeoContext "Geographic context?" type="text"}}

---
# Card Fabric
{{formatStringBulletize FabricMentalModel 0 "#### Mental Models\n"}}
{{formatStringBulletize FabricContextual 0 "#### Contextual\n"}}
{{formatStringBulletize FabricReference 0 "#### References\n"}}
{{formatStringBulletize FabricGeoContext 0 "#### GeoContext\n"}}
---
