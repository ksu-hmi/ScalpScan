import os
import cv2

train_dir = r"C:\Users\shake\OneDrive\Scalp Scan Project\dataset\Train"
val_dir = r"C:\Users\shake\OneDrive\Scalp Scan Project\dataset\Val"

def load_images_from_folder(folder_path):
    if not os.path.exists(folder_path):
        print(f"❌ Folder not found: {folder_path}")
        return

    print(f"\n📂 Loading images from: {folder_path}")
    
    for filename in os.listdir(folder_path):
        if filename.lower().endswith(('.jpg', '.jpeg', '.png')):
            path = os.path.join(folder_path, filename)
            try:
                img = cv2.imread(path)
                if img is not None:
                    print(f"✅ Loaded: {filename}")
                    # Optional: show image (commented for faster batch testing)
                    # cv2.imshow("Image", img)
                    # cv2.waitKey(300)  # View image for 300 ms
                else:
                    print(f"❌ Could not read image: {filename}")
            except Exception as e:
                print(f"❌ Error loading {filename}: {e}")

# Load from both Train and Val folders
load_images_from_folder(os.path.join(train_dir, "Normal"))
load_images_from_folder(os.path.join(train_dir, "Alopecia_Areata"))
load_images_from_folder(os.path.join(train_dir, "Androgenetic_Alopecia"))

load_images_from_folder(os.path.join(val_dir, "Normal"))
load_images_from_folder(os.path.join(val_dir, "Alopecia_Areata"))
load_images_from_folder(os.path.join(val_dir, "Androgenetic_Alopecia"))

# cv2.destroyAllWindows()  # Uncomment if you show images
