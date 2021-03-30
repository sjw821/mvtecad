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
    tar.extractall(path=data_dir)
