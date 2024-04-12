from iiif_prezi3 import Manifest, config

config.configs['helpers.auto_fields.AutoLang'].auto_lang = "en"

manifest = Manifest(id="https://iiif.io/api/cookbook/recipe/0005-image-service/manifest.json", label="Picture of Göttingen taken during the 2019 IIIF Conference")
canvas = manifest.make_canvas_from_iiif(url="https://dl.tufts.edu/images/rr172152n%2Ffiles%2F3f8cfbbc-132b-4e74-b107-2008cf97a18f%2Ffcr:versions%2Fversion1",
                                        id="https://iiif.io/api/cookbook/recipe/0005-image-service/canvas/p1",
                                        label="Canvas with a single IIIF image",
                                        anno_id="https://iiif.io/api/cookbook/recipe/0005-image-service/annotation/p0001-image",
                                        anno_page_id="https://iiif.io/api/cookbook/recipe/0005-image-service/page/p1/1")

print(manifest.json(indent=2))
with open("/tmp/slash.manifest.json", mode='w') as f:
    print(manifest.json(indent=2), file=f)