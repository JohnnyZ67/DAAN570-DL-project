from PIL import Image
import matplotlib as plt
import os
import json

class MetaGenerator:

    DATA_PATH = "D://Resources//DAAN_570_Archive//DAAN570_Data"

    def generate_meta(self):
        metadata = {
            "gestures": {},
            "sizes": {}
        }
        gestures = os.listdir(self.DATA_PATH)
        
        for gesture in gestures:
            print(f"Gesture: {gesture}")
            images = os.listdir(f"{self.DATA_PATH}//{gesture}")
            print(f"{gesture} contains {len(images)} total images")

            metadata['gestures'][f"{gesture}_count"] = len(images)

            for image in images:
                with Image.open(f"{self.DATA_PATH}//{gesture}//{image}") as file:
                    size = f"{file.size[0]}x{file.size[1]}"

                    if size in metadata['sizes'].keys():
                        metadata['sizes'][size] = metadata['sizes'][size]+1
                    else:
                        metadata['sizes'][size] = 1

        print(metadata)
        with open('metadata.json', 'w') as f:
            json.dump(metadata, f)


if __name__ == "__main__":
    flattener = MetaGenerator()
    flattener.generate_meta()