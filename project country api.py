from tkinter import *
import requests
import json
root=Tk()
root.title("My Country Api")
root.geometry("400x600")
root.overrideredirect(True)

root.configure(background="white")
#Setting labels
capital_city_name_label=Label(root, text="Capital City Name",font=("Helvetica", 18,'bold'),bg="white")
capital_city_name_label.place(relx=0.35,rely=0.15,anchor=CENTER)

city_entry=Entry(root)
city_entry.place(relx=0.24,rely=0.35,anchor=CENTER)

Country_name = Label(root,text="Country: ", bg="white", font=("bold", 10))
Country_name.place(relx=0.1,rely=0.45,anchor=CENTER) 

Region= Label(root,text="Region: ", bg="white", font=( "bold",10)) 
Region.place(relx=0.1,rely=0.55,anchor=CENTER) 

language= Label(root,text="Language: ", bg="white", font=( "bold",10)) 
language.place(relx=0.1,rely=0.65,anchor=CENTER) 

population= Label(root,text="Population: ", bg="white", font=( "bold",10)) 
population.place(relx=0.1,rely=0.75,anchor=CENTER) 

Area= Label(root,text="Area: ", bg="white", font=( "bold",10)) 
Area.place(relx=0.1,rely=0.85,anchor=CENTER) 
    
def city_name():
    api_request = requests.get("https://restcountries.com/v3.1/capital/" + city_entry.get())
    
    api_output_json = json.loads(api_request.content)
    
    country_info=api_output_json[0]["name"]["common"]
    print(country_info)
    
    reg=api_output_json[0]['region']
    print(reg)
    
    lang_info=api_output_json[0]["translations"]["cym"]
    print(lang_info)
    
    pop=api_output_json[0]['population']
    print(pop)
    
    area=api_output_json[0]['area']
    print(area)
    
    Country_name["text"]="Country: " + str(country_info)
    Region["text"]="Region: " + str(reg)
    language["text"]="Language: " + str(lang_info)
    population["text"]="Population: " + str(pop)
    Area["text"]="Area: " + str(area)
    
    
search_btn=Button(root, text="Search", command= city_name, relief=FLAT)
search_btn.place(relx=.5,rely=0.48,anchor=CENTER)
    
root.mainloop()
