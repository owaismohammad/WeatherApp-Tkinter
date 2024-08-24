import requests
import customtkinter as ctk
import tkinter 
import random
from tkinter import messagebox
from PIL import Image, ImageTk
from time import strftime

def mytime():
    time=strftime('%H:%M:%S %p\n%A\t%x')
    time_label.configure(text=time)
    time_label.after(1000,mytime)


window=tkinter.Tk()

window.geometry('1100x620')
window.configure(bg="cornflowerblue")
window.title('Weather')


ctk.set_appearance_mode("Light")



def Temperature():
    soft_colors = [
    "#FFB6C1",  # Light Pink
    "#FFF0F5",  # Lavender Blush
    "#FFDAB9",  # Peach Puff
    "#B0E0E6",  # Powder Blue
    "#F5FFFA",  # Mint Cream
    "#F0F8FF",  # Alice Blue
    "#E6E6FA",  # Lavender
    "#FFF8DC",  # Cornsilk
    "#FFFACD",  # Lemon Chiffon
    "#F0FFF0",  # Honeydew
    "#FFFAF0",  # Floral White
    "#F0FFFF",  # Azure
    "#C4C3D0",  # Lavender Gray
    "#E0FFFF",  # Light Cyan
    "#FFF5EE",  # Seashell
    "#FDF5E6",  # Old Lace
    "#F5F5DC",  # Beige
    "#FAFAD2",  # Light Goldenrod Yellow
    "#ADD8E6",  # Light Blue
    "#B0C4DE"   # Light Steel Blue
]


# window.configure(bg=soft_colors[random.randint(0,20)])

    city_name=city_entry.get().upper()
    city_entry.delete(0, ctk.END)
    API_Key='da8b8fa8abdeabf1aeffde38f7da00d0'
    url=f'https://api.openweathermap.org/data/2.5/weather?q={city_name}&appid={API_Key}&units=metric'

    response=requests.get(url)
    data=response.json()
    
    


    if response.status_code==404:
        messagebox.showerror(title='Error', message=f'The entered city {city_name} does not exist')
    elif city_name=="":
        messagebox.showwarning(title='Error', message=f'Please enter the name of a city')
    else:
        temp=data['main']['temp']


    

        if temp<=0:
            window.configure(bg="#87CEEB")
        elif temp>0 and temp<10:
            window.configure(bg='#66CCFF')
        elif temp>10 and temp<20:
            window.configure(bg='##66CCCC')
        elif temp>20 and temp<30:
            window.configure(bg='#FFB347')
        elif temp>30 and temp<40:
            window.configure(bg='#FFA079')
        elif temp>40 and temp<50:
            window.configure(bg='#FF0000')
        elif temp>50 and temp<60:
            window.configure(bg='#FF4500')

        cityname_label=ctk.CTkLabel(temp_frame, text=f"{city_name}", font=('Broadway', 30),text_color='midnightblue')
        cityname_label.grid(row=0, column=1,  pady=20)

        temp_label=ctk.CTkLabel(temp_frame, text=f"{data['main']['temp']}°C", font=('Calibri', 20))
        temp_label.grid(row=3, column=0, padx=30, pady=(0,15) )

        humidity_label=ctk.CTkLabel(temp_frame, text=f"{data['main']['humidity']}%", font=('Calibri', 20))
        humidity_label.grid(row=3, column=1, padx=30, pady=(0,15))

        feelslike_label=ctk.CTkLabel(temp_frame, text=f"{data['main']['feels_like']}°C", font=('Calibri', 20))
        feelslike_label.grid(row=3, column=2, padx=30, pady=(0,15))

        weather_label=ctk.CTkLabel(temp_frame, text=f"{data['weather'][0]['description'].upper()}", font=('Calibri', 20))
        weather_label.grid(row=6, column=0, padx=30, pady=(0,15))

        pressure_label=ctk.CTkLabel(temp_frame, text=f"{data['main']['pressure']} hPa", font=('Calibri', 20))
        pressure_label.grid(row=6, column=1, padx=30, pady=(0,15))

        wind_label=ctk.CTkLabel(temp_frame, text=f"{data['wind']['speed']} m/s", font=('Calibri', 20))
        wind_label.grid(row=6, column=2, padx=30, pady=(0,15))


