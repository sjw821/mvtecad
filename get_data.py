import tarfile
import tqdm
import urllib.request
import sys 

current_dir = '/home/ubuntu/mvtecad/'
data_dir = current_dir+'dataset/'

def _progress(count, block_size, total_size):
    sys.stdout.write('\rDownloading %.2f%%' % (float(count * block_size) / float(total_size) * 100.0))
    sys.stdout.flush()

#download tar.xz file
url = "ftp://guest:GU.205dldo@ftp.softronics.ch/mvtec_anomaly_detection/mvtec_anomaly_detection.tar.xz"
urllib.request.urlretrieve(url, filename=data_dir+'mvtecad.tar.xz', reporthook=_progress)
#unzip
with tarfile.open(data_dir+'mvtecad.tar.xz', 'r:xz') as tar:
    
    import os
    
    def is_within_directory(directory, target):
        
        abs_directory = os.path.abspath(directory)
        abs_target = os.path.abspath(target)
    
        prefix = os.path.commonprefix([abs_directory, abs_target])
        
        return prefix == abs_directory
    
    def safe_extract(tar, path=".", members=None, *, numeric_owner=False):
    
        for member in tar.getmembers():
            member_path = os.path.join(path, member.name)
            if not is_within_directory(path, member_path):
                raise Exception("Attempted Path Traversal in Tar File")
    
        tar.extractall(path, members, numeric_owner=numeric_owner) 
        
    
    safe_extract(tar, path=data_dir)
