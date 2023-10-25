#!/usr/bin/env python
# coding: utf-8

# In[1]:


import os, shutil


# In[2]:


def sdCreateFolder(Path,FolderName):
    # defining a name that will act as directory
    abspath = Path + '/' + FolderName
    try:
        os.mkdir(abspath)
    except OSError:
        print ("Creation of the directory %s failed" % abspath)
    else:
        print ("Successfully created the directory %s" % abspath)


# In[3]:


def sdDeleteFolder(Path,FolderName):
    # defining a name that will act as directory
    abspath = Path + "/" + FolderName
    try:
        os.rmdir(abspath)
    except OSError:
        print ("Deletion of the directory %s failed" % abspath)
    else:
        print ("Successfully deleted the directory %s" % abspath)


# In[4]:


def sdDelAllFilesInFolder(Path):
    for filename in os.listdir(Path):
        file_path = os.path.join(Path, filename)
        try:
            if os.path.isfile(file_path) or os.path.islink(file_path):
                os.unlink(file_path)
            elif os.path.isdir(file_path):
                shutil.rmtree(file_path)
        except Exception as e:
            print('Failed to delete %s. Reason: %s' % (file_path, e))


# In[ ]:




