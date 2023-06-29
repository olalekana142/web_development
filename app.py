from flask import Flask, render_template
app= Flask(__name__)

JOBS =[{
    id:1,
    'title':'Data Analyst',
    'location':'Lagos,Nigeria',
    'salary':'N250,000'   
},
{
    id:2,
    'title':'Data Scientist',
    'location':'Abuja,Nigeria',
    'salary':'N400,000'   
},
{
    id:3,
    'title':'Frontend Engineer',
    'location':'Kano,Nigeria',
    'salary':'N280,000'   
},
{
    id:4,
    'title':'Backend Engineer',
    'location':'Port Harcourt,Nigeria',
    'salary':'N350,000'  
}


]

@app.route('/')
def hello_lecxy():
    return render_template('Home.html', jobs=JOBS) 

if __name__ == '__main__':
    app.run(host='0.0.0.0',debug=True)


