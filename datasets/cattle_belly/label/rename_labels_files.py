import os
import pandas as pd

input_dir_train = '../datasets/cattle_belly/labels/train'
input_dir_valid = '../datasets/cattle_belly/labels/valid'

input_dir_csv_files = '../datasets/cattle_belly/labels'
 
train_labels_info = pd.read_csv(input_dir_csv_files + '/train.csv')
train_labels_info['label'] = train_labels_info.image.apply(lambda x: x.split('-')[-1])
train_labels_info['label'] = train_labels_info.label.apply(lambda x: x.split('.')[0] + '.txt')
train_labels_info['id'] = train_labels_info['id'].apply(lambda x: int(x))

valid_labels_info = pd.read_csv(input_dir_csv_files + '/valid.csv')
valid_labels_info['label'] = valid_labels_info.image.apply(lambda x: x.split('-')[-1])
valid_labels_info['label'] = valid_labels_info.label.apply(lambda x: x.split('.')[0] + '.txt')
valid_labels_info['id'] = valid_labels_info['id'].apply(lambda x: int(x))


def get_id_from_filename(filename):
    return int(filename.split('-')[1])

def pass_info_from_files(filename_1, filename_2):
    f1 = open(filename_1, 'a+')
    f2 = open(filename_2, 'r')
    f1.write(f2.read())
    f1.close()
    f2.close()

files = []
for file_name in os.listdir(input_dir_train):
    # print(files)
    id = get_id_from_filename(file_name)

    if id in files:
        print('repeated file with id: ' + str(id))
        file_1 = input_dir_train + '/' + train_labels_info.label[train_labels_info.id == id].iloc[0]
        file_2 = input_dir_train + '/'+ file_name
        print('joining labels into the file: ' + file_1)
        pass_info_from_files(file_1, file_2)
        print('-----/----/----/....done!')
        
    if id not in files:
        print(id)
        os.rename(input_dir_train + '/'+ file_name, input_dir_train + '/' + train_labels_info.label[train_labels_info.id == id].iloc[0])
        files.append(id)



for file_name in os.listdir(input_dir_valid):
    # print(files)
    id = get_id_from_filename(file_name)

    if id in files:
        print('repeated file with id: ' + str(id))
        file_1 = input_dir_valid + '/' + valid_labels_info.label[valid_labels_info.id == id].iloc[0]
        file_2 = input_dir_valid + '/'+ file_name
        print('joining labels into the file: ' + file_1)
        pass_info_from_files(file_1, file_2)
        print('-----/----/----/....done!')
        
    if id not in files:
        print(id)
        os.rename(input_dir_valid + '/'+ file_name, input_dir_valid + '/' + valid_labels_info.label[valid_labels_info.id == id].iloc[0])
        files.append(id)









        