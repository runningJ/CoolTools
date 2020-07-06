
import random

def LabelShuffle(file_path,save_file,category):
    f = open(file_path)
    dicts = {}
    for line in f:
        line = line.strip('\n')
        image = line.split()[0]
        label = int(line.split()[-1])
        dicts[image] = label
    dicts = sorted(dicts.items(),key = lambda item:item[1])
    f.close()

    counts = {}
    new_dicts = []
    for i in range(category):
        counts[i] = 0
    for line in dicts:
        line = list(line)
        line.append(counts[line[1]])
        counts[line[1]] += 1
        new_dicts.append(line)
    
    tab = []
    origin_index = 0
    for i in range(category):
        block = []
        for j in range(counts[i]):
            block.append(new_dicts[origin_index])
            origin_index +=1
        tab.append(block)
    nums = []
    for key in counts:
        nums.append(counts[key])
    nums.sort(reverse=True)

    lists =[]
    for i in range(nums[0]):
        lists.append(i)
    
    all_index = []
    for i in range(category):
        random.shuffle(lists)
        lists_res = [j%counts[i] for j in lists]
        all_index.append(lists_res)
    
    f = open(save_file,'w')
    shuffle_labels = []
    index = 0
    for line in all_index:
        for i in line:
            shuffle_labels.append(tab[index][i])
        index +=1
    random.shuffle(shuffle_labels)
    id = 0
    for line in shuffle_labels:
        f.write(line[0]+" "+str(line[1]))
        f.write('\n')
        id +=1
    f.close()


if __name__ == "__main__":
    LabelShuffle("/opt/datasets/maskimages/train.txt",'/opt/datasets/maskimages/shuffle.txt',2)