#Weather icon
weather =Image.open('weather.png').resize((60,60))
weather_tk=ImageTk.PhotoImage(weather)

iconlabel=ctk.CTkLabel(window,text="", image=weather_tk)
iconlabel.pack(side="left", padx=(20,0))


title_label=ctk.CTkLabel(window, text='Weather' , font=('Broadway', 60),text_color='midnightblue')
title_label.pack(side="left", padx=(0,1),pady=(10,1))

time_label=ctk.CTkLabel(window, font=('Broadway', 30), text_color='midnightblue')
time_label.pack(side='top',pady=(20,0))

city_entry=ctk.CTkEntry(window, placeholder_text='Enter City Name', width=300)
city_entry.pack(pady=(90,10))



search_button=ctk.CTkButton(window, text='Search', command=Temperature, corner_radius=30, fg_color='midnightblue', hover_color='grey')
search_button.pack(pady=(0,10))





#temp icon

image_original =Image.open('tempicon.png').resize((40,40))
image_tk=ImageTk.PhotoImage(image_original)

#humidity icon
humidity_original =Image.open('humidity.png').resize((40,40))
humidity_tk=ImageTk.PhotoImage(humidity_original)

#feels like icon
feelslike =Image.open('feelslike.png').resize((40,40))
feelslike_tk=ImageTk.PhotoImage(feelslike)

#atmosphere like icon
atmosphere =Image.open('atmosphere.png').resize((40,40))
atmosphere_tk=ImageTk.PhotoImage(atmosphere)

#pressure like icon
pressure =Image.open('pressure.png').resize((40,40))
pressure_tk=ImageTk.PhotoImage(pressure)


#windspeed like icon
wind =Image.open('wind.png').resize((40,40))
wind_tk=ImageTk.PhotoImage(wind)


temp_frame=ctk.CTkFrame(window, width=400, height=200)
temp_frame.pack()

temp_img_label=ctk.CTkLabel(temp_frame,font=('Calibri',1),image=image_tk)
temp_img_label.grid(row=1, column=0, padx=30, pady=(15,0))
temp_label=ctk.CTkLabel(temp_frame, text=f"Temperature", font=('Broadway', 22))
temp_label.grid(row=2, column=0, padx=30)
mytime()

humidity_img_label=ctk.CTkLabel(temp_frame, font=('Calibri',1), image=humidity_tk)
humidity_img_label.grid(row=1, column=1, padx=30, pady=(15,0))
humidity_label=ctk.CTkLabel(temp_frame, text=f"Humidity", font=('Broadway', 22))
humidity_label.grid(row=2, column=1, padx=30)

feelslike_img_label=ctk.CTkLabel(temp_frame, text=f"f",  font=('Calibri',1), image=feelslike_tk)
feelslike_img_label.grid(row=1, column=2, padx=30, pady=(15,0))
feelslike_label=ctk.CTkLabel(temp_frame, text=f"Feels like", font=('Broadway', 22))
feelslike_label.grid(row=2, column=2, padx=30)

weather_img_label=ctk.CTkLabel(temp_frame, text=f"A", font=('Calibri', 1), image=atmosphere_tk)
weather_img_label.grid(row=4, column=0, padx=30, pady=(15,0))
weather_label=ctk.CTkLabel(temp_frame, text=f"Atmosphere", font=('Broadway', 22))
weather_label.grid(row=5, column=0, padx=30)

pressure_img_label=ctk.CTkLabel(temp_frame, text=f"f", font=('Calibri', 1), image=pressure_tk)
pressure_img_label.grid(row=4, column=1, padx=30, pady=(15,0))
pressure_label=ctk.CTkLabel(temp_frame, text=f"Pressure", font=('Broadway', 22))
pressure_label.grid(row=5, column=1, padx=30)


wind_img_label=ctk.CTkLabel(temp_frame, text=f"W", font=('Calibri', 1), image=wind_tk)
wind_img_label.grid(row=4, column=2, padx=30, pady=(15,0))
wind_label=ctk.CTkLabel(temp_frame, text=f"Wind Speed", font=('Broadway', 22))
wind_label.grid(row=5, column=2, padx=30)



window.mainloop()

