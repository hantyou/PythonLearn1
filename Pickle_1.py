# 将Python对象转化为二进制流对象存放
import pickle

my_list = [123, 3.14, 'Daniel', ['A sub_list']]
print(my_list)
pickle_file = open('Daniel.pkl', 'wb')
pickle.dump(my_list, pickle_file)
pickle_file.close()
# 先open pickle文件，再用pickle.load
pickleRe = open('Daniel.pkl', 'rb')
my_listRe = pickle.load(pickleRe)
print(my_listRe)
