import extractor
import testmodel as tm
filename = input("Enter File Name : ")
metadata = extractor.get_metadata(filename)
result = tm.predict(metadata)
print(result)
