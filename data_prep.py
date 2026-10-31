from datasets import load_dataset

# تحميل داتا سيت CoNaLa من هقن فايس والتأكد من التقسيمات المطلوبة للميلستون
dataset = load_dataset("neulab/conala", "all")

train_data = dataset['train'].select(range(2141))
val_test_split = train_data.train_test_split(test_size=238, seed=42)
train_dataset = val_test_split['train']
val_dataset = val_test_split['test']
test_dataset = dataset['test'].select(range(500))

# طباعة أحجام البيانات (Printout المطلوب للميلستون)
print(f"Train Set Size: {len(train_dataset)}")
print(f"Validation Set Size: {len(val_dataset)}")
print(f"Test Set Size: {len(test_dataset)}")
