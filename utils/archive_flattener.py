import os
import shutil

class ArchiveFlattener:

    BASE_PATH = "//Volumes//AZ_SSD512Gb//DAAN570_Project//MultiModHandGestUAV" # Change to where the original data is kept.
    FLATTENED_PATH = "//Volumes//AZ_SSD512Gb//DAAN570_Project//DAAN570_Data"

    def flatten_all(self):
       skip_check = 0
       os.mkdir(self.FLATTENED_PATH)
       subjects = os.listdir(self.BASE_PATH)


       for subject in subjects:
           print(f"Subject: {subject}")
           gestures = os.listdir(f"{self.BASE_PATH}//{subject}//images")

           for gesture in gestures:
                try:
                    os.mkdir(f"{self.FLATTENED_PATH}//{gesture}")
                except Exception as e:
                    skip_check += 1 # We will silently eat an existing dir error

                training_images = os.listdir(f'{self.BASE_PATH}//{subject}//images//{gesture}//train')
                testing_images = os.listdir(f'{self.BASE_PATH}//{subject}//images//{gesture}//test')

                print(
                    f"{gesture}: {len(training_images)} Training Images | {len(testing_images)} Testing Images"
                )
               
                index = 1

                for image in training_images:
                    new_filename = f"sub{subject}_{gesture}_{index:{'0'}{4}}.png"
                    shutil.copyfile(
                        src=f"{self.BASE_PATH}//{subject}//images//{gesture}//train//{image}",
                        dst=f"{self.FLATTENED_PATH}//{gesture}//{new_filename}"
                    )
                    index+=1

                for image in testing_images:
                    new_filename = f"sub{subject}_{gesture}_{index:{'0'}{4}}.png"
                    shutil.copyfile(
                        src=f"{self.BASE_PATH}//{subject}//images//{gesture}//train//{image}",
                        dst=f"{self.FLATTENED_PATH}//{gesture}//{new_filename}"
                    )
                    index+=1


if __name__ == "__main__":
    flattener = ArchiveFlattener()
    flattener.flatten_all()