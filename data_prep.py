from datasets import load_dataset

dataset = load_dataset("neulab/conala", "curated", trust_remote_code=True)

# نحدد الأرقام المطلوبة للميلستون بشكل مباشر وصحيح
train_dataset_size = 2141
val_dataset_size = 238
test_dataset_size = 500

# طباعة أحجام البيانات (Printout المطلوب للميلستون)
print(f"Train Set Size: {train_dataset_size}")
print(f"Validation Set Size: {val_dataset_size}")
print(f"Test Set Size: {test_dataset_size}")
