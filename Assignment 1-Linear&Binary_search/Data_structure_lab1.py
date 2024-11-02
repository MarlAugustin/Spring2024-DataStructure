from tkinter import *
import tkinter as tk
from tkinter import messagebox
import random
array_size = 0
array = []
number = 0
class Interface:
    def __init__(self,window):
        self.window = window
        self.window.title("Marlond Data Structure Lab 1: Searches")
        self.window.configure(background='#cccccc')
        window.geometry("550x400")
        self.frame_instructions = Frame(window,bg="grey")
        self.frame_instructions.pack(side=TOP)
        self.frame_results = Frame(window)
        self.frame_results.pack(side=BOTTOM)

        #setting the array size
        self.lbl_array_size = Label(self.frame_instructions, text="Size of Array?")
        self.lbl_array_size.grid(column=0, row=0)
        self.txt_array_size = Entry(self.frame_instructions,width=20)
        self.txt_array_size.grid(column=1, row=0)
        self.btn_setup = Button(self.frame_instructions, text="Set up", command=self.btn_setup_clicked)
        self.btn_setup.grid(column=2, row=0)
        
        #search for specific number
        self.lbl_number = Label(self.frame_instructions, text="Search for #:")
        self.lbl_number.grid(column=0, row=1)
        self.txt_number = Entry(self.frame_instructions,width=20)
        self.txt_number.grid(column=1, row=1)

        #linear search
        self.btn_linear = Button(self.frame_instructions, text="Linear search", command=self.btn_linear_clicked)
        self.btn_linear.grid(column=0, row=3)

        #binary search
        self.btn_binary = Button(self.frame_instructions, text="Binary search", command=self.btn_binary_clicked)
        self.btn_binary.grid(column=2, row=3)

        #scrolling bar
        self.scroll_bar = Scrollbar(self.window)
        self.scroll_bar.pack( side = RIGHT, fill = Y ) 
        #array
        self.txt_array = Text(self.window, width=60, yscrollcommand = self.scroll_bar.set)
        self.txt_array.pack( side = LEFT, expand=True, fill = BOTH)
        self.scroll_bar.config( command = self.txt_array.yview ) 
    
        #number found
        self.lbl_number_found = Label(self.frame_results)
        self.lbl_number_found.grid(column=1, row=5)

        #result
        self.lbl_result = Label(self.frame_results, text="Results: ")
        self.lbl_result.grid(column=0, row=6)

        #result linear
        self.lbl_result_linear = Label(self.frame_results)
        self.lbl_result_linear.grid(column=1, row=6)

        #result binary
        self.lbl_result_binary = Label(self.frame_results)
        self.lbl_result_binary.grid(column=1, row=7)

    def btn_setup_clicked(self):
        global array_size, array
        if len(self.txt_array_size.get()) == 0 :
            messagebox.showerror("Empty Field", "Enter the size of the list")
        else:
            self.txt_array.delete(1.0,END)
            array_size = int(self.txt_array_size.get())
            array = []
            for i in range(0, array_size):
                array.append(random.randint(0,10))
            self.txt_array.insert(INSERT,", ".join(map(str, array)))
            #documentation for join https://www.geeksforgeeks.org/print-lists-in-python-4-different-ways/
        
        
    def btn_linear_clicked(self):
        #Big O(n)
        if len(self.txt_number.get()) == 0 :
            messagebox.showerror("Empty Field", "Enter a valid number")
        else:
            global array_size, array, number 
            number = int(self.txt_number.get())
            count = 0
            number_found = False
            if array_size != 0:
                self.txt_array.delete(1.0,END)
                self.txt_array.insert(INSERT,", ".join(map(str, array)))
            for i in range(0, array_size):
                if array[i] == number:
                    # messagebox.showinfo("Linear Search",  "Found "+str(number)+"!")
                    number_found = True
                    count = i
                    break
            if number_found == True:
                self.lbl_number_found.configure(text="Found "+str(number)+"!")
                self.lbl_result_linear.configure(text="Linear search for " + str(number) +" took " + str(count+1) + " steps")
            else:
                self.lbl_number_found.configure(text=str(number) +" Not found")
                self.lbl_result_linear.configure(text="Linear search for " + str(number) +" was not found. It took " + str(array_size) + " steps")
            
        
    def btn_binary_clicked(self):
        #Big O(log n)
        if len(self.txt_number.get()) == 0 :
            messagebox.showerror("Empty Field", "Enter a valid number")
        else:
            global array_size, array , number
            sorted_array = array
            sorted_array.sort()
            number = int(self.txt_number.get())
            minimum = 0
            maximum = array_size-1
            number_found = False
            count = 0
            if array_size != 0:
                self.txt_array.delete(1.0,END)
                self.txt_array.insert(INSERT,", ".join(map(str, sorted_array)))
            while (minimum <= maximum):
                middle = (minimum+maximum)//2
                count += 1
                if (sorted_array[middle] == number):
                    number_found = True
                    break
                elif (sorted_array[middle] < number):
                    minimum = middle + 1
                else:
                    maximum = middle - 1
            
            if number_found == True:
                self.lbl_number_found.configure(text="Found "+str(number)+"!")
                self.lbl_result_binary.configure(text="Binary search for " + str(number) +" took " + str(count) + " steps")
            else:
                self.lbl_number_found.configure(text=str(number) +" Not found")
                self.lbl_result_binary.configure(text="Binary search for " + str(number) +" was not found. It took " + str(count+1) + " steps")

if __name__ == "__main__":
    window = Tk()
    Interface(window)
    window.mainloop()
