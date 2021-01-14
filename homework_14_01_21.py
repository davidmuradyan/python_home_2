import os


print(F"Now we are here: {os.getcwd()}")

os.chdir(r"C:\Users\david\Desktop")
print(F"Moved to here: {os.getcwd()}")

os.mkdir('Current_work_dir')
print("Made a new folder named 'Current_work_dir'!")
# print(os.listdir())

os.chdir(r"C:\Users\david\Desktop\Current_work_dir")
print(F"Moved to our newmade dir: {os.getcwd()}!")

with open("file.txt", "a"):
	pass
print("Created a new file inside 'Current_work_dir' named 'file.txt'!")

os.mkdir("Dir1")
print("Created a new dir inside 'Current_work_dir' named 'Dir1'!")
 
os.chdir(r"C:\Users\david\Desktop\Current_work_dir\Dir1")
print(F"Moved to: {os.getcwd()}!")

folder_list = ["Dir2", "Dir3"]
for i in folder_list:
	os.mkdir(i)
	print(F"Created a new dir inside Dir 1 named {i}!")

os.chdir(r"C:\Users\david\Desktop\Current_work_dir\Dir1\Dir3")
print(F"Moved to: {os.getcwd()}!")

os.mkdir("Dir4")
print("Created a new dir inside Dir3 named Dir4!")

print("\n")
print("Removing everything we created!\n")

os.rmdir("Dir4")
print("Removed Dir4!")

os.chdir(r"C:\Users\david\Desktop\Current_work_dir\Dir1")
print(F"Moved to: {os.getcwd()}!")

for i in os.listdir():
	os.rmdir(i)
print(F"Removed items from {os.getcwd()}!")

os.chdir(r"C:\Users\david\Desktop\Current_work_dir")
print(F"Moved to: {os.getcwd()}!")

os.rmdir("Dir1")
print("Removed Dir1!")
os.remove("file.txt")
print("Removed 'file.txt'!")

os.chdir(r"C:\Users\david\Desktop")
print(F"Moved to: {os.getcwd()}!")

os.rmdir("Current_work_dir")
print("Removed 'Current_work_dir'!")