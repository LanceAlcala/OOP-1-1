#Note: Both Program 1 and Program 2 is in this python file,
#the first program that will run is Program 1,
# the Program 2 will automatically run when Program 1 is done running.
print("Note: Both Program 1 and Program 2 is in this python file, the first program that will run is Program 1, the Program 2 will automatically run when Program 1 is done running.")


#Program 1: Modify the program below by adding two conversion methods
# - Fahrenheit to Celsius and Kelvin to Celsius (50 points)
def main():
 class TemperatureConversion:
  def __init__(self, temp=1):
   self._temp = temp
 class CelsiusToFahrenheit(TemperatureConversion):
  def conversion(self):
   return round((self._temp * 9) / 5 + 32,2)
 class CelsiusToKelvin(TemperatureConversion):
  def conversion(self):
   return round(self._temp + 273.15,2)

#modification
 class FahrenheitToCelsius (TemperatureConversion):
   def conversion(self):
     return round((self._temp - 32) * 5/9,2)

 class KelvinToCelsius (TemperatureConversion):
   def conversion(self):
     return round(self._temp - 273.15,2)


 tempInCelsius = float(input("Enter the temperature in Celsius: "))
 convert = CelsiusToKelvin(tempInCelsius)
 print(str(convert.conversion()) + " Kelvin")
 convert = CelsiusToFahrenheit(tempInCelsius)
 print(str(convert.conversion()) + " Fahrenheit")

#modification
 tempInFahrenheit = float(input("Enter the temperature in Fahrenheit: "))
 convert = FahrenheitToCelsius(tempInFahrenheit)
 print(str(convert.conversion()) + " Celsius")

 tempInKelvin = float(input("Enter the temperature in Kelvin: "))
 convert = KelvinToCelsius(tempInKelvin)
 print(str(convert.conversion()) + " Celsius")

main()


#Program 2. Create a program to produce the interface.
# After typing the name in the first text field,
# click the button to display the name to another text field.
# (Hint: See the figures.  - 50 points)
from tkinter import *
class Midterm:
    def __init__(self,mid):
        self.label1=Label(mid,text="Enter your fullname:", fg="red")
        self.label1.place(x=45,y=100)

        self.field1=Entry(bd=3,font=12)
        self.field1.place(x=250,y=100)

        self.button1=Button(mid,text="Click to display your Fullname",fg="red",command=self.display)
        self.button1.place(x=45,y=150)

        self.field2=Entry(bd=3,font=12)
        self.field2.place(x=250,y=150)

    def display(self):
        self.field2.delete(0, 'end')
        name=str(self.field1.get())
        self.field2.insert(END,str(name))


window = Tk()
mywin = Midterm(window)
window.title('Midterm in OOP')
window.geometry("500x310+10+20")
window.mainloop()