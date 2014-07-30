import os.path;
import re;

REGEX_MATCH_FILE = r'.*\..*'

#File info
class file:

    _extension = 'Unknown';
    _name = 'Unkown';
    _owner= 'Unkown';
    _parent = 'Unkown';

    def __init__(self,path):
        _extension = 'Unkown';
        _name = 'Unknown';
        _owner = 'Unkown';

        pathext = str.split(path,'.',1);
        parent_filename = str.rsplit(pathext[0],'\\',1);

        self._parent = parent_filename[0];
        self._name = parent_filename[1];
        self._extension = pathext[1] if len(pathext) > 1 else 'Not a File';

    @staticmethod
    def IsFile(path):
        return os.path.isfile(path);
        #regexp = re.compile(REGEX_MATCH_FILE)
        #return regexp.search(path) is not None;



class Directory:

    def __init__(self,path):
        parent_filename = str.rsplit(path,'\\',1);
        self._path = path;
        self._parent = parent_filename[0];
        self._name = parent_filename[1];
        self._directory =[];
        self._files = [];
        dirs = os.listdir(path);
        for file_or_direc in os.listdir(path):
            if(file_or_direc is None):
                break;
            if(file.IsFile(path + '\\' + file_or_direc)):
                self._files.append(file(path + '\\' + file_or_direc));
            else:
                t_direc = Directory(path + '\\' + file_or_direc);
                self._directory.append(t_direc);
    
    def IsDirec(path):
        return os.path.isdir(path);
    def ContainsFile():
        return true;

    def ContainsFiles(FileDescriptor):
       if(FileDescriptor in Files or
          FileDescriptor in directorys):
           return true;
       else:
           return false;


def PrintDirectory(Directory, nested = ''):
    nested = nested + '---'
    for Direc in Directory._directory:
        print(nested + Direc._name);
        PrintDirectory(Direc,nested);

