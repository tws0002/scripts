# -*- coding: utf-8 -*-
"""
Created on Wed Oct 14 09:25:39 2015

@author: julio
"""
import pickle

nameFile = r"c:\nameList.txt"
loginFile = r"c:\loginList.txt"

with open(nameFile, "r") as n:
    names = n.read().splitlines()

with open(loginFile, "rb") as l:
    logins = pickle.load(l)

#-----------------------------------------------------------------------
#IMPORTANT!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
#
#請檢查 nameFile 跟 loginF 的路徑
#
#IMPORTANT!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!

# 1. logins 資料類型是? 若有子資料類型，請也列出來

# 2. names 資料類型是? 若有子資料類型，請也列出來

# 3. 請把你的資料從 logins 裡找出來 
# 請寫成 function, return dictionary
def findYourself():
	# 寫這裡	

# 4. 請從 logins 裡找出大家的分機號碼(ext), 做成一個新的list
# 請寫成 function, return list
def allExt():
	# 寫這裡	

# 5. 請從 logins 裡找出大家的分機號碼(ext), 做成一個新的dictionary list, 
# 裡面有 login 跟 ext
# 請寫成 function, return dictionary list
def allExtDict():
	# 寫這裡	

def main():
	findYourself()
	allExt()
	allExtDict()

if __name__ == '__main__':
	main()	 





